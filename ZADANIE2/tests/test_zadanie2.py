import re

import ZADANIE2.zadanie2 as sg


def rle_len(seq):
    # Pomocnicze liczenie dlugosci RLE dla calego ciagu (korzysta z sg.dlugosc)
    if not seq:
        return 0
    total = 0
    curr = seq[0]
    count = 1
    for ch in seq[1:]:
        if ch == curr:
            count += 1
        else:
            total += sg.dlugosc(count)
            curr = ch
            count = 1
    total += sg.dlugosc(count)
    return total


def compression_percent(seq):
    if not seq:
        return 100
    return round(100 * rle_len(seq) / len(seq))


def test_dlugosc_basic():
    assert sg.dlugosc(1) == 1
    assert sg.dlugosc(2) == 2   # "a2"
    assert sg.dlugosc(9) == 2   # "a9"
    assert sg.dlugosc(10) == 3  # "a10"


def test_rle_len_and_percent_examples():
    assert rle_len("") == 0
    assert rle_len("a") == 1
    assert rle_len("aa") == 2
    assert rle_len("aaa") == 2        # "a3"
    assert rle_len("aaabbbc") == 5    # "a3b3c"

    assert compression_percent("a") == 100
    assert compression_percent("aa") == 100
    assert compression_percent("aaa") == 67       # 2/3 -> 66.7 -> 67
    assert compression_percent("aaabbbc") == 71   # 5/7 -> 71.4 -> 71


def test_znaki_run_length_range(monkeypatch):
    # Wymuszamy dlugosc ciagu 3 i naprzemienne znaki A/B
    run = {"i": -1}

    def fake_choice(_alphabet):
        run["i"] += 1
        return "A" if run["i"] % 2 == 0 else "B"

    def fake_randint(a, b):
        assert a == 1 and b == 10, "Liczba powtorzen ma byc losowana z zakresu 1-10"
        return 3

    monkeypatch.setattr(sg.random, "choice", fake_choice)
    monkeypatch.setattr(sg.random, "randint", fake_randint)

    it = sg.znaki()
    out = [next(it) for _ in range(8)]  # 3xA, 3xB, 2xA
    assert out == list("AAABBBAA")


def test_main_jedna_linia_na_biezaco(monkeypatch, capsys):
    # Podstawiamy znany strumien "aaabbbc..." i skracamy animacje do 7 znakow
    monkeypatch.setattr(sg, "znaki", lambda: iter("aaabbbc" + "x" * 100))
    monkeypatch.setattr(sg, "MAXLEN", 7)
    monkeypatch.setattr(sg, "DELAY_SEC", 0)
    monkeypatch.setattr(sg.time, "sleep", lambda s: None)

    sg.main()
    out = capsys.readouterr().out

    assert "\r" in out, "Animacja ma nadpisywac linie znakiem \\r"
    assert out.count("\n") <= 1, "Cala animacja ma sie odbywac w jednej linii"

    klatki = [k for k in out.replace("\n", "").split("\r") if k.strip()]
    assert len(klatki) >= 7, "Po kazdym nowym znaku ma byc wydrukowana nowa klatka"

    ostatnia = klatki[-1].rstrip()
    assert ostatnia.startswith("aaabbbc")
    assert ostatnia.endswith("71%")

    # wspolczynnik liczony na biezaco po kazdym znaku: a, aa, aaa, ..., aaabbbc
    procenty = []
    for k in klatki[-7:]:
        m = re.search(r"(\d+)%\s*$", k)
        assert m, f"Brak wspolczynnika xx% na koncu klatki: {k!r}"
        procenty.append(int(m.group(1)))
    assert procenty == [100, 100, 67, 75, 80, 67, 71]
