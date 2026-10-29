import copy
import json

import pytest

import ZADANIE5.zadanie5 as mod

# Odpowiedz serwera Ollama w trybie strumieniowym: kazda linia to osobny obiekt JSON
FRAGMENTY = ["Witaj", "! To ", "odpowiedź", " testowa."]
PELNY_TEKST = "".join(FRAGMENTY)
LINIE = [
    json.dumps({"model": "test", "message": {"role": "assistant", "content": f}, "done": False})
    for f in FRAGMENTY
] + [
    json.dumps({
        "model": "test",
        "message": {"role": "assistant", "content": ""},
        "done": True,
        "eval_count": 50,
        "eval_duration": 2_000_000_000,
    })
]


class FakeResponse:
    def __init__(self, linie):
        self._linie = linie
        self.status_code = 200

    def iter_lines(self, *args, **kwargs):
        for linia in self._linie:
            yield linia if kwargs.get("decode_unicode") else linia.encode("utf-8")

    def raise_for_status(self):
        pass

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


@pytest.fixture
def serwer(monkeypatch):
    """Podstawia requests.post i zapisuje kopie kazdego wyslanego zapytania."""
    zapytania = []

    def fake_post(url, *args, **kwargs):
        tresc = kwargs.get("json")
        if tresc is None and "data" in kwargs:
            tresc = json.loads(kwargs["data"])
        zapytania.append({"url": url, "tresc": copy.deepcopy(tresc), "kwargs": kwargs})
        return FakeResponse(LINIE)

    monkeypatch.setattr(mod.requests, "post", fake_post)
    return zapytania


def podstaw_wejscie(monkeypatch, wpisy):
    wejscia = iter(wpisy)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(wejscia))


# --- strumien() ----------------------------------------------------------------

def test_strumien_oddaje_obiekty_json(serwer):
    historia = [{"role": "user", "content": "Cześć"}]
    obiekty = list(mod.strumien(historia))
    assert obiekty == [json.loads(linia) for linia in LINIE]


def test_strumien_tresc_zapytania(serwer):
    historia = [{"role": "user", "content": "Cześć"}]
    list(mod.strumien(historia, "gemma3:1b"))
    assert len(serwer) == 1
    z = serwer[0]
    assert z["url"] == mod.URL
    assert z["tresc"]["model"] == "gemma3:1b"
    assert z["tresc"]["messages"] == historia
    assert z["tresc"].get("stream", True) is True
    assert z["kwargs"].get("stream") is True, "requests.post(..., stream=True) - odbior na biezaco"


# --- predkosc() ------------------------------------------------------------------

def test_predkosc():
    assert mod.predkosc({"eval_count": 50, "eval_duration": 2_000_000_000}) == pytest.approx(25.0)
    assert mod.predkosc({"eval_count": 282, "eval_duration": 4_535_599_000}) == pytest.approx(62.175, abs=0.01)


# --- odpowiedz() -------------------------------------------------------------------

def test_odpowiedz_wypisuje_i_zwraca(serwer, capsys):
    tekst = mod.odpowiedz([{"role": "user", "content": "Cześć"}])
    out = capsys.readouterr().out
    assert tekst == PELNY_TEKST
    assert PELNY_TEKST in out
    assert "25.0 tok/s" in out
    assert "50" in out


# --- uruchom_czat() ------------------------------------------------------------------

def test_czat_pusta_linia_konczy(serwer, monkeypatch):
    podstaw_wejscie(monkeypatch, [""])
    mod.uruchom_czat()
    assert serwer == []


def test_czat_pamieta_rozmowe(serwer, monkeypatch, capsys):
    podstaw_wejscie(monkeypatch, ["Cześć", "Jak się masz?", ""])
    mod.uruchom_czat()
    assert len(serwer) == 2
    assert serwer[0]["tresc"]["messages"] == [
        {"role": "user", "content": "Cześć"},
    ]
    assert serwer[1]["tresc"]["messages"] == [
        {"role": "user", "content": "Cześć"},
        {"role": "assistant", "content": PELNY_TEKST},
        {"role": "user", "content": "Jak się masz?"},
    ]
    assert PELNY_TEKST in capsys.readouterr().out


def test_czat_reset(serwer, monkeypatch):
    podstaw_wejscie(monkeypatch, ["Raz", "/reset", "Dwa", ""])
    mod.uruchom_czat()
    assert len(serwer) == 2, "Polecenie /reset nie jest wysylane do modelu"
    assert serwer[1]["tresc"]["messages"] == [{"role": "user", "content": "Dwa"}]


def test_czat_model_z_argumentu(serwer, monkeypatch):
    podstaw_wejscie(monkeypatch, ["Cześć", ""])
    mod.uruchom_czat("gemma3:1b")
    assert serwer[0]["tresc"]["model"] == "gemma3:1b"
