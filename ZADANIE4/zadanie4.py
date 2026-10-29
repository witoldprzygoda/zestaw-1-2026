"""
Zadanie 4 - biezace temperatury ze stacji synoptycznych IMGW.

Uruchomienie:
    python zadanie4.py            # dane pobierane z serwisu IMGW
    python zadanie4.py --offline  # dane z pliku synop_przyklad.json (bez sieci)
"""

import json
import sys
from pathlib import Path

import requests

URL = "https://danepubliczne.imgw.pl/api/data/synop"
PLIK_PRZYKLADOWY = Path(__file__).parent / "synop_przyklad.json"
SZEROKOSC = 40        # dlugosc najdluzszego paska wykresu (w znakach)


def wczytaj_z_pliku(sciezka=PLIK_PRZYKLADOWY):
    """Wczytuje zapisana odpowiedz serwisu IMGW z pliku JSON (gotowe)."""
    with open(sciezka, encoding="utf-8") as plik:
        return json.load(plik)


def pobierz_dane():
    """
    Pobiera dane ze wszystkich stacji synoptycznych IMGW i zwraca je
    jako liste slownikow (po jednym slowniku na stacje).
    - requests.get(URL, timeout=10)
    - sprawdzenie odpowiedzi: raise_for_status()
    - zamiana odpowiedzi na struktury Pythona: .json()
    """
    pass


def temperatury(dane):
    """
    Z listy slownikow IMGW buduje liste krotek (stacja, temperatura_float),
    pomijajac stacje bez pomiaru temperatury (wartosc None).
    Lista ma byc posortowana rosnaco wedlug temperatury.
    """
    pass


def dlugosc_paska(t, tmin, tmax, szerokosc=SZEROKOSC):
    """
    Dlugosc paska wykresu dla temperatury t:
        1 + round((t - tmin) / (tmax - tmin) * (szerokosc - 1))
    Najzimniejsza stacja dostaje 1 znak, najcieplejsza 'szerokosc' znakow.
    Gdy tmax == tmin (wszystkie temperatury rowne), zwracamy 'szerokosc'.
    """
    pass


def main():
    if "--offline" in sys.argv[1:]:
        dane = wczytaj_z_pliku()
    else:
        dane = pobierz_dane()

    # TODO:
    # 1. naglowek z data i godzina pomiaru (pola "data_pomiaru", "godzina_pomiaru"),
    # 2. lista temperatur (funkcja temperatury) i wykres: jedna linia na stacje,
    #    nazwa stacji, temperatura i pasek ze znakow '█' (funkcja dlugosc_paska),
    # 3. podsumowanie: najzimniej, najcieplej, srednia temperatura.


if __name__ == "__main__":
    main()
