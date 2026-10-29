"""
Zadanie 1 - rozklad liczb naturalnych na czynniki pierwsze.

Uruchomienie:
    python zadanie1.py 4407 13041599400

Oczekiwany wydruk:
    4407 = 3*13*113
    13041599400 = 2^3*3^4*5^2*805037
"""

import sys


def czynniki(n):
    """
    Zwraca slownik {czynnik_pierwszy: wykladnik} dla liczby naturalnej n >= 1.

    Przyklady:
        czynniki(360) -> {2: 3, 3: 2, 5: 1}
        czynniki(13)  -> {13: 1}
        czynniki(1)   -> {}          (liczba 1 nie ma czynnikow pierwszych)

    Wskazowka: dzielniki d sprawdzamy tylko dopoki d * d <= n;
    jesli po petli zostalo n > 1, to n jest ostatnim czynnikiem pierwszym.
    """
    pass


def rozklad_na_czynniki(n):
    """
    Zwraca rozklad liczby n jako napis, np. "2^3*3^4*5^2*805037".

    - czynniki w kolejnosci rosnacej, rozdzielone znakiem *,
    - wykladnik 1 pomijamy ("3*17", a nie "3^1*17^1"),
    - dla n == 1 zwracamy "1".

    Skorzystaj z funkcji czynniki(n).
    """
    pass


def main():
    argv = sys.argv[1:]  # argumenty programu bez nazwy pliku

    for arg in argv:
        # TODO: pomin (z komunikatem) argumenty, ktore nie sa liczbami naturalnymi >= 1
        liczba = int(arg)
        wynik = rozklad_na_czynniki(liczba)
        print(f"{liczba} = {wynik}")


if __name__ == "__main__":
    main()
