# M13 Python3 Modules Collection - Made with AI

Comprehensive collection of production-ready Python utilities and data structure modules. All modules have been developed and enhanced with AI assistance.

## Features

### Core Modules

1. **VariableExtender** - Advanced data structures and utilities
   - `generic_tree` - N-ary tree data structure with metadata support
   - `MenuMaker` - Dynamic, interactive menu management system
   - `Multidimention_table` - Efficient multi-dimensional array operations
   - `multidimention_paint` - Geometric shapes and selection in N-dimensional space

2. **Utilities** - Development and documentation tools
   - `PydocsExport` - Python documentation exporter (multiple formats)

## Quick Start

### Installation

```bash
pip install M13aiCollection
```

### Running Modules

#### Option 1: Use Interactive Menu

```bash
python run.py
```

This launches an interactive menu where you can select modules to run.

#### Option 2: Import in Your Code

```python
from VariableExtender.generic_tree import GenericTree
from VariableExtender.MenuMaker import Menu
from VariableExtender.Multidimention_table import MultiTable
```

## Module Documentation

### GenericTree
Flexible n-ary tree structure supporting any Python value types.

```python
from VariableExtender.generic_tree import GenericTree

tree = GenericTree("root")
tree.add_child("child1")
tree.add_child("child2")
print(tree)  # Displays tree structure
```

See [VariableExtender/generic_tree/README.md](VariableExtender/generic_tree/README.md) for full documentation.

### MenuMaker
Create interactive menus with various item types (text input, numeric input, checkboxes, radio buttons).

```python
from VariableExtender.MenuMaker import Menu, TextInput

menu = Menu("Main Menu")
menu.add_item(TextInput("name", "Enter your name: "))
menu.show()
```

See [VariableExtender/MenuMaker/README.md](VariableExtender/MenuMaker/README.md) for full documentation.

### MultiTable
Efficient operations on multi-dimensional arrays.

```python
from VariableExtender.Multidimention_table import MultiTable

table = MultiTable(2)  # Create 2D table
table[0][0] = 42
print(table[0][0])  # Output: 42
```

See [VariableExtender/Multidimention_table/README.md](VariableExtender/Multidimention_table/README.md) for full documentation.

### PydocsExport
Export Python module documentation to various formats.

See [Utilities/PydocsExport/README.md](Utilities/PydocsExport/README.md) for full documentation.

## Supported Languages

Documentation available in:
- English (English)
- Français (French)
- Español (Spanish)
- Deutsch (German)
- Italiano (Italian)
- Português (Portuguese)

## Project Structure

```
M13-Python3-Modules-Collection-made-in-AI/
├── README.md                    # This file
├── run.py                       # Main interactive menu
├── pyproject.toml               # Project configuration
├── Utilities/                   # Utility modules
│   ├── PydocsExport/           # Documentation exporter
│   └── run.py                  # Utilities menu
└── VariableExtender/           # Data structure modules
    ├── generic_tree/           # N-ary tree implementation
    ├── MenuMaker/              # Menu system
    ├── Multidimention_table/   # Multi-dimensional arrays
    ├── multidimention_paint/   # N-dimensional geometry
    └── run.py                  # VariableExtender menu
```

## Testing

Run the test suite:

```bash
pytest
```

Individual module tests:

```bash
pytest VariableExtender/generic_tree/test_generic_tree.py
pytest VariableExtender/MenuMaker/test_menumaker.py
pytest VariableExtender/Multidimention_table/test_multitable.py
```

## Requirements

- Python 3.7+
- See [requirements.txt](requirements.txt) for dependencies

## License

MIT License - See [LICENSE](LICENSE) file for details

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history

## Author

Created by Musclor13 with AI assistance

## AI Generation Notice

This project and its modules were generated/enhanced using AI assistance (Claude). All code has been reviewed for quality and functionality.
