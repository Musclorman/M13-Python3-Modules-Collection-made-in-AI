# PydocsExport - Documentazione Completa

## Indice dei Contenuti

1. [Introduzione](#introduzione)
2. [Installazione](#installazione)
3. [Utilizzo](#utilizzo)
4. [Architettura](#architettura)
5. [Formato di Output](#formato-di-output)
6. [Riferimento API](#riferimento-api)
7. [Esempi](#esempi)
8. [Risoluzione dei Problemi](#risoluzione-dei-problemi)
9. [Contribuire](#contribuire)

---

## Introduzione

### Cos'è PydocsExport?

**PydocsExport** è un potente modulo Python che consente di esportare la documentazione completa di Python installata nel vostro sistema in molteplici formati di e-book e formati di testo.

### Caratteristiche Principali

- ✅ Esportazione in **5 formati diversi**: TXT, PDF, EPUB, MOBI, HTML
- ✅ Supporto per **11 formati di carta** per i PDF (da A0 a A10)
- ✅ **Struttura organizzata** con capitoli e indice
- ✅ **Supporto multilingue** nella documentazione e nell'interfaccia
- ✅ **Registro di esportazione dettagliato** in JSON
- ✅ **API semplice e intuitiva** per facile integrazione
- ✅ **Interfaccia CLI** (EasyPydocsExport.py) per gli utenti

### Casi d'Uso

- Creare una documentazione Python completa offline
- Generare e-book per dispositivi di lettura
- Creare PDF stampabili in diversi formati
- Archiviare la documentazione per futuri riferimenti
- Creare risorse educative

---

## Installazione

### Requisiti

- Python 3.6 o superiore
- Nessuna dipendenza esterna richiesta (utilizza pydoc integrato)

### Passaggi di Installazione

1. **Clonare o scaricare** la directory del progetto:
```bash
git clone <repository_url>
cd PydocsExport
```

2. **Verificare la struttura**:
```bash
ls
# Dovrebbe visualizzare: src/, tests/, docs/, EasyPydocsExport.py
```

3. **Testare l'installazione**:
```bash
python EasyPydocsExport.py --help
```

### Struttura del Progetto

```
PydocsExport/
├── src/                          # Modulo principale
│   ├── __init__.py               # Inizializzazione del pacchetto
│   ├── exporter.py               # Classe esportatrice principale
│   ├── formatter.py              # Formattatori per diversi formati
│   └── index_manager.py          # Gestore degli indici
├── tests/                        # Test unitari
│   └── test_pydocs_export.py    # Suite di test completa
├── docs/                         # Documentazione
│   ├── README.md                 # Questo file (Italiano)
│   ├── README_EN.md              # Documentazione in inglese
│   ├── README_FR.md              # Documentazione in francese
│   ├── README_ES.md              # Documentazione in spagnolo
│   ├── README_DE.md              # Documentazione in tedesco
│   └── README_IT.md              # Documentazione in italiano
├── output/                       # Directory di output (creata al runtime)
├── EasyPydocsExport.py          # Script principale per gli utenti
└── README.md                     # File iniziale
```

---

## Utilizzo

### Utilizzo di Base

#### Via Script CLI (Consigliato)

```bash
# Esportare tutti i formati
python EasyPydocsExport.py

# Esportare solo TXT e HTML
python EasyPydocsExport.py --txt --html

# Esportare solo in PDF
python EasyPydocsExport.py --pdf

# Specificare una directory di output personalizzata
python EasyPydocsExport.py --output /mio/percorso/personalizzato

# Mostrare l'aiuto
python EasyPydocsExport.py --help
```

#### Via Modulo Python

```python
from src.exporter import PydocsExporter

# Creare un esportatore
esportatore = PydocsExporter(output_base_dir="mia_documentazione")

# Esportare tutti i formati
risultati = esportatore.export_all()

# Esportare formati specifici
risultati = esportatore.export_all(formats=['txt', 'epub', 'html'])

# Visualizzare i risultati
print(risultati)
```

### Opzioni Disponibili

| Opzione | Descrizione | Esempio |
|---------|-------------|---------|
| `--all` | Esportare tutti i formati | `--all` |
| `--txt` | Formato testo semplice | `--txt` |
| `--pdf` | Formato PDF (tutte le dimensioni) | `--pdf` |
| `--epub` | Formato e-book | `--epub` |
| `--mobi` | Formato Kindle/MOBI | `--mobi` |
| `--html` | Pagine HTML interattive | `--html` |
| `--output [dir]` | Directory di output | `--output /percorso` |
| `--help` | Mostra aiuto | `--help` |

---

## Architettura

### Componenti Principali

#### 1. PydocsExporter (exporter.py)

**Responsabilità:**
- Orchestrazione del processo di esportazione
- Recupero della documentazione pydocs
- Gestione dei formati carta per PDF
- Creazione di strutture di directory

**Formati di Carta Supportati:**
```
A0:  2384 × 3370 punti
A1:  1684 × 2384 punti
A2:  1191 × 1684 punti
A3:   842 × 1191 punti
A4:   595 ×  842 punti (Standard)
A5:   420 ×  595 punti
A6:   298 ×  420 punti
A7:   210 ×  298 punti
A8:   148 ×  210 punti
A9:   105 ×  148 punti
A10:  73  ×  105 punti
```

#### 2. Formattatori (formatter.py)

Fornisce classi di formattazione:

- **TextFormatter**: Formattazione semplice per TXT
- **PDFFormatter**: Adattamento per diversi formati carta
- **EbookFormatter**: Struttura per EPUB/MOBI

#### 3. Gestore degli Indici (index_manager.py)

Gestisce gli indici della documentazione:

- Creazione di indici in TXT, JSON, HTML
- Raggruppamento per categorie
- Generazione del sommario

---

## Formato di Output

### Struttura delle Directory

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
│   └── ... (altri formati carta)
│
├── EBOOK_EPUB/
│
├── EBOOK_MOBI/
│
└── HTML/
```

---

## Esempi

### Esempio 1: Esportazione Semplice

```bash
python EasyPydocsExport.py
```

Questo esporterà tutta la documentazione in tutti i formati disponibili
nella directory predefinita `pydocs_export_output/`.

### Esempio 2: Esportazione Specifica

```bash
python EasyPydocsExport.py --txt --html --output /mia/cartella
```

Esporta solo TXT e HTML in `/mia/cartella/`.

### Esempio 3: Utilizzo Programmatico

```python
#!/usr/bin/env python3
from pathlib import Path
from src.exporter import PydocsExporter

def main():
    # Creare un esportatore
    esportatore = PydocsExporter("mia_documentazione")
    
    # Esportare
    print("Inizio esportazione...")
    risultati = esportatore.export_all(['epub', 'mobi'])
    
    # Visualizzare le statistiche
    print(f"Moduli esportati: {risultati['total_modules']}")
    for fmt, stats in risultati['formats'].items():
        print(f"{fmt}: {stats}")

if __name__ == "__main__":
    main()
```

---

## Risoluzione dei Problemi

### Problema: Errore "Impossibile importare il modulo PydocsExporter"

**Soluzione:**
1. Verificare di essere nella directory corretta
2. Verificare che la directory `src/` esista
3. Verificare che `__init__.py` sia in `src/`

```bash
ls -la src/
# Dovrebbe visualizzare __init__.py
```

### Problema: Permesso negato durante la creazione dei file

**Soluzione:**
1. Verificare i permessi della directory di output
2. Utilizzare un'altra directory con `--output`

```bash
mkdir -p ~/mia_documentazione
python EasyPydocsExport.py --output ~/mia_documentazione
```

---

## Licenza

Questo progetto è sotto licenza MIT. Consultare il file `LICENSE` per ulteriori dettagli.

---

**Ultimo aggiornamento:** Gennaio 2024
**Versione:** 1.0.0

---

**Grazie per aver utilizzato PydocsExport! 🎉**
