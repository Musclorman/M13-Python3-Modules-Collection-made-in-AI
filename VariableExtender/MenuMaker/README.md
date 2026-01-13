# MenuMaker - Menu Management Module

[![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-orange)](https://github.com)

A simple yet powerful Python module for managing menus in console and graphical applications with built-in internationalization support.

## Features

✨ **Complete Menu Management**
- Dynamic menu creation and manipulation
- Multiple menu item types (text, numeric, checkbox, radio, action, submenu)
- Nested submenu support
- Item enable/disable and visibility control

🌍 **Internationalization**
- Built-in gettext support for multilingual applications
- Easy language switching
- French and English documentation

🎯 **Developer Friendly**
- Zero external dependencies (pure Python)
- Simple and intuitive API
- Type hints for IDE support
- Comprehensive documentation with examples

📋 **Rich Item Types**
- Text input items
- Numeric input with validation (min/max)
- Checkbox items
- Radio button items (single or multiple selection)
- Action buttons with callbacks
- Submenu items
- Visual separators

## Installation

### Requirements
- Python 3.6 or higher
- No external dependencies

### Usage

Simply copy the `MenuMaker` directory to your project or add it to your Python path:

```python
from MenuMaker import Menu, MenuItem, MenuSystem, ItemType
```

## Quick Start

### Create a Simple Menu

```python
from MenuMaker import Menu

# Create menu
menu = Menu("main", label="Main Menu")

# Add items
menu.add_action("start", "Start Game")
menu.add_action("settings", "Settings")
menu.add_action("quit", "Quit")

# Display items
for item in menu.get_visible_items():
    print(f"- {item.label}")
```

### Menu with Multiple Item Types

```python
from MenuMaker import Menu

menu = Menu("user", label="User Settings")

# Text input
menu.add_text_input("username", "Username", default="Player1")

# Numeric input with validation
menu.add_numeric_input("level", "Difficulty", 
                       default=1, min_val=1, max_val=5)

# Checkbox
menu.add_checkbox("fullscreen", "Fullscreen", default=True)

# Radio buttons
menu.add_radio("language", "Language",
              options=["English", "Français", "Español"],
              default="English")

# Get all values
settings = menu.get_all_values()
```

### Submenus

```python
from MenuMaker import Menu

# Main menu
main = Menu("main", label="Main Menu")

# Submenu
settings = Menu("settings", label="Settings")
settings.add_checkbox("sound", "Enable Sound", default=True)
settings.add_numeric_input("volume", "Volume", default=80, min_val=0, max_val=100)

# Add to main menu
main.add_submenu("settings", "Settings", settings)
```

### Actions with Callbacks

```python
from MenuMaker import Menu

def on_start(item):
    print("Game starting...")
    return True

menu = Menu("game", label="Game Menu")
menu.add_action("start", "Start Game", callback=on_start)

# Execute
menu.get_item("start").execute()
```

## API Overview

### Menu Creation

```python
# Create a menu
menu = Menu(identifier="menu_id", label="Menu Title")

# Add different item types
menu.add_text_input(id, label, default="")
menu.add_numeric_input(id, label, default=0, min_val=0, max_val=100)
menu.add_checkbox(id, label, default=False)
menu.add_radio(id, label, options=["A", "B", "C"])
menu.add_action(id, label, callback=function)
menu.add_submenu(id, label, submenu)
menu.add_separator()
```

### Value Management

```python
# Get/Set values
menu.set_value("item_id", value)
value = menu.get_value("item_id")
all_values = menu.get_all_values()

menu.set_all_values({"id1": val1, "id2": val2})
menu.reset_all()
```

### Item Control

```python
# Enable/Disable
menu.enable_item("item_id")
menu.disable_item("item_id")

# Show/Hide
menu.show_item("item_id")
menu.hide_item("item_id")

# Get filtered items
visible = menu.get_visible_items()
enabled = menu.get_enabled_items()
```

### Menu System (with i18n)

```python
from MenuMaker import MenuSystem

system = MenuSystem(locale_dir="./locale", default_language="fr")
menu = system.create_menu("main", label="Menu Principal")

# Change language
system.set_language("en")
```

## Examples

### Example 1: Game Configuration Menu

```python
from MenuMaker import Menu

config = Menu("game_config", label="Game Configuration")

# Graphics
config.add_numeric_input("width", "Width", default=1920, min_val=800, max_val=3840)
config.add_numeric_input("height", "Height", default=1080, min_val=600, max_val=2160)
config.add_radio("quality", "Graphics Quality",
                options=["Low", "Medium", "High", "Ultra"],
                default="High")
config.add_checkbox("vsync", "V-Sync", default=True)

# Audio
config.add_numeric_input("volume", "Master Volume", default=80, min_val=0, max_val=100)
config.add_checkbox("effects", "Sound Effects", default=True)

# Get settings
settings = config.get_all_values()
print(settings)
```

### Example 2: Hierarchical Menu

```python
from MenuMaker import Menu

main = Menu("main", label="Main Menu")

# Game submenu
game = Menu("game", label="Game")
game.add_action("new", "New Game")
game.add_action("load", "Load Game")
game.add_action("save", "Save Game")
main.add_submenu("game", "Game", game)

# Settings submenu
settings = Menu("settings", label="Settings")
settings.add_numeric_input("difficulty", "Difficulty", default=1, min_val=1, max_val=5)
settings.add_radio("language", "Language", options=["English", "Français"])
main.add_submenu("settings", "Settings", settings)

# Help submenu
help_menu = Menu("help", label="Help")
help_menu.add_action("about", "About")
main.add_submenu("help", "Help", help_menu)
```

### Example 3: Form with Validation

```python
from MenuMaker import Menu

form = Menu("registration", label="Registration")
form.add_text_input("email", "Email")
form.add_text_input("password", "Password")
form.add_numeric_input("age", "Age", default=18, min_val=13, max_val=120)
form.add_checkbox("terms", "I agree to terms")

def validate():
    email = form.get_value("email")
    if "@" not in email:
        return False, "Invalid email"
    
    password = form.get_value("password")
    if len(password) < 6:
        return False, "Password too short"
    
    age = form.get_value("age")
    if age < 18:
        return False, "Must be 18+"
    
    return True, "Valid"

# Test
form.set_value("email", "user@example.com")
form.set_value("password", "secure123")
form.set_value("age", 25)

valid, msg = validate()
print(f"{msg}: {valid}")  # Valid: True
```

## Internationalization (i18n)

MenuMaker supports multilingual applications using Python's gettext module.

### Setup

```python
from MenuMaker import MenuSystem

menu_system = MenuSystem(locale_dir="./locale", default_language="fr")
```

### Translation File Structure

```
MenuMaker/
├── locale/
│   ├── fr/LC_MESSAGES/
│   │   ├── menumaker.po
│   │   └── menumaker.mo
│   └── en/LC_MESSAGES/
│       ├── menumaker.po
│       └── menumaker.mo
```

### Creating Translations

1. **Extract strings**:
```bash
xgettext -o locale/menumaker.pot MenuMaker/menu.py
```

2. **Initialize for language**:
```bash
msginit -i locale/menumaker.pot -l fr -o locale/fr/LC_MESSAGES/menumaker.po
```

3. **Translate and compile**:
```bash
msgfmt -o locale/fr/LC_MESSAGES/menumaker.mo locale/fr/LC_MESSAGES/menumaker.po
```

## Documentation

- [English Documentation](DOCUMENTATION_EN.md) - Complete API reference and examples
- [French Documentation](DOCUMENTATION_FR.md) - Documentation complète en français

## Testing

The module includes a comprehensive test suite with 100+ unit tests covering:
- Menu creation and manipulation
- All item types
- Value management
- Enable/disable/visibility
- Callbacks and actions
- Submenu handling
- Numeric validation
- Form validation
- Edge cases

Run tests with:
```bash
python -m pytest test_menumaker.py -v
```

## Project Structure

```
MenuMaker/
├── __init__.py                 # Package initialization
├── menu.py                     # Core classes (Menu, MenuItem, MenuSystem, ItemType)
├── test_menumaker.py          # Comprehensive test suite (100+ tests)
├── DOCUMENTATION_EN.md        # English documentation
├── DOCUMENTATION_FR.md        # French documentation
├── README.md                  # This file
└── locale/                    # Translation files (optional)
    ├── fr/LC_MESSAGES/
    │   └── menumaker.{po,mo}
    └── en/LC_MESSAGES/
        └── menumaker.{po,mo}
```

## Key Classes

### MenuItem
Represents a single menu item with type, value, and callback support.

### Menu
Manages a collection of menu items with value management and item control.

### MenuSystem
Top-level system managing multiple menus with internationalization support.

### ItemType
Enumeration of available item types (TEXT, NUMERIC, CHECKBOX, RADIO, ACTION, SUBMENU, SEPARATOR).

## Performance Notes

- Menus are lightweight and suitable for both large and small applications
- Value management is O(1) for direct item access
- Iteration over visible/enabled items is O(n)
- Deep copying menus uses Python's copy.deepcopy

## Error Handling

The module handles common errors gracefully:

```python
# Invalid value assignment returns False
if not menu.set_value("age", 200):  # Out of range
    print("Value rejected")

# get_value returns None for non-existent items
value = menu.get_value("nonexistent")  # Returns None

# Invalid operations don't raise exceptions
menu.remove_item("nonexistent")  # Returns False
```

## Contributing

To extend MenuMaker:

1. Add new item types to `ItemType` enum
2. Implement methods in `Menu` class
3. Add comprehensive tests
4. Update documentation

## Requirements

- Python 3.6+
- Standard Library only (gettext, enum, typing, copy)

## License

MIT License - See LICENSE file for details

## Version History

### Version 1.0.0
- Initial release
- All core features implemented
- 100+ tests passing
- French and English documentation
- Gettext internationalization support

---

**Need Help?**
- Check [English Documentation](DOCUMENTATION_EN.md) for detailed API reference
- Check [French Documentation](DOCUMENTATION_FR.md) for French guide
- Review examples in this README
- Check test file for usage patterns

**Questions or Issues?**
- Review troubleshooting section in documentation
- Check test cases for examples
- Verify internationalization setup if translations don't work

---

**Last Updated**: 2024  
**Author**: MenuMaker Contributors  
**Python**: 3.6+
