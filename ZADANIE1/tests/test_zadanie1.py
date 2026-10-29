import sys
import time

import ZADANIE1.zadanie1 as Z


# --- funkcja czynniki(n) -------------------------------------------------

def test_czynniki_liczba_pierwsza():
    assert Z.czynniki(13) == {13: 1}


def test_czynniki_potega():
    assert Z.czynniki(2**10) == {2: 10}


def test_czynniki_mieszane():
    assert Z.czynniki(360) == {2: 3, 3: 2, 5: 1}


def test_czynniki_jedynka():
    assert Z.czynniki(1) == {}


def test_czynniki_duza_liczba():
    assert Z.czynniki(13041599400) == {2: 3, 3: 4, 5: 2, 805037: 1}


# --- funkcja rozklad_na_czynniki(n) --------------------------------------

def test_rozklad_liczba_pierwsza():
    assert Z.rozklad_na_czynniki(13) == "13"


def test_rozklad_iloczyn_pierwszych():
    assert Z.rozklad_na_czynniki(3 * 17) == "3*17"


def test_rozklad_duza_pierwsza():
    assert Z.rozklad_na_czynniki(805037) == "805037"


def test_rozklad_potega_dwojki():
    assert Z.rozklad_na_czynniki(2**10) == "2^10"


def test_rozklad_mieszany():
    assert Z.rozklad_na_czynniki((2**3) * (3**4) * (5**2)) == "2^3*3^4*5^2"


def test_rozklad_jedynka():
    assert Z.rozklad_na_czynniki(1) == "1"


def test_rozklad_duza_zlozona():
    assert Z.rozklad_na_czynniki(13041599400) == "2^3*3^4*5^2*805037"


def test_rozklad_szybkosc():
    # 100000007 jest liczba pierwsza; sprawdzanie dzielnikow do pierwiastka
    # konczy sie w ulamku sekundy, sprawdzanie az do n trwa kilka sekund
    start = time.perf_counter()
    wynik = Z.rozklad_na_czynniki(100000007)
    czas = time.perf_counter() - start
    assert wynik == "100000007"
    assert czas < 1.0, f"Obliczenie trwalo {czas:.1f} s (limit 1 s)"


# --- program glowny main() -------------------------------------------------

def test_main_wydruk(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["zadanie1.py", "4407", "13041599400"])
    Z.main()
    linie = capsys.readouterr().out.splitlines()
    assert "4407 = 3*13*113" in linie
    assert "13041599400 = 2^3*3^4*5^2*805037" in linie


def test_main_bledne_argumenty(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["zadanie1.py", "abc", "0", "12"])
    Z.main()  # nie moze zakonczyc sie wyjatkiem
    linie = capsys.readouterr().out.splitlines()
    assert "12 = 2^2*3" in linie
    assert any("abc" in linia for linia in linie), "Brak komunikatu dla argumentu abc"
    assert not any(linia.startswith("0 =") for linia in linie), "Liczba 0 nie ma rozkladu"
