"""
Zadanie 2 - strumien znakow i wspolczynnik kompresji RLE liczony na biezaco.

Zalozenia:
- alfabet: A-Z, a-z,
- kazdy znak powtarza sie losowo 1-10 razy, potem losowany jest kolejny,
- generowanie konczy sie po MAXLEN znakach,
- wydruk to JEDNA linia odswiezana w miejscu: ostatnie WIDTH znakow
  oraz na koncu wspolczynnik kompresji w formacie "  xx%".

Animacja w jednej linii: print(..., end="\\r", flush=True),
dopelnienie okna spacjami: "".join(buf).ljust(WIDTH),
staly sufiks: f"  {procent:3d}%".
"""

import random
import string
import time
from collections import deque

WIDTH = 80            # szerokosc okna podgladu
MAXLEN = 1000         # liczba generowanych znakow
DELAY_SEC = 0.02      # opoznienie miedzy kolejnymi znakami (plynnosc animacji)

ALPHABET = string.ascii_letters  # A-Z, a-z


def znaki():
    """
    Generator znakow (dziala w nieskonczonosc, while True):
      - losuje znak z ALPHABET:            random.choice(ALPHABET)
      - losuje liczbe powtorzen 1..10:     random.randint(1, 10)
      - oddaje (yield) wylosowany znak tyle razy.
    """
    pass


def dlugosc(count):
    """
    Zwraca dlugosc zapisu RLE jednego ciagu jednakowych znakow o dlugosci count:
      - count == 1  -> 1                  ("a")
      - count >= 2  -> 1 + len(str(count)) ("a3" -> 2, "a10" -> 3)
    """
    pass


def main():
    """
    Animacja strumienia znakow i wspolczynnika kompresji w jednej linii.
    """
    buf = deque(maxlen=WIDTH)

    # Szkic petli glownej:
    # for ch in znaki():
    #     ... dopisz znak do buf, zaktualizuj liczniki ...
    #     ... policz procent kompresji dla wszystkich dotychczasowych znakow ...
    #     print(..., end="\r", flush=True)
    #     time.sleep(DELAY_SEC)
    #     if total_raw >= MAXLEN:
    #         break

    print()  # po zakonczeniu animacji przejscie do nowej linii


if __name__ == "__main__":
    main()
