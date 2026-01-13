# Arbre Générique - Structure d'Arbre Générique Complète

## Vue d'ensemble

`generic_tree.py` fournit une implémentation complète d'une structure d'arbre générique n-aire qui permet de stocker et manipuler **tous types de valeurs** dans une organisation hiérarchique.

## Caractéristiques Principales

✓ **Support de tous les types de valeurs** - Entiers, chaînes, flottants, dictionnaires, listes, objets personnalisés  
✓ **Structure n-aire** - Chaque nœud peut avoir un nombre illimité d'enfants  
✓ **Support des métadonnées** - Paires clé-valeur par nœud  
✓ **Modes de parcours multiples** - PRE_ORDER, POST_ORDER, LEVEL_ORDER, IN_ORDER  
✓ **Capacités de recherche** - DFS, BFS, par valeur, par prédicat  
✓ **Sérialisation JSON** - Sauvegarde/chargement natif JSON  
✓ **Opérations fonctionnelles** - Map, filter, reduce, apply  
✓ **Analyse d'arbre** - Hauteur, profondeur, vérification d'équilibre, extraction de feuilles  
✓ **Manipulation d'arbre** - Tri, inversion, clonage  

## Classes

### TreeNode

Représente un seul nœud dans l'arbre.

```python
node = TreeNode(value=5)
node.add_child(10)
node.set_metadata("couleur", "rouge")
```

#### Méthodes Principales

| Méthode | Description |
|---------|-------------|
| `add_child(value)` | Ajouter un enfant et retourner le nœud enfant |
| `add_node(node)` | Ajouter un nœud existant comme enfant |
| `remove_child(node)` | Supprimer un enfant |
| `get_child_by_index(index)` | Obtenir enfant par index |
| `get_child_by_value(value)` | Obtenir enfant par valeur |
| `get_children_by_predicate(func)` | Obtenir enfants correspondant au prédicat |
| `child_count()` | Nombre d'enfants |
| `is_leaf()` | Vérifier si c'est une feuille |
| `is_root()` | Vérifier si c'est la racine |
| `get_depth()` | Obtenir la profondeur depuis la racine |
| `get_path_to_root()` | Obtenir le chemin vers la racine |
| `set_metadata(key, value)` | Définir métadonnée |
| `get_metadata(key, default=None)` | Obtenir métadonnée |
| `has_metadata(key)` | Vérifier si métadonnée existe |
| `clear_metadata()` | Effacer toutes les métadonnées |
| `clone(deep=True)` | Cloner le nœud |

### Tree

Gère la structure d'arbre complète.

```python
tree = Tree(root_value="Racine")
child = tree.add_child(tree.root, "Enfant")
```

#### Méthodes Principales

| Méthode | Description |
|--------|-------------|
| `add_child(parent, value)` | Ajouter enfant au parent |
| `add_node(parent, node)` | Ajouter nœud existant |
| `remove_child(parent, child)` | Supprimer enfant |
| `get_node_by_value(value)` | Trouver nœud par valeur |
| `get_nodes_by_predicate(func)` | Trouver nœuds par prédicat |
| `get_all_leaf_nodes()` | Obtenir toutes les feuilles |
| `get_all_nodes()` | Obtenir tous les nœuds |
| `get_node_count()` | Nombre total de nœuds |
| `get_height()` | Hauteur de l'arbre |
| `traverse(mode, start=None)` | Parcourir l'arbre |
| `to_dict()` | Convertir en dictionnaire |
| `to_json(indent=None)` | Convertir en JSON |
| `from_dict(data)` | Créer à partir de dictionnaire |
| `from_json(json_str)` | Créer à partir de JSON |
| `save_to_file(filepath)` | Sauvegarder en fichier JSON |
| `load_from_file(filepath)` | Charger depuis fichier JSON |
| `map(func)` | Appliquer fonction à tous les nœuds |
| `filter(predicate)` | Créer arbre filtré |
| `find_path(value)` | Trouver chemin vers valeur |
| `get_common_ancestor(n1, n2)` | Trouver ancêtre commun |
| `print_tree()` | Imprimer arbre formaté |
| `clear()` | Effacer l'arbre |
| `reverse_children()` | Inverser ordre des enfants |
| `sort_children(key=None)` | Trier les enfants |
| `depth_first_search(value)` | Recherche DFS |
| `breadth_first_search(value)` | Recherche BFS |
| `apply(func)` | Appliquer fonction à tous les nœuds |
| `reduce(func, initial=None)` | Réduire à une seule valeur |
| `get_siblings(node)` | Obtenir nœuds frères |
| `get_subtree_height(node)` | Obtenir hauteur du sous-arbre |
| `is_balanced()` | Vérifier si équilibré |

## Exemples d'Utilisation

### Créer un Arbre

```python
tree = Tree(root_value="Racine")
child1 = tree.add_child(tree.root, "Enfant 1")
child2 = tree.add_child(tree.root, "Enfant 2")
grandchild = tree.add_child(child1, "Petit-enfant")

tree.print_tree()
```

### Recherche

```python
# Par valeur
node = tree.get_node_by_value("Petit-enfant")

# Par prédicat
string_nodes = tree.get_nodes_by_predicate(lambda x: isinstance(x, str))

# DFS/BFS
node = tree.depth_first_search("Enfant 1")
```

### Sérialisation

```python
# Sauvegarder
tree.save_to_file("mon_arbre.json")

# Charger
tree = Tree.load_from_file("mon_arbre.json")
```

## Cas d'Usage Réels

1. Systèmes de fichiers
2. Hiérarchies organisationnelles
3. Structures de menu
4. Arbres DOM
5. Hiérarchies de catégories
6. Graphes de dépendances

## Auteur

Assistant IA - 12 janvier 2026
