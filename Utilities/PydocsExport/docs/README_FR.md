# PydocsExport - Documentation Complète

## Table des Matières

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Utilisation](#utilisation)
4. [Architecture](#architecture)
5. [Format de Sortie](#format-de-sortie)
6. [API Référence](#api-référence)
7. [Exemples](#exemples)
8. [Dépannage](#dépannage)
9. [Contribuer](#contribuer)

---

## Introduction

### Qu'est-ce que PydocsExport?

**PydocsExport** est un module Python puissant qui permet d'exporter la documentation complète de Python installée sur votre système en plusieurs formats de livres électroniques et formats texte.

### Caractéristiques Principales

- ✅ Exportation en **5 formats différents**: TXT, PDF, EPUB, MOBI, HTML
- ✅ Support de **11 formats de papier** pour les PDFs (A0 à A10)
- ✅ **Structure organisée** avec chapitres et index
- ✅ **Support multilingue** dans la documentation et l'interface
- ✅ **Journal d'exportation** détaillé en JSON
- ✅ **API simple et intuitive** pour une intégration facile
- ✅ **Interface CLI** (EasyPydocsExport.py) pour les utilisateurs

### Cas d'Usage

- Créer une documentation hors ligne complète de Python
- Générer des e-books pour une lecture sur liseuse
- Créer des PDFs imprimables dans différents formats
- Archiver la documentation pour la référence future
- Créer des ressources éducatives

---

## Installation

### Prérequis

- Python 3.6 ou supérieur
- Aucune dépendance externe requise (utilise pydoc built-in)

### Étapes d'Installation

1. **Cloner ou télécharger** le répertoire du projet:
```bash
git clone <repository_url>
cd PydocsExport
```

2. **Vérifier la structure**:
```bash
ls
# Devrait afficher: src/, tests/, docs/, EasyPydocsExport.py
```

3. **Tester l'installation**:
```bash
python EasyPydocsExport.py --help
```

### Structure du Projet

```
PydocsExport/
├── src/                          # Module principal
│   ├── __init__.py               # Package initialization
│   ├── exporter.py               # Classe exportateur principale
│   ├── formatter.py              # Formateurs pour différents formats
│   └── index_manager.py          # Gestionnaire d'index
├── tests/                        # Tests unitaires
│   └── test_pydocs_export.py    # Suite de tests complète
├── docs/                         # Documentation
│   ├── README.md                 # Ce fichier
│   ├── README_EN.md              # Documentation anglaise
│   ├── README_FR.md              # Documentation française
│   ├── README_ES.md              # Documentation espagnole
│   ├── README_DE.md              # Documentation allemande
│   └── README_IT.md              # Documentation italienne
├── output/                       # Répertoire de sortie (créé à l'exécution)
├── EasyPydocsExport.py          # Script principal pour utilisateurs
└── README.md                     # Fichier initial
```

---

## Utilisation

### Utilisation de Base

#### Via le Script CLI (Recommandé)

```bash
# Exporter tous les formats
python EasyPydocsExport.py

# Exporter uniquement en TXT et HTML
python EasyPydocsExport.py --txt --html

# Exporter en PDF uniquement
python EasyPydocsExport.py --pdf

# Spécifier un répertoire de sortie personnalisé
python EasyPydocsExport.py --output /mon/chemin/personnalisé

# Afficher l'aide
python EasyPydocsExport.py --help
```

#### Via le Module Python

```python
from src.exporter import PydocsExporter

# Créer un exportateur
exporter = PydocsExporter(output_base_dir="ma_documentation")

# Exporter tous les formats
resultats = exporter.export_all()

# Exporter des formats spécifiques
resultats = exporter.export_all(formats=['txt', 'epub', 'html'])

# Afficher les résultats
print(resultats)
```

### Options Disponibles

| Option | Description | Exemple |
|--------|-------------|---------|
| `--all` | Exporter tous les formats | `--all` |
| `--txt` | Format texte simple | `--txt` |
| `--pdf` | Format PDF (tous les tailles) | `--pdf` |
| `--epub` | Format livre électronique | `--epub` |
| `--mobi` | Format Kindle/MOBI | `--mobi` |
| `--html` | Pages HTML interactives | `--html` |
| `--output [dir]` | Répertoire de sortie | `--output /chemin` |
| `--help` | Affiche l'aide | `--help` |

---

## Architecture

### Composants Principaux

#### 1. PydocsExporter (exporter.py)

**Responsabilités:**
- Orchestration de l'exportation
- Récupération de la documentation pydocs
- Gestion des formats de papier pour PDF
- Création des structures de répertoires

**Formats de Papier Supportés:**
```
A0:  2384 × 3370 points
A1:  1684 × 2384 points
A2:  1191 × 1684 points
A3:   842 × 1191 points
A4:   595 ×  842 points (Standard)
A5:   420 ×  595 points
A6:   298 ×  420 points
A7:   210 ×  298 points
A8:   148 ×  210 points
A9:   105 ×  148 points
A10:  73  ×  105 points
```

#### 2. Formatters (formatter.py)

Fournit des classes de formatage:

- **TextFormatter**: Formatage simple pour TXT
- **PDFFormatter**: Adaptation pour différents formats de papier
- **EbookFormatter**: Structure pour EPUB/MOBI

```python
# Exemple d'utilisation
formatter = TextFormatter()
formatter.add_title("Mon Titre", level=1)
formatter.add_paragraph("Mon contenu")
formatter.add_code("print('Hello')", language="python")
contenu = formatter.get_content()
```

#### 3. IndexManager (index_manager.py)

Gère les index de documentation:

- Création d'index en TXT, JSON, HTML
- Groupage par catégories
- Génération de table des matières

```python
# Exemple d'utilisation
index_mgr = IndexManager()
index_mgr.add_entry("module_name", "path/to/file", "builtins", 1024)
index_mgr.create_index_file(Path("output"), format="html")
```

---

## Format de Sortie

### Structure de Répertoires

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
│   │   └── Python_Documentation_A0_[timestamp].txt
│   ├── A1/
│   │   └── Python_Documentation_A1_[timestamp].txt
│   ├── A3/
│   │   └── Python_Documentation_A3_[timestamp].txt
│   ├── A4/
│   │   └── Python_Documentation_A4_[timestamp].txt
│   └── ... (autres formats de papier)
│
├── EBOOK_EPUB/
│   └── Python_Documentation_[timestamp].epub
│
├── EBOOK_MOBI/
│   └── Python_Documentation_[timestamp].mobi
│
├── HTML/
│   ├── index.html (Index interactif)
│   ├── 001_sys.html
│   ├── 002_os.html
│   └── ...
│
├── INDEX.txt (Index général)
└── export_log_[timestamp].json (Journal d'exportation)
```

### Contenu du Fichier de Log

```json
{
  "timestamp": "20240115_143052",
  "formats": {
    "txt": {
      "format": "TXT",
      "files_created": 42,
      "total_size": 5242880,
      "chapters": [
        {
          "name": "sys",
          "file": "001_sys.txt",
          "size": 125440
        }
      ]
    }
  },
  "total_modules": 42,
  "errors": []
}
```

---

## API Référence

### PydocsExporter

#### Constructeur

```python
PydocsExporter(output_base_dir: str = "pydocs_export_output")
```

**Paramètres:**
- `output_base_dir`: Répertoire de base pour les exports

#### Méthode: export_all()

```python
export_all(formats: Optional[List[str]] = None) -> Dict[str, any]
```

**Paramètres:**
- `formats`: Liste des formats à exporter ('txt', 'pdf', 'epub', 'mobi', 'html')
  - Si `None`, tous les formats sont exportés

**Retour:**
- Dictionnaire contenant les statistiques d'export

**Exemple:**
```python
exporter = PydocsExporter()
resultats = exporter.export_all(['txt', 'html'])
print(resultats['total_modules'])  # Affiche le nombre de modules
```

### TextFormatter

```python
# Créer un formateur
formatter = TextFormatter()

# Ajouter contenu
formatter.add_title("Mon Titre", level=1)      # Titre niveau 1
formatter.add_title("Sous-titre", level=2)     # Titre niveau 2
formatter.add_paragraph("Un paragraphe")       # Paragraphe
formatter.add_code("python code", "python")   # Bloc de code

# Récupérer le contenu
contenu = formatter.get_content()
```

### IndexManager

```python
# Créer un gestionnaire d'index
index_mgr = IndexManager()

# Ajouter des entrées
index_mgr.add_entry(
    name="mon_module",
    path="chemin/vers/fichier",
    category="builtins",
    file_size=1024,
    module_type="built-in"
)

# Créer un fichier d'index
index_mgr.create_index_file(Path("output"), format="html")
```

---

## Exemples

### Exemple 1: Export Simple

```bash
python EasyPydocsExport.py
```

Cela va exporter toute la documentation en tous les formats disponibles
dans le répertoire par défaut `pydocs_export_output/`.

### Exemple 2: Export Spécifique

```bash
python EasyPydocsExport.py --txt --html --output /mon/dossier
```

Exporte uniquement en TXT et HTML dans `/mon/dossier/`.

### Exemple 3: Utilisation Programmée

```python
#!/usr/bin/env python3
from pathlib import Path
from src.exporter import PydocsExporter

def main():
    # Créer un exportateur
    exporter = PydocsExporter("ma_documentation")
    
    # Exporter
    print("Début de l'exportation...")
    resultats = exporter.export_all(['epub', 'mobi'])
    
    # Afficher les stats
    print(f"Modules exportés: {resultats['total_modules']}")
    for fmt, stats in resultats['formats'].items():
        print(f"{fmt}: {stats}")

if __name__ == "__main__":
    main()
```

### Exemple 4: Traitement Personnalisé

```python
from src.exporter import PydocsExporter
from src.index_manager import IndexManager
from pathlib import Path

# Créer l'exportateur
exporter = PydocsExporter()

# Obtenir la liste des modules
modules = exporter._get_all_modules()

# Créer un index personnalisé
index = IndexManager()
for module in modules[:10]:  # Premiers 10 modules
    index.add_entry(module, f"modules/{module}.txt", "demo", 1024)

# Sauvegarder l'index en HTML
index.create_index_file(exporter.output_base, format="html")
```

---

## Dépannage

### Problème: Erreur "Impossible d'importer le module PydocsExporter"

**Solution:**
1. Vérifiez que vous êtes dans le répertoire correct
2. Vérifiez que le répertoire `src/` existe
3. Vérifiez que `__init__.py` est dans `src/`

```bash
ls -la src/
# Devrait afficher __init__.py
```

### Problème: Permission refusée lors de la création des fichiers

**Solution:**
1. Vérifiez les permissions du répertoire de sortie
2. Utilisez un autre répertoire avec `--output`

```bash
# Créer un répertoire avec permissions
mkdir -p ~/my_docs
python EasyPydocsExport.py --output ~/my_docs
```

### Problème: Fichiers de sortie corrompus ou vides

**Solution:**
1. Vérifiez l'espace disque disponible
2. Vérifiez les logs d'erreur dans le fichier `export_log_[timestamp].json`
3. Essayez un export de format unique

```bash
python EasyPydocsExport.py --txt
```

### Problème: Exportation très lente

**Solution:**
- C'est normal pour une première exportation complète
- Les modules sont nombreux (100+)
- Soyez patient ou réduisez le nombre de modules dans `exporter.py`

---

## Contribuer

### Signaler un Bug

1. Ouvrez une issue avec:
   - Description du problème
   - Pas de reproduction
   - Environnement (OS, Python version)

### Proposer une Amélioration

1. Fork le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Commitez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Exécuter les Tests

```bash
python -m pytest tests/ -v
# ou
python tests/test_pydocs_export.py
```

---

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## Support

Pour toute question ou support:
- 📧 Email: support@pydocsexport.local
- 🐛 Issues: https://github.com/example/pydocsexport/issues
- 💬 Discussions: https://github.com/example/pydocsexport/discussions

---

**Dernière mise à jour:** Janvier 2024
**Version:** 1.0.0
**Maintenant:** Copilot

---

## Ressources Supplémentaires

### Documentation Python Officielle
- [pydoc](https://docs.python.org/3/library/pydoc.html)
- [Built-in Modules](https://docs.python.org/3/library/index.html)

### Formats de Livres Électroniques
- [EPUB Format](https://www.w3.org/publishing/epub/)
- [MOBI Format](https://wiki.mobileread.com/wiki/MOBI)

### Autres Outils
- [Sphinx](https://www.sphinx-doc.org/) - Générateur de documentation
- [Pandoc](https://pandoc.org/) - Convertisseur de documents

---

**Merci d'utiliser PydocsExport! 🎉**
