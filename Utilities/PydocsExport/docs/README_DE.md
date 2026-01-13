# PydocsExport - Vollständige Dokumentation

## Inhaltsverzeichnis

1. [Einführung](#einführung)
2. [Installation](#installation)
3. [Verwendung](#verwendung)
4. [Architektur](#architektur)
5. [Ausgabeformat](#ausgabeformat)
6. [API-Referenz](#api-referenz)
7. [Beispiele](#beispiele)
8. [Fehlerbehebung](#fehlerbehebung)
9. [Beitragen](#beitragen)

---

## Einführung

### Was ist PydocsExport?

**PydocsExport** ist ein leistungsstarkes Python-Modul, das die vollständige Python-Dokumentation auf Ihrem System in mehrere E-Book-Formate und Textformate exportiert.

### Hauptmerkmale

- ✅ Export in **5 verschiedene Formate**: TXT, PDF, EPUB, MOBI, HTML
- ✅ Unterstützung für **11 Papierformate** für PDFs (A0 bis A10)
- ✅ **Organisierte Struktur** mit Kapiteln und Index
- ✅ **Mehrsprachige Unterstützung** in Dokumentation und Schnittstelle
- ✅ **Detailliertes Exportprotokoll** in JSON
- ✅ **Einfache und intuitive API** zur einfachen Integration
- ✅ **CLI-Schnittstelle** (EasyPydocsExport.py) für Benutzer

### Anwendungsfälle

- Erstellen Sie eine vollständige Offline-Python-Dokumentation
- Generieren Sie E-Books für E-Reader-Geräte
- Erstellen Sie druckbare PDFs in verschiedenen Formaten
- Archivieren Sie die Dokumentation für zukünftige Referenzen
- Erstellen Sie Bildungsressourcen

---

## Installation

### Anforderungen

- Python 3.6 oder höher
- Keine externen Abhängigkeiten erforderlich (verwendet integriertes pydoc)

### Installationsschritte

1. **Klonen oder herunterladen** Sie das Projektverzeichnis:
```bash
git clone <repository_url>
cd PydocsExport
```

2. **Überprüfen Sie die Struktur**:
```bash
ls
# Sollte anzeigen: src/, tests/, docs/, EasyPydocsExport.py
```

3. **Testen Sie die Installation**:
```bash
python EasyPydocsExport.py --help
```

### Projektstruktur

```
PydocsExport/
├── src/                          # Hauptmodul
│   ├── __init__.py               # Paketinitialisierung
│   ├── exporter.py               # Hauptexportklasse
│   ├── formatter.py              # Formatierer für verschiedene Formate
│   └── index_manager.py          # Indexverwaltung
├── tests/                        # Unittests
│   └── test_pydocs_export.py    # Vollständige Test-Suite
├── docs/                         # Dokumentation
│   ├── README.md                 # Diese Datei (Deutsch)
│   ├── README_EN.md              # Englische Dokumentation
│   ├── README_FR.md              # Französische Dokumentation
│   ├── README_ES.md              # Spanische Dokumentation
│   ├── README_DE.md              # Deutsche Dokumentation
│   └── README_IT.md              # Italienische Dokumentation
├── output/                       # Ausgabeverzeichnis (wird zur Laufzeit erstellt)
├── EasyPydocsExport.py          # Hauptskript für Benutzer
└── README.md                     # Ausgangsdatei
```

---

## Verwendung

### Grundlegende Verwendung

#### Über CLI-Skript (empfohlen)

```bash
# Export aller Formate
python EasyPydocsExport.py

# Nur TXT und HTML exportieren
python EasyPydocsExport.py --txt --html

# Nur in PDF exportieren
python EasyPydocsExport.py --pdf

# Benutzerdefinierten Ausgabeverzeichnis angeben
python EasyPydocsExport.py --output /mein/benutzerdefinierter/pfad

# Hilfe anzeigen
python EasyPydocsExport.py --help
```

#### Über Python-Modul

```python
from src.exporter import PydocsExporter

# Erstellen Sie einen Exporter
exporter = PydocsExporter(output_base_dir="meine_dokumentation")

# Alle Formate exportieren
ergebnisse = exporter.export_all()

# Spezifische Formate exportieren
ergebnisse = exporter.export_all(formats=['txt', 'epub', 'html'])

# Ergebnisse anzeigen
print(ergebnisse)
```

### Verfügbare Optionen

| Option | Beschreibung | Beispiel |
|--------|-------------|----------|
| `--all` | Alle Formate exportieren | `--all` |
| `--txt` | Nur Text-Format | `--txt` |
| `--pdf` | PDF-Format (alle Größen) | `--pdf` |
| `--epub` | E-Book-Format | `--epub` |
| `--mobi` | Kindle/MOBI-Format | `--mobi` |
| `--html` | Interaktive HTML-Seiten | `--html` |
| `--output [dir]` | Ausgabeverzeichnis | `--output /pfad` |
| `--help` | Hilfe anzeigen | `--help` |

---

## Architektur

### Hauptkomponenten

#### 1. PydocsExporter (exporter.py)

**Verantwortungen:**
- Orchestrierung des Exportvorgangs
- Abruf der pydocs-Dokumentation
- Verwaltung von Papierformaten für PDF
- Erstellung von Verzeichnisstrukturen

**Unterstützte Papierformate:**
```
A0:  2384 × 3370 Punkte
A1:  1684 × 2384 Punkte
A2:  1191 × 1684 Punkte
A3:   842 × 1191 Punkte
A4:   595 ×  842 Punkte (Standard)
A5:   420 ×  595 Punkte
A6:   298 ×  420 Punkte
A7:   210 ×  298 Punkte
A8:   148 ×  210 Punkte
A9:   105 ×  148 Punkte
A10:  73  ×  105 Punkte
```

#### 2. Formatierer (formatter.py)

Stellt Formatierungsklassen bereit:

- **TextFormatter**: Einfache Formatierung für TXT
- **PDFFormatter**: Anpassung an verschiedene Papierformate
- **EbookFormatter**: Struktur für EPUB/MOBI

#### 3. Indexverwaltung (index_manager.py)

Verwaltet Dokumentationsindizes:

- Erstellung von Indizes in TXT, JSON, HTML
- Gruppierung nach Kategorien
- Generierung von Inhaltsverzeichnis

---

## Ausgabeformat

### Verzeichnisstruktur

```
pydocs_export_output/
│
├── TXT/
│   ├── Chapters/
│   │   ├── 001_sys.txt
│   │   ├── 002_os.txt
│   │   └── ...
│   └── index.txt
│
├── PDF/
│   ├── A0/
│   ├── A1/
│   ├── A3/
│   ├── A4/
│   └── ... (andere Papierformate)
│
├── EBOOK_EPUB/
│
├── EBOOK_MOBI/
│
└── HTML/
```

---

## Beispiele

### Beispiel 1: Einfacher Export

```bash
python EasyPydocsExport.py
```

Dies exportiert alle Dokumentationen in allen verfügbaren Formaten
in das Standardverzeichnis `pydocs_export_output/`.

### Beispiel 2: Spezifischer Export

```bash
python EasyPydocsExport.py --txt --html --output /mein/ordner
```

Exportiert nur TXT und HTML in `/mein/ordner/`.

---

## Fehlerbehebung

### Problem: "Modul PydocsExporter kann nicht importiert werden"

**Lösung:**
1. Überprüfen Sie, ob Sie im korrekten Verzeichnis sind
2. Überprüfen Sie, ob das Verzeichnis `src/` existiert
3. Überprüfen Sie, ob `__init__.py` in `src/` ist

```bash
ls -la src/
# Sollte __init__.py anzeigen
```

### Problem: Berechtigung verweigert beim Erstellen von Dateien

**Lösung:**
1. Überprüfen Sie die Berechtigungen des Ausgabeverzeichnisses
2. Verwenden Sie ein anderes Verzeichnis mit `--output`

```bash
mkdir -p ~/meine_dokumentation
python EasyPydocsExport.py --output ~/meine_dokumentation
```

---

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Datei `LICENSE`.

---

**Zuletzt aktualisiert:** Januar 2024
**Version:** 1.0.0

---

**Vielen Dank, dass Sie PydocsExport verwenden! 🎉**
