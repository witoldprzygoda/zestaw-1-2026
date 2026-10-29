# Zestaw 1 - Język Python

Pięć zadań laboratoryjnych. Pełna treść zadań znajduje się w dokumencie PDF zestawu.

## Zawartość repozytorium

| Katalog    | Plik do uzupełnienia | Testy                             |
|------------|----------------------|-----------------------------------|
| `ZADANIE1` | `zadanie1.py`        | `tests/test_zadanie1.py`          |
| `ZADANIE2` | `zadanie2.py`        | `tests/test_zadanie2.py`          |
| `ZADANIE3` | `zadanie3.py`        | `tests/test_zadanie3.py`          |
| `ZADANIE4` | `zadanie4.py`        | `tests/test_zadanie4.py`          |
| `ZADANIE5` | `zadanie5.py`        | `tests/test_zadanie5.py`          |

Plik `ZADANIE4/synop_przyklad.json` to zapisana odpowiedź serwisu IMGW (dane do pracy bez sieci).

## Przygotowanie

```
python -m pip install -r requirements.txt
```

## Uruchamianie testów

```
python -m pytest            # wszystkie zadania
python -m pytest ZADANIE1   # jedno zadanie
python -m pytest -v         # z listą poszczególnych testów
```

Nie zmieniaj plików z testami ani nazw funkcji w kodzie początkowym.
