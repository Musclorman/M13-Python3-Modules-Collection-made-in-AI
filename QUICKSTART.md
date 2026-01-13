# M13 Modules Collection - Quick Start Guide

This guide will get you started with the M13 Python Modules Collection in 5 minutes.

## Installation

### From PyPI (when published)

```bash
pip install M13aiCollection
```

### From Source

```bash
git clone https://github.com/Musclorman/M13-Python3-Modules-Collection-made-in-AI
cd M13-Python3-Modules-Collection-made-in-AI
pip install -e .
```

## Run Interactive Menu

The easiest way to explore all modules:

```bash
python run.py
```

This launches an interactive menu system where you can:
1. Browse available modules
2. Run examples for each module
3. Return to previous menu or exit

## Quick Module Examples

### 1. Generic Tree - Hierarchical Data Structure

```python
from VariableExtender.generic_tree import GenericTree

# Create a tree
tree = GenericTree("root")

# Add children
child1 = tree.add_child("child1")
child2 = tree.add_child("child2")

# Add grandchildren
child1.add_child("grandchild1")

# Add metadata
tree.add_metadata("description", "My tree")

print(tree)  # Display tree structure
print(tree.depth())  # Get tree depth
```

### 2. Menu Maker - Interactive Menus

```python
from VariableExtender.MenuMaker import Menu, TextInput, NumericInput

# Create a menu
menu = Menu("User Registration")

# Add input items
menu.add_item(TextInput("name", "Enter your name: "))
menu.add_item(NumericInput("age", "Enter your age: "))

# Display and get results
results = menu.show()
print(f"Hello {results['name']}, age {results['age']}")
```

### 3. Multi-Dimensional Tables

```python
from VariableExtender.Multidimention_table import MultiTable

# Create a 2D table
table = MultiTable(2, size=(3, 3))

# Set values
table[0][0] = 1
table[1][1] = 5
table[2][2] = 9

# Get values
print(table[1][1])  # Output: 5

# Create 3D table
table_3d = MultiTable(3, size=(2, 2, 2))
table_3d[0][1][0] = "value"
```

### 4. Multidimensional Paint - Geometric Shapes

```python
from VariableExtender.Multidimention_table.multidimention_paint import MultidimensionalPaint

# Create painter
painter = MultidimensionalPaint()

# Add points
painter.add_point(0, 0)
painter.add_point(5, 5)
painter.add_point(10, 10)

# Draw shapes
painter.draw_circle((5, 5), radius=3)
painter.draw_rectangle((0, 0), (10, 10))

# Select points in region
selected = painter.select_within_region((0, 0), (5, 5))
print(f"Points in region: {len(selected)}")

# Get statistics
stats = painter.get_statistics()
print(f"Centroid: {stats['centroid']}")
```

### 5. Python Documentation Exporter

```python
from Utilities.PydocsExport import PydocsExport

# Create exporter
exporter = PydocsExport()

# Export module documentation
exporter.export_module("mymodule", output_format="html")
exporter.export_module("mymodule", output_format="pdf")
exporter.export_module("mymodule", output_format="markdown")
```

## Directory Structure for Your Project

```
my_project/
├── main.py
└── requirements.txt
```

### requirements.txt

```
M13aiCollection>=1.0.0
pytest>=7.0
```

### main.py

```python
from VariableExtender.generic_tree import GenericTree
from VariableExtender.MenuMaker import Menu

# Your code using the modules
tree = GenericTree("root")
# ... rest of your code
```

## Running Tests

Test all modules:

```bash
pytest
```

Test specific module:

```bash
pytest VariableExtender/generic_tree/test_generic_tree.py -v
```

## Documentation

For more detailed documentation:

- **Generic Tree**: [VariableExtender/generic_tree/README.md](VariableExtender/generic_tree/README.md)
- **Menu Maker**: [VariableExtender/MenuMaker/README.md](VariableExtender/MenuMaker/README.md)
- **Multidimensional Table**: [VariableExtender/Multidimention_table/README.md](VariableExtender/Multidimention_table/README.md)
- **Paint**: [VariableExtender/Multidimention_table/multidimention_paint/README.md](VariableExtender/Multidimention_table/multidimention_paint/README.md)
- **PydocsExport**: [Utilities/PydocsExport/README.md](Utilities/PydocsExport/README.md)

## Common Tasks

### Adding a Node to Tree

```python
parent = tree.find("parent_name")
if parent:
    new_child = parent.add_child("new_child")
```

### Creating Multi-Dimensional Table

```python
# Create 4D table
table = MultiTable(4, size=(2, 3, 4, 5))

# Access element
value = table[0][1][2][3]
```

### Selecting Points with Conditions

```python
# Rectangular region
selected = painter.select_within_region((0, 0), (10, 10))

# Circular region
selected = painter.select_within_radius((5, 5), 3)

# Custom selection
selected = painter.select_by_distance((5, 5), max_dist=7)
```

## Troubleshooting

### ImportError: Cannot import module

```bash
# Reinstall the package
pip install -e . --force-reinstall
```

### Tests failing

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run with verbose output
pytest -vv
```

### Module not found

Make sure you're in the correct directory and the package is installed:

```bash
python -c "import VariableExtender; print(VariableExtender.__file__)"
```

## Contributing

Found a bug or want to add a feature?

1. Check [CONTRIBUTING.md](CONTRIBUTING.md)
2. Create an issue or pull request
3. Follow coding standards (see project configuration)

## License

All modules are MIT Licensed. See [LICENSE](LICENSE) for details.

## Support

- **Issues**: GitHub Issues
- **Documentation**: See README.md files in each module
- **Examples**: See example.py files in modules

## Next Steps

1. Run `python run.py` to explore the interactive menu
2. Try the quick examples above in your Python shell
3. Read module-specific documentation
4. Contribute improvements back to the project!

---

**Happy coding! 🚀**

For more information, visit: https://github.com/Musclorman/M13-Python3-Modules-Collection-made-in-AI
