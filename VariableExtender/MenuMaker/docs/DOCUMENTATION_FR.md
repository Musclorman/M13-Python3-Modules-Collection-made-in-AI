# MenuMaker - Documentation Française

## Table des matières

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Guide de démarrage rapide](#guide-de-démarrage-rapide)
4. [Types d'éléments](#types-déléments)
5. [Référence complète de l'API](#référence-complète-de-lapi)
6. [Exemples avancés](#exemples-avancés)
7. [Internationalisation (i18n)](#internationalisation-i18n)
8. [Dépannage](#dépannage)

---

## Introduction

MenuMaker est un module simple mais puissant pour gérer des menus dans des applications console ou graphiques. Il fournit:

- **Gestion de menus complète** : Créez des menus avec plusieurs types d'éléments
- **Types d'éléments variés** : Texte, nombres, cases à cocher, boutons radio, sous-menus
- **Internationalisation intégrée** : Support multilingue via gettext
- **Facilement intégrable** : Zéro dépendance externe, pur Python
- **API intuitive** : Conception simple et claire

### Caractéristiques principales

- ✅ Création de menus dynamiques
- ✅ Lecture/écriture de valeurs d'éléments
- ✅ Sous-menus imbriqués
- ✅ Activation/désactivation d'éléments
- ✅ Visibilité contrôlable des éléments
- ✅ Validation des valeurs numériques
- ✅ Callbacks pour les actions
- ✅ Support des séparateurs visuels
- ✅ Copie profonde de menus
- ✅ Réinitialisation aux valeurs par défaut

---

## Installation

### Prérequis

- Python 3.6 ou supérieur
- Pas de dépendances externes (utilise la stdlib)

### Utilisation

Le module MenuMaker se trouve dans le répertoire `MenuMaker/`. Pour l'importer:

```python
from MenuMaker import Menu, MenuItem, MenuSystem, ItemType
```

---

## Guide de démarrage rapide

### Exemple 1 : Menu simple en console

```python
from MenuMaker import Menu

# Créer un menu
menu = Menu("main", label="Menu Principal")

# Ajouter des éléments
menu.add_action("start", "Démarrer le jeu")
menu.add_action("settings", "Paramètres")
menu.add_action("quit", "Quitter")

# Afficher les éléments
for item in menu.get_visible_items():
    print(f"- {item.label}")

# Accéder aux valeurs
menu.set_value("player_name", "Alice")
name = menu.get_value("player_name")
```

### Exemple 2 : Menu avec diverses entrées

```python
from MenuMaker import Menu, ItemType

menu = Menu("user", label="Configuration utilisateur")

# Éléments de texte
menu.add_text_input("username", "Nom d'utilisateur", default="Joueur1")

# Éléments numériques
menu.add_numeric_input("level", "Niveau de difficulté", 
                       default=1, min_val=1, max_val=5)

# Cases à cocher
menu.add_checkbox("fullscreen", "Plein écran", default=True)

# Boutons radio
menu.add_radio("language", "Langue",
              options=["Français", "English", "Español"],
              default="Français")

# Récupérer toutes les valeurs
settings = menu.get_all_values()
print(settings)
# {'username': 'Joueur1', 'level': 1, 'fullscreen': True, 'language': 'Français'}
```

### Exemple 3 : Sous-menus

```python
# Menu principal
main_menu = Menu("main", label="Menu Principal")

# Sous-menu
settings_menu = Menu("settings", label="Paramètres")
settings_menu.add_checkbox("sound", "Activer le son", default=True)
settings_menu.add_numeric_input("volume", "Volume", default=50, min_val=0, max_val=100)

# Ajouter le sous-menu au menu principal
main_menu.add_submenu("settings", "Paramètres", settings_menu)

# Accéder au sous-menu
sub = main_menu.get_menu("settings")
```

### Exemple 4 : Actions avec callbacks

```python
def on_start_click(item):
    print(f"Action lancée: {item.label}")
    return "Game started!"

menu = Menu("game", label="Menu Jeu")
menu.add_action("start", "Démarrer", callback=on_start_click)

# Exécuter l'action
item = menu.get_item("start")
result = item.execute()  # Appelle le callback
```

---

## Types d'éléments

### ItemType.TEXT - Entrée de texte

```python
menu.add_text_input("name", "Votre nom", default="Anonyme")
```

### ItemType.NUMERIC - Entrée numérique

```python
menu.add_numeric_input("age", "Âge",
                       default=25, min_val=0, max_val=120)
```

### ItemType.CHECKBOX - Case à cocher

```python
menu.add_checkbox("agree_terms", "J'accepte les conditions", default=False)
```

### ItemType.RADIO - Boutons radio

```python
menu.add_radio("color", "Couleur préférée",
              options=["Rouge", "Vert", "Bleu"],
              default="Bleu")
```

### ItemType.SUBMENU - Sous-menu

```python
submenu = Menu("colors", label="Couleurs")
menu.add_submenu("color_settings", "Paramètres de couleur", submenu)
```

### ItemType.ACTION - Bouton d'action

```python
def callback(item):
    print("Action exécutée!")
    
menu.add_action("save", "Sauvegarder", callback=callback)
```

### ItemType.SEPARATOR - Séparateur

```python
menu.add_separator()  # Ligne de séparation visuelle
```

---

## Référence complète de l'API

### Classe MenuItem

Représente un élément de menu individuel.

#### Constructeur

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

#### Propriétés

| Propriété | Type | Description |
|-----------|------|-------------|
| `identifier` | str | ID unique de l'élément |
| `label` | str | Texte affiché |
| `item_type` | ItemType | Type d'élément |
| `value` | Any | Valeur actuelle |
| `default_value` | Any | Valeur par défaut |
| `options` | List[str] | Options pour radio |
| `callback` | Callable | Fonction de rappel |
| `enabled` | bool | Élément actif ? |
| `visible` | bool | Élément visible ? |
| `description` | str | Texte d'aide |

#### Méthodes

| Méthode | Description |
|---------|-------------|
| `reset()` | Réinitialiser à la valeur par défaut |
| `execute()` | Exécuter le callback |

---

### Classe Menu

Gère une collection d'éléments de menu.

#### Constructeur

```python
Menu(identifier: str,
     label: str = "",
     description: str = "",
     allow_multiple_selection: bool = False)
```

#### Méthodes d'ajout d'éléments

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

#### Méthodes de gestion des valeurs

```python
get_item(identifier) -> MenuItem
set_value(identifier, value) -> bool
get_value(identifier) -> Any
get_all_values() -> Dict[str, Any]
set_all_values(values) -> None
reset_all() -> None
```

#### Méthodes de contrôle

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

### Classe MenuSystem

Système complet de gestion des menus avec support de l'internationalisation.

#### Constructeur

```python
MenuSystem(locale_dir: str = None, default_language: str = "en")
```

#### Méthodes

```python
create_menu(identifier, label="", description="") -> Menu
get_menu(identifier) -> Menu
remove_menu(identifier) -> bool
set_language(language) -> None
```

---

## Exemples avancés

### Exemple 1 : Configuration de jeu

```python
from MenuMaker import Menu

# Créer le menu de configuration
config = Menu("game_config", label="Configuration du jeu")

# Graphiques
config.add_numeric_input("resolution_width", "Résolution (largeur)", 
                         default=1920, min_val=800, max_val=3840)
config.add_numeric_input("resolution_height", "Résolution (hauteur)", 
                         default=1080, min_val=600, max_val=2160)
config.add_radio("graphics_quality", "Qualité graphique",
                options=["Basse", "Moyenne", "Haute", "Ultra"],
                default="Haute")
config.add_checkbox("vsync", "V-Sync activé", default=True)

# Audio
config.add_numeric_input("master_volume", "Volume maître", 
                         default=80, min_val=0, max_val=100)
config.add_numeric_input("music_volume", "Volume musique", 
                         default=70, min_val=0, max_val=100)
config.add_checkbox("enable_sound_effects", "Effets sonores", default=True)

# Récupérer la configuration
settings = config.get_all_values()
print(settings)
```

### Exemple 2 : Menu hiérarchique

```python
from MenuMaker import Menu

# Menu principal
main = Menu("main", label="Menu Principal")

# Sous-menu Jeu
game_menu = Menu("game", label="Jeu")
game_menu.add_action("new_game", "Nouvelle partie")
game_menu.add_action("load_game", "Charger une partie")
game_menu.add_action("save_game", "Sauvegarder")
main.add_submenu("game", "Jeu", game_menu)

# Sous-menu Paramètres
settings_menu = Menu("settings", label="Paramètres")
settings_menu.add_numeric_input("difficulty", "Difficulté", default=1, min_val=1, max_val=5)
settings_menu.add_radio("language", "Langue", 
                       options=["Français", "English"],
                       default="Français")
main.add_submenu("settings", "Paramètres", settings_menu)

# Sous-menu Aide
help_menu = Menu("help", label="Aide")
help_menu.add_action("about", "À propos")
help_menu.add_action("controls", "Contrôles")
main.add_submenu("help", "Aide", help_menu)

# Navigation
game_submenu = main.get_item("game").submenu
print(f"Menu Jeu: {len(game_submenu.items)} éléments")
```

### Exemple 3 : Validation de formulaire

```python
from MenuMaker import Menu

# Formulaire d'inscription
form = Menu("registration", label="Inscription")

form.add_text_input("email", "Email", default="")
form.add_text_input("password", "Mot de passe", default="")
form.add_numeric_input("age", "Âge", default=18, min_val=13, max_val=120)
form.add_checkbox("newsletter", "S'abonner à la newsletter", default=False)

# Validation
def validate_form(form):
    email = form.get_value("email")
    password = form.get_value("password")
    age = form.get_value("age")
    
    if not email or "@" not in email:
        return False, "Email invalide"
    if not password or len(password) < 6:
        return False, "Mot de passe trop court (min 6 caractères)"
    if age < 18:
        return False, "Vous devez avoir au moins 18 ans"
    
    return True, "Inscription valide"

# Tester
form.set_value("email", "test@example.com")
form.set_value("password", "secure123")
form.set_value("age", 25)

valid, message = validate_form(form)
print(f"{message} : {valid}")  # Inscription valide : True
```

### Exemple 4 : Utilisation des callbacks

```python
from MenuMaker import Menu

menu = Menu("main", label="Menu Principal")

# Définir des callbacks
def on_start(item):
    print(f">> {item.label} sélectionné")
    print("Initialisation du jeu...")
    return True

def on_quit(item):
    print(f">> {item.label} sélectionné")
    print("Au revoir!")
    return False

# Ajouter des actions avec callbacks
menu.add_action("start", "Démarrer", callback=on_start)
menu.add_action("quit", "Quitter", callback=on_quit)

# Exécuter les actions
start_item = menu.get_item("start")
result = start_item.execute()  # Affiche les messages

quit_item = menu.get_item("quit")
result = quit_item.execute()
```

---

## Internationalisation (i18n)

MenuMaker utilise `gettext` pour la traduction multilingue.

### Configuration du système de menu avec i18n

```python
from MenuMaker import MenuSystem

# Créer un système de menu avec support de traduction
# Supposant que les fichiers de traduction sont dans './locale/'
menu_system = MenuSystem(
    locale_dir="./locale",
    default_language="fr"
)

# Créer un menu
main_menu = menu_system.create_menu("main", label="Menu Principal")
main_menu.add_action("start", "Démarrer")
main_menu.add_action("quit", "Quitter")

# Changer de langue
menu_system.set_language("en")
# Les étiquettes seront traduites selon les fichiers .mo disponibles
```

### Structure des fichiers de traduction

```
MenuMaker/
├── locale/
│   ├── fr/
│   │   └── LC_MESSAGES/
│   │       ├── menumaker.po     # Fichier source de traduction
│   │       └── menumaker.mo     # Fichier compilé
│   └── en/
│       └── LC_MESSAGES/
│           ├── menumaker.po
│           └── menumaker.mo
```

### Créer des fichiers de traduction

1. **Extraire les chaînes à traduire** :
```bash
xgettext -o locale/menumaker.pot MenuMaker/menu.py
```

2. **Créer un fichier .po pour chaque langue** :
```bash
msginit -i locale/menumaker.pot -l fr -o locale/fr/LC_MESSAGES/menumaker.po
msginit -i locale/menumaker.pot -l en -o locale/en/LC_MESSAGES/menumaker.po
```

3. **Traduire les chaînes** dans les fichiers .po
4. **Compiler en fichiers .mo** :
```bash
msgfmt -o locale/fr/LC_MESSAGES/menumaker.mo locale/fr/LC_MESSAGES/menumaker.po
msgfmt -o locale/en/LC_MESSAGES/menumaker.mo locale/en/LC_MESSAGES/menumaker.po
```

---

## Dépannage

### Problème : Les traductions ne s'affichent pas

**Solution** : Vérifiez que:
1. Le répertoire `locale/` existe
2. Les fichiers `.mo` sont compilés correctement
3. Le paramètre `locale_dir` pointe vers le bon chemin
4. La langue est définie avec `set_language()`

### Problème : Erreur "KeyError" lors de l'accès à un élément

**Solution** : Assurez-vous que:
1. L'identifiant utilisé correspond exactement (sensible à la casse)
2. L'élément a bien été ajouté au menu avec `add_item()`

### Problème : La validation numérique ne fonctionne pas

**Solution** : Assurez-vous que:
1. `min_val` et `max_val` sont spécifiés lors de la création
2. La valeur est bien un nombre (int ou float)

### Exemple complet de gestion d'erreurs

```python
from MenuMaker import Menu

menu = Menu("test", label="Test")
menu.add_numeric_input("age", "Âge", default=25, min_val=0, max_val=120)

# Tentative de définir une valeur invalide
if menu.set_value("age", 150):
    print("Valeur acceptée")
else:
    print("Valeur rejetée (hors limites)")
    # La valeur n'a pas été modifiée, elle reste 25
```

---

## Résumé rapide

| Tâche | Commande |
|-------|----------|
| Créer un menu | `menu = Menu("id", label="Titre")` |
| Ajouter du texte | `menu.add_text_input("id", "Label")` |
| Ajouter un nombre | `menu.add_numeric_input("id", "Label", min_val=0, max_val=100)` |
| Ajouter checkbox | `menu.add_checkbox("id", "Label")` |
| Ajouter radio | `menu.add_radio("id", "Label", options=[...])` |
| Ajouter action | `menu.add_action("id", "Label", callback=func)` |
| Ajouter sous-menu | `menu.add_submenu("id", "Label", submenu)` |
| Obtenir valeur | `menu.get_value("id")` |
| Définir valeur | `menu.set_value("id", value)` |
| Obtenir toutes | `menu.get_all_values()` |
| Réinitialiser | `menu.reset_all()` |

---

**Version**: 1.0.0  
**Dernière mise à jour**: 2024  
**Auteur**: MenuMaker Contributors
