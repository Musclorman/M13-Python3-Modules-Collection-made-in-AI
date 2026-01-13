# MenuMaker - English Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Quick Start Guide](#quick-start-guide)
4. [Item Types](#item-types)
5. [Complete API Reference](#complete-api-reference)
6. [Advanced Examples](#advanced-examples)
7. [Internationalization (i18n)](#internationalization-i18n)
8. [Troubleshooting](#troubleshooting)

---

## Introduction

MenuMaker is a simple yet powerful module for managing menus in console and graphical applications. It provides:

- **Complete menu management** : Create menus with multiple item types
- **Diverse item types** : Text, numbers, checkboxes, radio buttons, submenus
- **Built-in internationalization** : Multilingual support via gettext
- **Easy to integrate** : Zero external dependencies, pure Python
- **Intuitive API** : Simple and clear design

### Key Features

- ✅ Dynamic menu creation
- ✅ Read/write item values
- ✅ Nested submenus
- ✅ Enable/disable items
- ✅ Controllable item visibility
- ✅ Numeric value validation
- ✅ Callbacks for actions
- ✅ Visual separator support
- ✅ Deep copy of menus
- ✅ Reset to default values

---

## Installation

### Requirements

- Python 3.6 or higher
- No external dependencies (uses stdlib)

### Usage

The MenuMaker module is located in the `MenuMaker/` directory. To import it:

```python
from MenuMaker import Menu, MenuItem, MenuSystem, ItemType
```

---

## Quick Start Guide

### Example 1: Simple Console Menu

```python
from MenuMaker import Menu

# Create a menu
menu = Menu("main", label="Main Menu")

# Add items
menu.add_action("start", "Start Game")
menu.add_action("settings", "Settings")
menu.add_action("quit", "Quit")

# Display items
for item in menu.get_visible_items():
    print(f"- {item.label}")

# Access values
menu.set_value("player_name", "Alice")
name = menu.get_value("player_name")
```

### Example 2: Menu with Various Inputs

```python
from MenuMaker import Menu, ItemType

menu = Menu("user", label="User Configuration")

# Text input
menu.add_text_input("username", "Username", default="Player1")

# Numeric input
menu.add_numeric_input("difficulty", "Difficulty Level", 
                       default=1, min_val=1, max_val=5)

# Checkbox
menu.add_checkbox("fullscreen", "Fullscreen", default=True)

# Radio buttons
menu.add_radio("language", "Language",
              options=["English", "Français", "Español"],
              default="English")

# Get all values
settings = menu.get_all_values()
print(settings)
# {'username': 'Player1', 'difficulty': 1, 'fullscreen': True, 'language': 'English'}
```

### Example 3: Submenus

```python
# Main menu
main_menu = Menu("main", label="Main Menu")

# Submenu
settings_menu = Menu("settings", label="Settings")
settings_menu.add_checkbox("sound", "Enable Sound", default=True)
settings_menu.add_numeric_input("volume", "Volume", default=50, min_val=0, max_val=100)

# Add submenu to main menu
main_menu.add_submenu("settings", "Settings", settings_menu)

# Access submenu
sub = main_menu.get_item("settings").submenu
```

### Example 4: Actions with Callbacks

```python
def on_start_click(item):
    print(f"Action triggered: {item.label}")
    return "Game started!"

menu = Menu("game", label="Game Menu")
menu.add_action("start", "Start", callback=on_start_click)

# Execute action
item = menu.get_item("start")
result = item.execute()  # Calls the callback
```

---

## Item Types

### ItemType.TEXT - Text Input

```python
menu.add_text_input("name", "Your Name", default="Anonymous")
```

### ItemType.NUMERIC - Numeric Input

```python
menu.add_numeric_input("age", "Age",
                       default=25, min_val=0, max_val=120)
```

### ItemType.CHECKBOX - Checkbox

```python
menu.add_checkbox("agree_terms", "I agree to terms", default=False)
```

### ItemType.RADIO - Radio Buttons

```python
menu.add_radio("color", "Favorite Color",
              options=["Red", "Green", "Blue"],
              default="Blue")
```

### ItemType.SUBMENU - Submenu

```python
submenu = Menu("colors", label="Colors")
menu.add_submenu("color_settings", "Color Settings", submenu)
```

### ItemType.ACTION - Action Button

```python
def callback(item):
    print("Action executed!")
    
menu.add_action("save", "Save", callback=callback)
```

### ItemType.SEPARATOR - Separator

```python
menu.add_separator()  # Visual separation line
```

---

## Complete API Reference

### MenuItem Class

Represents a single menu item.

#### Constructor

```python
MenuItem(identifier: str,
         label: str,
         item_type: ItemType = ItemType.ACTION,
         value: Any = None,
         default_value: Any = None,
         options: List[str] = None,
         callback: Callable = None,
         enabled: bool = True,
         visible: bool = True,
         description: str = "")
```

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `identifier` | str | Unique item ID |
| `label` | str | Display text |
| `item_type` | ItemType | Item type |
| `value` | Any | Current value |
| `default_value` | Any | Default value |
| `options` | List[str] | Options for radio |
| `callback` | Callable | Callback function |
| `enabled` | bool | Item active? |
| `visible` | bool | Item visible? |
| `description` | str | Help text |

#### Methods

| Method | Description |
|--------|-------------|
| `reset()` | Reset to default value |
| `execute()` | Execute callback |

---

### Menu Class

Manages a collection of menu items.

#### Constructor

```python
Menu(identifier: str,
     label: str = "",
     description: str = "",
     allow_multiple_selection: bool = False)
```

#### Item Addition Methods

```python
add_item(identifier, label, item_type, **kwargs) -> MenuItem
add_text_input(identifier, label, default="", **kwargs) -> MenuItem
add_numeric_input(identifier, label, default=0, min_val=None, max_val=None, **kwargs) -> MenuItem
add_checkbox(identifier, label, default=False, **kwargs) -> MenuItem
add_radio(identifier, label, options, default=None, **kwargs) -> MenuItem
add_submenu(identifier, label, submenu, **kwargs) -> MenuItem
add_action(identifier, label, callback, **kwargs) -> MenuItem
add_separator(identifier=None) -> MenuItem
```

#### Value Management Methods

```python
get_item(identifier) -> MenuItem
set_value(identifier, value) -> bool
get_value(identifier) -> Any
get_all_values() -> Dict[str, Any]
set_all_values(values) -> None
reset_all() -> None
```

#### Control Methods

```python
enable_item(identifier) -> bool
disable_item(identifier) -> bool
show_item(identifier) -> bool
hide_item(identifier) -> bool
get_visible_items() -> List[MenuItem]
get_enabled_items() -> List[MenuItem]
remove_item(identifier) -> bool
clear_items() -> None
copy() -> Menu
```

---

### MenuSystem Class

Complete menu management system with internationalization support.

#### Constructor

```python
MenuSystem(locale_dir: str = None, default_language: str = "en")
```

#### Methods

```python
create_menu(identifier, label="", description="") -> Menu
get_menu(identifier) -> Menu
remove_menu(identifier) -> bool
set_language(language) -> None
```

---

## Advanced Examples

### Example 1: Game Configuration

```python
from MenuMaker import Menu

# Create configuration menu
config = Menu("game_config", label="Game Configuration")

# Graphics
config.add_numeric_input("resolution_width", "Resolution (width)", 
                         default=1920, min_val=800, max_val=3840)
config.add_numeric_input("resolution_height", "Resolution (height)", 
                         default=1080, min_val=600, max_val=2160)
config.add_radio("graphics_quality", "Graphics Quality",
                options=["Low", "Medium", "High", "Ultra"],
                default="High")
config.add_checkbox("vsync", "Enable V-Sync", default=True)

# Audio
config.add_numeric_input("master_volume", "Master Volume", 
                         default=80, min_val=0, max_val=100)
config.add_numeric_input("music_volume", "Music Volume", 
                         default=70, min_val=0, max_val=100)
config.add_checkbox("enable_sound_effects", "Sound Effects", default=True)

# Get all configuration
settings = config.get_all_values()
print(settings)
```

### Example 2: Hierarchical Menu

```python
from MenuMaker import Menu

# Main menu
main = Menu("main", label="Main Menu")

# Game submenu
game_menu = Menu("game", label="Game")
game_menu.add_action("new_game", "New Game")
game_menu.add_action("load_game", "Load Game")
game_menu.add_action("save_game", "Save Game")
main.add_submenu("game", "Game", game_menu)

# Settings submenu
settings_menu = Menu("settings", label="Settings")
settings_menu.add_numeric_input("difficulty", "Difficulty", default=1, min_val=1, max_val=5)
settings_menu.add_radio("language", "Language", 
                       options=["English", "Français"],
                       default="English")
main.add_submenu("settings", "Settings", settings_menu)

# Help submenu
help_menu = Menu("help", label="Help")
help_menu.add_action("about", "About")
help_menu.add_action("controls", "Controls")
main.add_submenu("help", "Help", help_menu)

# Navigation
game_submenu = main.get_item("game").submenu
print(f"Game Menu: {len(game_submenu.items)} items")
```

### Example 3: Form Validation

```python
from MenuMaker import Menu

# Registration form
form = Menu("registration", label="Registration")

form.add_text_input("email", "Email", default="")
form.add_text_input("password", "Password", default="")
form.add_numeric_input("age", "Age", default=18, min_val=13, max_val=120)
form.add_checkbox("newsletter", "Subscribe to newsletter", default=False)

# Validation function
def validate_form(form):
    email = form.get_value("email")
    password = form.get_value("password")
    age = form.get_value("age")
    
    if not email or "@" not in email:
        return False, "Invalid email"
    if not password or len(password) < 6:
        return False, "Password too short (min 6 characters)"
    if age < 18:
        return False, "Must be at least 18 years old"
    
    return True, "Registration valid"

# Test
form.set_value("email", "test@example.com")
form.set_value("password", "secure123")
form.set_value("age", 25)

valid, message = validate_form(form)
print(f"{message}: {valid}")  # Registration valid: True
```

### Example 4: Using Callbacks

```python
from MenuMaker import Menu

menu = Menu("main", label="Main Menu")

# Define callbacks
def on_start(item):
    print(f">> {item.label} selected")
    print("Initializing game...")
    return True

def on_quit(item):
    print(f">> {item.label} selected")
    print("Goodbye!")
    return False

# Add actions with callbacks
menu.add_action("start", "Start", callback=on_start)
menu.add_action("quit", "Quit", callback=on_quit)

# Execute actions
start_item = menu.get_item("start")
result = start_item.execute()  # Prints messages

quit_item = menu.get_item("quit")
result = quit_item.execute()
```

---

## Internationalization (i18n)

MenuMaker uses `gettext` for multilingual translation support.

### Setting up Menu System with i18n

```python
from MenuMaker import MenuSystem

# Create a menu system with translation support
# Assuming translation files are in './locale/'
menu_system = MenuSystem(
    locale_dir="./locale",
    default_language="en"
)

# Create a menu
main_menu = menu_system.create_menu("main", label="Main Menu")
main_menu.add_action("start", "Start")
main_menu.add_action("quit", "Quit")

# Change language
menu_system.set_language("fr")
# Labels will be translated according to available .mo files
```

### Translation File Structure

```
MenuMaker/
├── locale/
│   ├── en/
│   │   └── LC_MESSAGES/
│   │       ├── menumaker.po     # Source translation file
│   │       └── menumaker.mo     # Compiled file
│   └── fr/
│       └── LC_MESSAGES/
│           ├── menumaker.po
│           └── menumaker.mo
```

### Creating Translation Files

1. **Extract translatable strings**:
```bash
xgettext -o locale/menumaker.pot MenuMaker/menu.py
```

2. **Create .po file for each language**:
```bash
msginit -i locale/menumaker.pot -l en -o locale/en/LC_MESSAGES/menumaker.po
msginit -i locale/menumaker.pot -l fr -o locale/fr/LC_MESSAGES/menumaker.po
```

3. **Translate strings** in the .po files
4. **Compile into .mo files**:
```bash
msgfmt -o locale/en/LC_MESSAGES/menumaker.mo locale/en/LC_MESSAGES/menumaker.po
msgfmt -o locale/fr/LC_MESSAGES/menumaker.mo locale/fr/LC_MESSAGES/menumaker.po
```

---

## Troubleshooting

### Issue: Translations not displaying

**Solution**: Check that:
1. The `locale/` directory exists
2. `.mo` files are compiled correctly
3. The `locale_dir` parameter points to the correct path
4. The language is set with `set_language()`

### Issue: "KeyError" when accessing item

**Solution**: Make sure:
1. The identifier matches exactly (case-sensitive)
2. The item was added to the menu with `add_item()`

### Issue: Numeric validation not working

**Solution**: Make sure:
1. `min_val` and `max_val` are specified at creation
2. The value is a valid number (int or float)

### Complete Error Handling Example

```python
from MenuMaker import Menu

menu = Menu("test", label="Test")
menu.add_numeric_input("age", "Age", default=25, min_val=0, max_val=120)

# Try to set invalid value
if menu.set_value("age", 150):
    print("Value accepted")
else:
    print("Value rejected (out of range)")
    # Value remains 25
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Create menu | `menu = Menu("id", label="Title")` |
| Add text | `menu.add_text_input("id", "Label")` |
| Add number | `menu.add_numeric_input("id", "Label", min_val=0, max_val=100)` |
| Add checkbox | `menu.add_checkbox("id", "Label")` |
| Add radio | `menu.add_radio("id", "Label", options=[...])` |
| Add action | `menu.add_action("id", "Label", callback=func)` |
| Add submenu | `menu.add_submenu("id", "Label", submenu)` |
| Get value | `menu.get_value("id")` |
| Set value | `menu.set_value("id", value)` |
| Get all values | `menu.get_all_values()` |
| Reset | `menu.reset_all()` |

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Author**: MenuMaker Contributors
