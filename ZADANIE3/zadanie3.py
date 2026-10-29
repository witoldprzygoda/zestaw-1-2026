"""
Zadanie 3 - duzy zegar HH:MM:SS w terminalu oraz tryb minutnika.

Uruchomienie:
    python zadanie3.py        # zegar (biezacy czas), konczymy Ctrl+C
    python zadanie3.py 25     # minutnik: odliczanie 25 minut do 00:00:00

Matryce cyfr i dwukropka zbudowane sa ze znakow '█' i spacji
(8 wierszy; cyfra ma 8 kolumn, dwukropek 4 kolumny).
"""

import math
import os
import sys
import time
from datetime import datetime, timedelta

# Ustawienia
FPS = 4               # klatki na sekunde
DIGIT_H = 8           # wysokosc znaku (wiersze)
PRZERWA = 2           # odstep miedzy znakami (kolumny)

# Wzorce cyfr (kazdy wiersz ma szerokosc 8 znakow)
DIGITS = {
    '0': [
        "████████",
        "██    ██",
        "██    ██",
        "██    ██",
        "██    ██",
        "██    ██",
        "██    ██",
        "████████",
    ],
    '1': [
        "    ███ ",
        "   ████ ",
        "    ███ ",
        "    ███ ",
        "    ███ ",
        "    ███ ",
        "    ███ ",
        "  ██████",
    ],
    '2': [
        "████████",
        "      ██",
        "      ██",
        "████████",
        "██      ",
        "██      ",
        "██      ",
        "████████",
    ],
    '3': [
        "████████",
        "      ██",
        "      ██",
        "████████",
        "      ██",
        "      ██",
        "      ██",
        "████████",
    ],
    '4': [
        "██    ██",
        "██    ██",
        "██    ██",
        "████████",
        "      ██",
        "      ██",
        "      ██",
        "      ██",
    ],
    '5': [
        "████████",
        "██      ",
        "██      ",
        "████████",
        "      ██",
        "      ██",
        "      ██",
        "████████",
    ],
    '6': [
        "████████",
        "██      ",
        "██      ",
        "████████",
        "██    ██",
        "██    ██",
        "██    ██",
        "████████",
    ],
    '7': [
        "████████",
        "      ██",
        "     ██ ",
        "    ██  ",
        "   ██   ",
        "  ██    ",
        "  ██    ",
        "  ██    ",
    ],
    '8': [
        "████████",
        "██    ██",
        "██    ██",
        "████████",
        "██    ██",
        "██    ██",
        "██    ██",
        "████████",
    ],
    '9': [
        "████████",
        "██    ██",
        "██    ██",
        "████████",
        "      ██",
        "      ██",
        "      ██",
        "████████",
    ],
}

# Dwukropek (kazdy wiersz ma szerokosc 4 znakow)
COLON = [
    "    ",
    " ██ ",
    " ██ ",
    "    ",
    "    ",
    " ██ ",
    " ██ ",
    "    ",
]


def czyszczenie():
    """
    Czysci ekran terminala poleceniem systemowym:
    os.name == 'nt' -> os.system('cls'), w przeciwnym razie os.system('clear').
    """
    pass


def klatka(napis):
    """
    Zwraca wieloliniowy napis (DIGIT_H wierszy rozdzielonych znakiem "\\n")
    przedstawiajacy napis zlozony z cyfr i dwukropkow, np. "12:34:56".

    Wiersz i wyniku to sklejone i-te wiersze wzorcow kolejnych znakow
    (DIGITS dla cyfr, COLON dla ':'), rozdzielone PRZERWA spacjami.
    """
    return ""  # tymczasowo pusto


def format_czasu(sekundy):
    """
    Zamienia liczbe sekund na napis "HH:MM:SS", np. 3725 -> "01:02:05".
    Wskazowka: divmod().
    """
    pass


def zegar():
    """
    Petla zegara: co 1/FPS sekundy czysci ekran i rysuje biezacy czas.
    """
    pass


def minutnik(minuty):
    """
    Petla minutnika: odlicza zadana liczbe minut do 00:00:00.
    Po dojsciu do zera rysuje 00:00:00, wypisuje "Koniec!" i konczy dzialanie.
    """
    pass


def main():
    argv = sys.argv[1:]
    # TODO: bez argumentow -> zegar(), z jednym argumentem (liczba minut) -> minutnik(...)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:  # Ctrl+C konczy program bez komunikatu o bledzie
        print()
