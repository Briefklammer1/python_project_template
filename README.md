# Python Project Template

Dies ist ein Python-Projekttemplate mit einer sauberen und modernen Ordnerstruktur.

## Projektstruktur

```
python_project_template/
│
├── src/                    # Quellcode des Projekts
│   └── __init__.py
│
├── tests/                  # Testkodeverzeichnis
│   └── __init__.py
│
├── docs/                   # Dokumentation
│
├── requirements.txt        # Projektabhängigkeiten
│
└── README.md              # Projektdokumentation
```

## Installation

1. Erstelle eine virtuelle Umgebung:
```bash
python -m venv venv
```

2. Aktiviere die virtuelle Umgebung:
- Windows: `venv\Scripts\activate`
- Unix/MacOS: `source venv/bin/activate`

3. Installiere die Abhängigkeiten:
```bash
pip install -r requirements.txt
```

## Entwicklung

- Platziere deinen Hauptquellcode im `src`-Verzeichnis
- Schreibe Tests im `tests`-Verzeichnis
- Dokumentiere dein Projekt in `docs`
- Halte die `requirements.txt` aktuell

## Lizenz

MIT
