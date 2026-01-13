# variableplus - Python Package Collection

**Language / Langue**: [English](#english) | [Français](#français)

---

## English

### Overview

**variableplus** is a comprehensive Python package collection featuring multiple specialized modules for data structures, user interfaces, and geometric operations. Created by **Musclor13** with AI assistance, this project provides production-ready implementations for common programming challenges.

### Package Contents

The **variableplus** project includes four main modules:

#### 1. **generic_tree** 
A complete n-ary tree data structure implementation with advanced features:
- Support for any Python data type as node values
- 30+ tree manipulation methods
- Multiple traversal modes (PRE_ORDER, POST_ORDER, LEVEL_ORDER, IN_ORDER)
- Search algorithms (DFS, BFS, predicate-based)
- Functional operations (map, filter, reduce, apply)
- JSON serialization support
- 52+ core unit tests
- Complete type hints

**Key Features:**
- Unlimited children per node
- Thread-safe operations
- Memory-efficient structure
- Zero external dependencies

#### 2. **MenuMaker**
An interactive menu system for building command-line interfaces:
- Simple and powerful menu creation
- Support for multiple item types (command, submenu, separator, text, radio, checkbox)
- Nested menu structure
- Automatic layout and formatting
- Item groups and organization
- Example implementations

**Key Features:**
- Easy-to-use API
- Flexible item configuration
- Professional appearance
- No external dependencies required

#### 3. **Multidimention_table**
Multi-dimensional array/table handling for 1D to n-dimensional data:
- Support for 1D, 2D, 3D, 4D, and beyond
- Flexible shape definition
- Automatic dimension calculation
- Comprehensive error handling
- Sub-module for geometric operations

**Key Features:**
- Flexible dimensionality
- Intuitive indexing
- Robust validation
- Multiple view options

#### 4. **multidimention_paint** (sub-module)
Advanced point and geometric shape management:
- Point operations in n-dimensional space
- Multiple shape types (Line, Circle, Rectangle, Square, Ellipse, Arc, ClosedShape)
- Point selection and manipulation
- Distance and midpoint calculations
- Dual import system (package and standalone usage)

**Key Features:**
- Full n-dimensional support
- Flexible shape definitions
- Point collection management
- Utility functions for geometry

### Installation

Install via pip:

```bash
pip install variableplus
```

Or from source:

```bash
git clone <repository-url>
cd variableplus
pip install -e .
```

### Quick Start

#### generic_tree Example
```python
from generic_tree import Tree, TreeNode

# Create a tree
tree = Tree()
root = tree.root

# Add children
child1 = root.add_child("Child 1")
child2 = root.add_child("Child 2")
grandchild = child1.add_child("Grandchild")

# Traverse tree
for node in tree.traverse(traversal_mode='PRE_ORDER'):
    print(node.value)
```

#### MenuMaker Example
```python
from MenuMaker import Menu, MenuItem, ItemType

menu = Menu("Main Menu")
menu.add_item(MenuItem("Option 1", item_type=ItemType.COMMAND))
menu.add_item(MenuItem("Option 2", item_type=ItemType.COMMAND))
menu.display()
```

#### Multidimension Table Example
```python
from Multidimention_table import MultiDimTable

# Create 3D table
table = MultiDimTable(shape=(2, 3, 4))
table[0, 1, 2] = "value"
```

#### Geometric Shapes Example
```python
from Multidimention_table.multidimention_paint import Point, Circle, distance

p1 = Point(0, 0)
p2 = Point(3, 4)
circle = Circle(p1, 5)

dist = distance(p1, p2)  # 5.0
```

### Project Metadata

- **Project Name**: variableplus
- **Author**: Musclor13
- **AI Assistance**: Yes
- **License**: MIT
- **Python Version**: 3.7+
- **Status**: Production Ready

### Supported Languages

Documentation available in:
- 🇺🇸 English
- 🇫🇷 French
- 🇪🇸 Spanish
- 🇩🇪 German
- 🇮🇹 Italian
- 🇨🇳 Chinese (Simplified)
- 🇵🇹 Portuguese

### Documentation

- **setup.py** - Package configuration
- **pyproject.toml** - Modern Python project metadata
- **CONTRIBUTING.md** - Contribution guidelines
- **CHANGELOG.md** - Version history
- **LICENSE** - MIT License

Each module includes comprehensive documentation:
- Module-specific README files
- Detailed API documentation
- Multiple language support
- Usage examples
- Quick start guides

### Features Across All Modules

✅ **Production Ready** - Thoroughly tested and documented
✅ **Type Hints** - Full Python type hint support
✅ **Zero Dependencies** - No external package requirements
✅ **Multilingual** - Documentation in 7 languages
✅ **Well-tested** - Comprehensive test coverage
✅ **Professional** - Clean, maintainable code
✅ **Open Source** - MIT License

### Requirements

- Python 3.7 or higher
- No external dependencies

### Testing

Each module includes comprehensive tests:

```bash
# Run all tests
pytest

# Run specific module tests
pytest generic_tree/test_generic_tree.py
pytest MenuMaker/test_menumaker.py
pytest Multidimention_table/test_multidim_table.py
```

### Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Project Structure

```
variableplus/
├── generic_tree/              # N-ary tree data structure
│   ├── __init__.py
│   ├── generic_tree.py
│   ├── test_generic_tree.py
│   └── README.md
├── MenuMaker/                 # Interactive menu system
│   ├── __init__.py
│   ├── menu.py
│   ├── test_menumaker.py
│   └── README.md
├── Multidimention_table/      # Multi-dimensional arrays
│   ├── __init__.py
│   ├── multidim_table.py
│   ├── multitable.py
│   ├── multidimention_paint/  # Geometric shapes & points
│   │   ├── __init__.py
│   │   ├── paint.py
│   │   ├── points.py
│   │   ├── shapes.py
│   │   ├── selection.py
│   │   ├── utils.py
│   │   └── README.md
│   └── README.md
├── setup.py                   # Package configuration
├── pyproject.toml            # Modern project metadata
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # Contribution guidelines
└── README.md                 # This file
```

### Contact

For questions, issues, or suggestions, please use the GitHub issue tracker or contact the project maintainer.

---

## Français

### Aperçu

**variableplus** est une collection de packages Python complète comprenant plusieurs modules spécialisés pour les structures de données, les interfaces utilisateur et les opérations géométriques. Créé par **Musclor13** avec l'aide d'une IA, ce projet fournit des implémentations prêtes pour la production pour les défis de programmation courants.

### Contenu du Package

Le projet **variableplus** comprend quatre modules principaux :

#### 1. **generic_tree**
Une implémentation complète de structure de données d'arbre n-aire avec des fonctionnalités avancées :
- Support de n'importe quel type de données Python comme valeurs de nœud
- 30+ méthodes de manipulation d'arbres
- Modes de traversée multiples (PRE_ORDER, POST_ORDER, LEVEL_ORDER, IN_ORDER)
- Algorithmes de recherche (DFS, BFS, basés sur prédicats)
- Opérations fonctionnelles (map, filter, reduce, apply)
- Support de sérialisation JSON
- 52+ tests unitaires principaux
- Indices de type complets

**Caractéristiques principales:**
- Enfants illimités par nœud
- Opérations thread-safe
- Structure efficace en mémoire
- Zéro dépendances externes

#### 2. **MenuMaker**
Un système de menu interactif pour créer des interfaces de ligne de commande :
- Création de menu simple et puissante
- Support de types d'éléments multiples (commande, sous-menu, séparateur, texte, radio, case à cocher)
- Structure de menu imbriquée
- Mise en page et formatage automatiques
- Groupes d'éléments et organisation
- Implémentations d'exemple

**Caractéristiques principales:**
- API facile à utiliser
- Configuration d'élément flexible
- Apparence professionnelle
- Aucune dépendance externe requise

#### 3. **Multidimention_table**
Gestion de tableaux/tableaux multi-dimensionnels pour données 1D à n-dimensionnelles :
- Support pour 1D, 2D, 3D, 4D et au-delà
- Définition flexible de la forme
- Calcul automatique des dimensions
- Gestion d'erreurs complète
- Sous-module pour opérations géométriques

**Caractéristiques principales:**
- Dimensionnalité flexible
- Indexation intuitive
- Validation robuste
- Plusieurs options d'affichage

#### 4. **multidimention_paint** (sous-module)
Gestion avancée de points et de formes géométriques :
- Opérations ponctuelles dans l'espace n-dimensionnel
- Types de formes multiples (Ligne, Cercle, Rectangle, Carré, Ellipse, Arc, FermeeShape)
- Sélection et manipulation de points
- Calculs de distance et de point milieu
- Système d'import dual (utilisation en package et autonome)

**Caractéristiques principales:**
- Support complet n-dimensionnel
- Définitions de formes flexibles
- Gestion de collection de points
- Fonctions utilitaires pour la géométrie

### Installation

Installez via pip :

```bash
pip install variableplus
```

Ou depuis la source :

```bash
git clone <url-repository>
cd variableplus
pip install -e .
```

### Démarrage Rapide

#### Exemple generic_tree
```python
from generic_tree import Tree, TreeNode

# Créer un arbre
tree = Tree()
root = tree.root

# Ajouter des enfants
child1 = root.add_child("Child 1")
child2 = root.add_child("Child 2")
grandchild = child1.add_child("Grandchild")

# Parcourir l'arbre
for node in tree.traverse(traversal_mode='PRE_ORDER'):
    print(node.value)
```

#### Exemple MenuMaker
```python
from MenuMaker import Menu, MenuItem, ItemType

menu = Menu("Menu Principal")
menu.add_item(MenuItem("Option 1", item_type=ItemType.COMMAND))
menu.add_item(MenuItem("Option 2", item_type=ItemType.COMMAND))
menu.display()
```

#### Exemple Tableau Multidimensionnel
```python
from Multidimention_table import MultiDimTable

# Créer un tableau 3D
table = MultiDimTable(shape=(2, 3, 4))
table[0, 1, 2] = "valeur"
```

#### Exemple Formes Géométriques
```python
from Multidimention_table.multidimention_paint import Point, Circle, distance

p1 = Point(0, 0)
p2 = Point(3, 4)
circle = Circle(p1, 5)

dist = distance(p1, p2)  # 5.0
```

### Métadonnées du Projet

- **Nom du Projet**: variableplus
- **Auteur**: Musclor13
- **Aide IA**: Oui
- **Licence**: MIT
- **Version Python**: 3.7+
- **Statut**: Prêt pour la Production

### Langues Supportées

Documentation disponible en:
- 🇺🇸 Anglais
- 🇫🇷 Français
- 🇪🇸 Espagnol
- 🇩🇪 Allemand
- 🇮🇹 Italien
- 🇨🇳 Chinois (Simplifié)
- 🇵🇹 Portugais

### Documentation

- **setup.py** - Configuration du package
- **pyproject.toml** - Métadonnées modernes du projet Python
- **CONTRIBUTING.md** - Lignes directrices de contribution
- **CHANGELOG.md** - Historique des versions
- **LICENSE** - Licence MIT

Chaque module inclut une documentation complète :
- Fichiers README spécifiques aux modules
- Documentation API détaillée
- Support multilingue
- Exemples d'utilisation
- Guides de démarrage rapide

### Fonctionnalités dans Tous les Modules

✅ **Prêt pour la Production** - Entièrement testé et documenté
✅ **Type Hints** - Support complet des indices de type Python
✅ **Zéro Dépendances** - Aucune dépendance de package externe
✅ **Multilingue** - Documentation dans 7 langues
✅ **Bien testé** - Couverture de test complète
✅ **Professionnel** - Code propre et maintenable
✅ **Open Source** - Licence MIT

### Exigences

- Python 3.7 ou supérieur
- Aucune dépendance externe

### Tests

Chaque module inclut des tests complets :

```bash
# Exécuter tous les tests
pytest

# Exécuter les tests du module spécifique
pytest generic_tree/test_generic_tree.py
pytest MenuMaker/test_menumaker.py
pytest Multidimention_table/test_multidim_table.py
```

### Contribution

Les contributions sont bienvenues ! Veuillez consulter [CONTRIBUTING.md](CONTRIBUTING.md) pour les directives.

### Licence

Ce projet est autorisé sous la Licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

### Structure du Projet

```
variableplus/
├── generic_tree/              # Structure de données d'arbre n-aire
│   ├── __init__.py
│   ├── generic_tree.py
│   ├── test_generic_tree.py
│   └── README.md
├── MenuMaker/                 # Système de menu interactif
│   ├── __init__.py
│   ├── menu.py
│   ├── test_menumaker.py
│   └── README.md
├── Multidimention_table/      # Tableaux multi-dimensionnels
│   ├── __init__.py
│   ├── multidim_table.py
│   ├── multitable.py
│   ├── multidimention_paint/  # Formes géométriques et points
│   │   ├── __init__.py
│   │   ├── paint.py
│   │   ├── points.py
│   │   ├── shapes.py
│   │   ├── selection.py
│   │   ├── utils.py
│   │   └── README.md
│   └── README.md
├── setup.py                   # Configuration du package
├── pyproject.toml            # Métadonnées modernes du projet
├── LICENSE                   # Licence MIT
├── CONTRIBUTING.md           # Lignes directrices de contribution
└── README.md                 # Ce fichier
```

### Contact

Pour des questions, des problèmes ou des suggestions, veuillez utiliser le suivi des problèmes GitHub ou contacter le responsable du projet.

---

**Created with AI assistance** | **Créé avec l'aide d'une IA**  
**License / Licence: MIT** | **Author / Auteur: Musclor13**
