import sys

import pytest

import ZADANIE4.zadanie4 as Z

# Maly, kontrolowany zestaw danych w formacie IMGW (wartosci jako napisy, brak pomiaru = None)
DANE_TESTOWE = [
    {"stacja": "Kraków", "data_pomiaru": "2026-10-29", "godzina_pomiaru": "12", "temperatura": "7.3"},
    {"stacja": "Hel", "data_pomiaru": "2026-10-29", "godzina_pomiaru": "12", "temperatura": "10"},
    {"stacja": "Śnieżka", "data_pomiaru": "2026-10-29", "godzina_pomiaru": "12", "temperatura": "-2.5"},
    {"stacja": "Bez pomiaru", "data_pomiaru": "2026-10-29", "godzina_pomiaru": "12", "temperatura": None},
    {"stacja": "Łódź", "data_pomiaru": "2026-10-29", "godzina_pomiaru": "12", "temperatura": "7.3"},
]


class FakeResponse:
    def __init__(self, dane):
        self._dane = dane
        self.status_code = 200

    def json(self):
        return self._dane

    def raise_for_status(self):
        pass


# --- pobierz_dane() ---------------------------------------------------------

def test_pobierz_dane_bez_sieci(monkeypatch):
    wywolania = []

    def fake_get(url, *args, **kwargs):
        wywolania.append((url, kwargs))
        return FakeResponse(DANE_TESTOWE)

    monkeypatch.setattr(Z.requests, "get", fake_get)

    dane = Z.pobierz_dane()
    assert dane == DANE_TESTOWE
    assert len(wywolania) == 1, "Wszystkie stacje pobieramy jednym zapytaniem"
    url, kwargs = wywolania[0]
    assert url == Z.URL
    assert kwargs.get("timeout") is not None, "Zapytanie ma miec ustawiony timeout"


# --- temperatury(dane) --------------------------------------------------------

def test_temperatury_typy_i_pomijanie_none():
    wynik = Z.temperatury(DANE_TESTOWE)
    assert isinstance(wynik, list)
    assert len(wynik) == 4, "Stacja bez pomiaru (None) ma byc pominieta"
    for stacja, t in wynik:
        assert isinstance(stacja, str)
        assert isinstance(t, float)


def test_temperatury_sortowanie_rosnace():
    wynik = Z.temperatury(DANE_TESTOWE)
    assert wynik[0] == ("Śnieżka", -2.5)
    assert wynik[-1] == ("Hel", 10.0)
    assert [t for _, t in wynik] == sorted(t for _, t in wynik)


def test_temperatury_plik_przykladowy():
    dane = Z.wczytaj_z_pliku()
    wynik = Z.temperatury(dane)
    assert len(wynik) == 62
    assert wynik[0] == ("Kasprowy Wierch", 1.1)
    assert wynik[-1] == ("Platforma", 12.0)


# --- dlugosc_paska(t, tmin, tmax, szerokosc) -----------------------------------

def test_dlugosc_paska_skrajne():
    assert Z.dlugosc_paska(-5.0, -5.0, 15.0, 40) == 1
    assert Z.dlugosc_paska(15.0, -5.0, 15.0, 40) == 40


def test_dlugosc_paska_srodek():
    assert Z.dlugosc_paska(10.0, 0.0, 39.0, 40) == 11
    assert Z.dlugosc_paska(4.0, 2.0, 6.0, 21) == 11


def test_dlugosc_paska_rowne_temperatury():
    assert Z.dlugosc_paska(3.0, 3.0, 3.0, 40) == 40


def test_dlugosc_paska_domyslna_szerokosc():
    assert Z.dlugosc_paska(8.0, 1.0, 8.0) == Z.SZEROKOSC


# --- program glowny w trybie --offline -----------------------------------------

def test_main_offline(monkeypatch, capsys):
    def brak_sieci(*args, **kwargs):
        pytest.fail("W trybie --offline program nie moze korzystac z sieci")

    monkeypatch.setattr(Z.requests, "get", brak_sieci)
    monkeypatch.setattr(sys, "argv", ["zadanie4.py", "--offline"])

    Z.main()
    out = capsys.readouterr().out
    linie = out.splitlines()

    assert sum("█" in linia for linia in linie) == 62, "Wykres: jedna linia z paskiem na stacje"
    assert "Najzimniej" in out and "Kasprowy Wierch" in out
    assert "Najcieplej" in out and "Platforma" in out
    assert "Średnia" in out
    assert "2026-10-29" in out
