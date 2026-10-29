"""
Zadanie 5 - czat w terminalu z lokalnym modelem jezykowym (Ollama).

Przygotowanie:
    ollama pull llama3.2:1b

Uruchomienie:
    python zadanie5.py              # model domyslny (MODEL)
    python zadanie5.py gemma3:1b    # inny model podany jako argument

W czacie: pusta linia konczy rozmowe, polecenie /reset czysci historie.
"""

import json
import sys

import requests

MODEL = "llama3.2:1b"
URL = "http://localhost:11434/api/chat"


def strumien(historia, model=MODEL):
    """
    Generator. Wysyla cala historie rozmowy do modelu i oddaje (yield)
    kolejne obiekty JSON (slowniki) przychodzace z serwera, linia po linii.
    - requests.post(URL, json=..., stream=True)
    - tresc zapytania: {"model": model, "messages": historia, "stream": True}
    - odpowiedz czytamy przez .iter_lines(), puste linie pomijamy,
      kazda linie zamieniamy na slownik: json.loads(linia)
    """
    pass


def predkosc(ostatni):
    """
    Zwraca predkosc generowania w tokenach na sekunde (float),
    na podstawie ostatniego obiektu strumienia (tego z "done": True):
        eval_count / eval_duration * 10**9   (eval_duration jest w nanosekundach)
    """
    pass


def odpowiedz(historia, model=MODEL):
    """
    Pobiera odpowiedz modelu przez strumien(historia, model):
    - kazdy fragment tekstu (pole ["message"]["content"]) wypisuje od razu:
      print(fragment, end="", flush=True),
    - po zakonczeniu wypisuje linie statystyk, np. "[tokeny: 50, 25.0 tok/s]",
    - zwraca pelny tekst odpowiedzi (sklejone fragmenty).
    """
    pass


def uruchom_czat(model=MODEL):
    """
    Petla czatu z pamiecia rozmowy:
    - wejscie uzytkownika: input("Ty: "),
    - pusta linia konczy czat,
    - "/reset" czysci historie (nie jest wysylane do modelu),
    - kazda inna wypowiedz trafia do historii jako {"role": "user", ...},
      a odpowiedz modelu jako {"role": "assistant", ...}.
    """
    historia = []
    pass


if __name__ == "__main__":
    model = sys.argv[1] if len(sys.argv) > 1 else MODEL
    try:
        uruchom_czat(model)
    except requests.ConnectionError:
        print("\nBrak połączenia z Ollamą. Czy program Ollama jest uruchomiony?")
