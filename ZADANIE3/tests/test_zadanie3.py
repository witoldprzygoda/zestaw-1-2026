import ZADANIE3.zadanie3 as Z


def wzorzec(znak):
    return Z.COLON if znak == ":" else Z.DIGITS[znak]


def oczekiwana_klatka(napis):
    # Wiersz i = i-te wiersze wzorcow kolejnych znakow, rozdzielone PRZERWA spacjami
    odstep = " " * Z.PRZERWA
    return [odstep.join(wzorzec(z)[i] for z in napis) for i in range(Z.DIGIT_H)]


def wiersze(wynik):
    # Porownujemy wiersze bez koncowych spacji i bez koncowego znaku nowej linii
    assert isinstance(wynik, str), "klatka() ma zwracac napis (str)"
    return [w.rstrip() for w in wynik.rstrip("\n").split("\n")]


def test_klatka_jedna_cyfra():
    assert wiersze(Z.klatka("0")) == [w.rstrip() for w in Z.DIGITS["0"]]


def test_klatka_dwukropek():
    assert wiersze(Z.klatka(":")) == [w.rstrip() for w in Z.COLON]


def test_klatka_dwie_cyfry_z_przerwa():
    assert wiersze(Z.klatka("47")) == [w.rstrip() for w in oczekiwana_klatka("47")]


def test_klatka_pelny_czas():
    wynik = Z.klatka("12:34:56")
    assert wiersze(wynik) == [w.rstrip() for w in oczekiwana_klatka("12:34:56")]
    assert len(wiersze(wynik)) == Z.DIGIT_H


def test_klatka_wszystkie_cyfry():
    for c in "0123456789":
        assert wiersze(Z.klatka(c + c)) == [w.rstrip() for w in oczekiwana_klatka(c + c)]


def test_format_czasu():
    assert Z.format_czasu(0) == "00:00:00"
    assert Z.format_czasu(59) == "00:00:59"
    assert Z.format_czasu(60) == "00:01:00"
    assert Z.format_czasu(3725) == "01:02:05"
    assert Z.format_czasu(25 * 60) == "00:25:00"
    assert Z.format_czasu(23 * 3600 + 59 * 60 + 59) == "23:59:59"
