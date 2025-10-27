
focus_tracker:
Flow Tracker - zarys projektu

Cel:
    Aplikacja do planowania i reflesji, ma ona pomóc w :
        zaplanowaniu dnia / tygodnia w prosty sposób
        sledziź ile czasu faktycznie spędziło sie na danych zadaniach
        zapisywać refleksje, pomysły i priorytety względem zadań
        uczyć sie lepiej zarzadzać czasem

Głowna idea:
    Plan:
        - rano planujesz dzień lub tydzień (priorytety, bloki czasu).
    Realizacja:
        - uruchamiasz sesje (start/stop, notatki).
    Refleksja:
        - na koniec dnia robisz szybki przegląd (co poszło, co nie, wnioski).
    Adaptacja:
        - system pomaga przenieść / przeorganizować zadania

Ogólna architektura:
    src/
    ├── flow_tracker/        ← logika główna, CLI, główny “entry point”
    │   ├── cli.py           
        - Punkt wejścia aplikacji
        - Centurm dowodzenia
    │   ├── planner.py       
        - tworzenie planu dnia /tygodnia
        - wybieranie priorytetów, kategorii, czasu
        - automatyczne przenoszenie niedokończonych rzeczy z przeszłości
    │   ├── sessions.py      # sesje focusu (start, stop, statystyki)
    │   ├── reflection.py    # przegląd dnia / tygodnia, notatki
    │   └── habits.py        # (opcjonalnie później) śledzenie nawyków
    │
    ├── models/              ← struktury danych, Pydantic
    │   ├── task.py          # definicja zadania
    │   ├── session.py       # definicja sesji focusu
    │   ├── reflection.py    # zapis przeglądu / notatek
    │   └── config.py        # ustawienia aplikacji
    │
    ├── services/            ← logika pomocnicza / backend
    │   ├── storage.py       # zapis/odczyt JSON/SQLite
    │   ├── calendar.py      # eksport do kalendarza (ICS)
    │   └── analyzer.py      # podsumowania, statystyki, raporty
    │
    ├── common/              ← rzeczy wspólne
    │   ├── logger.py        # Twój logger
    │   ├── json_utils.py    # helpery do plików JSON
    │   └── time_utils.py    # (opcjonalnie) pomocne funkcje czasu
    │
    ├── static/              ← dane przykładowe, configi, ikony
    │   ├── dummy_data.json
    │   └── templates/       # np. szablon eksportu tygodnia (Markdown)
    │
    └── tests/               ← testy jednostkowe
        ├── test_models.py
        ├── test_planner.py
        ├── test_storage.py
        └── conftest.py