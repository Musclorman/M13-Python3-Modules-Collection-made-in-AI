# MultiDimTable - Documentation Complète

## Table des Matières
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Guide de Démarrage Rapide](#guide-de-démarrage-rapide)
4. [Référence API](#référence-api)
5. [Exemples Avancés](#exemples-avancés)
6. [Dépannage](#dépannage)

---

## Introduction

**MultiDimTable** est un module Python léger et intuitif pour gérer les tableaux multidimensionnels (1D, 2D, 3D et n-dimensions). Il est conçu pour être facile à importer et utiliser dans n'importe quel projet, bibliothèque console ou graphique.

### Caractéristiques Principales

- ✅ Support natif pour tableaux 1D, 2D, 3D et n-dimensionnels
- ✅ Création facile avec `MultiDimTable.create()`, `zeros()`, `ones()`
- ✅ Accès aux éléments par index simple ou tuple
- ✅ Remodelage (reshape) et aplatissement (flatten)
- ✅ Transposition pour tableaux 2D
- ✅ Concaténation et division de tableaux
- ✅ Empilage (stacking) de tableaux
- ✅ Conversion vers listes Python
- ✅ Itération sur les éléments
- ✅ Opérations statistiques (sum, mean, min, max)
- ✅ Application de fonctions personnalisées

---

## Installation

### Depuis le dossier du projet

```python
from Multidimention_table import MultiDimTable
```

Ou directement depuis le chemin :

```python
import sys
sys.path.insert(0, '/chemin/vers/Multidimention_table')
from __init__ import MultiDimTable
```

---

## Guide de Démarrage Rapide

### Création de Tableaux

```python
from Multidimention_table import MultiDimTable

# Créer un tableau 1D
t1d = MultiDimTable([1, 2, 3, 4, 5])
print(t1d.shape)  # (5,)

# Créer un tableau 2D
t2d = MultiDimTable([[1, 2, 3], [4, 5, 6]])
print(t2d.shape)  # (2, 3)

# Créer un tableau 3D
t3d = MultiDimTable.create((2, 3, 4), fill=0)
print(t3d.shape)  # (2, 3, 4)

# Créer avec des zéros ou des uns
zeros_table = MultiDimTable.zeros((3, 3))
ones_table = MultiDimTable.ones((2, 4))
```

### Accès aux Éléments

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])

# Accès 1D (si applicable)
value = t[1]  # Retourne [4, 5, 6]

# Accès 2D
value = t[0, 1]  # Retourne 2
value = t[1, 2]  # Retourne 6

# Accès 3D
t3d = MultiDimTable.create((2, 2, 2), fill=5)
value = t3d[0, 1, 1]  # Retourne 5

# Modification
t[0, 0] = 99
print(t[0, 0])  # 99
```

### Remodelage et Aplatissement

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])

# Aplatir en 1D
flat = t.flatten()
print(flat.shape)  # (6,)
print(flat.to_list())  # [1, 2, 3, 4, 5, 6]

# Remodelage
reshaped = flat.reshape((3, 2))
print(reshaped.shape)  # (3, 2)
print(reshaped.to_list())  # [[1, 2], [3, 4], [5, 6]]

# Remodelage 3D
reshaped_3d = flat.reshape((2, 3, 1))
print(reshaped_3d.shape)  # (2, 3, 1)
```

### Concaténation et Division

```python
t1 = MultiDimTable([[1, 2], [3, 4]])
t2 = MultiDimTable([[5, 6]])

# Concaténer
concatenated = t1.concatenate(t2, axis=0)
print(concatenated.shape)  # (3, 2)
print(concatenated.to_list())  # [[1, 2], [3, 4], [5, 6]]

# Diviser
t = MultiDimTable([[1, 2, 3, 4], [5, 6, 7, 8]])
parts = t.split(2, axis=0)
print(len(parts))  # 2
print(parts[0].shape)  # (1, 4)
print(parts[1].shape)  # (1, 4)
```

### Empilage

```python
t1 = MultiDimTable([1, 2, 3])
t2 = MultiDimTable([4, 5, 6])
t3 = MultiDimTable([7, 8, 9])

# Empiler
stacked = t1.stack([t2, t3], axis=0)
print(stacked.shape)  # (3, 3)
print(stacked.to_list())  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Transposition

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
print(t.shape)  # (2, 3)

transposed = t.transpose()
print(transposed.shape)  # (3, 2)
print(transposed.to_list())  # [[1, 4], [2, 5], [3, 6]]
```

### Itération et Opérations Statistiques

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])

# Itération
for value in t.iterate():
    print(value)  # Affiche 1, 2, 3, 4, 5, 6

# Statistiques
print(t.sum())   # 21
print(t.mean())  # 3.5
print(t.min())   # 1
print(t.max())   # 6

# Application de fonction
t2 = t.apply(lambda x: x ** 2)
print(t2.to_list())  # [[1, 4, 9], [16, 25, 36]]
```

---

## Référence API

### Classe MultiDimTable

#### Constructeurs

| Méthode | Description | Exemple |
|---------|-------------|---------|
| `MultiDimTable(data)` | Crée un tableau à partir de listes imbriquées | `MultiDimTable([[1, 2], [3, 4]])` |
| `create(shape, fill)` | Crée un tableau avec une dimension donnée, rempli avec une valeur | `MultiDimTable.create((2, 3), fill=0)` |
| `zeros(shape)` | Crée un tableau rempli de zéros | `MultiDimTable.zeros((3, 3))` |
| `ones(shape)` | Crée un tableau rempli de uns | `MultiDimTable.ones((2, 4))` |

#### Propriétés

| Propriété | Type | Description |
|-----------|------|-------------|
| `shape` | Tuple[int, ...] | Dimensions du tableau |
| `ndim` | int | Nombre de dimensions |
| `size` | int | Nombre total d'éléments |

#### Accès aux Données

| Méthode | Description | Exemple |
|---------|-------------|---------|
| `__getitem__(index)` | Accès à un élément ou ligne | `t[0, 1]` |
| `__setitem__(index, value)` | Modification d'un élément | `t[0, 1] = 10` |
| `to_list()` | Conversion en listes imbriquées | `t.to_list()` |
| `to_flat_list()` | Conversion en liste plate | `t.to_flat_list()` |

#### Transformations

| Méthode | Description | Retour |
|---------|-------------|--------|
| `flatten()` | Aplatir en 1D | MultiDimTable |
| `reshape(shape)` | Remodelage | MultiDimTable |
| `transpose()` | Transposition (2D) | MultiDimTable |
| `copy()` | Copie profonde | MultiDimTable |
| `apply(func)` | Appliquer une fonction | MultiDimTable |

#### Opérations de Fusion/Division

| Méthode | Description | Retour |
|---------|-------------|--------|
| `concatenate(other, axis)` | Concaténer avec un autre tableau | MultiDimTable |
| `split(sections, axis)` | Diviser en parties | List[MultiDimTable] |
| `stack(tables, axis)` | Empiler des tableaux | MultiDimTable |

#### Itération et Agrégation

| Méthode | Description | Retour |
|---------|-------------|--------|
| `iterate()` | Itérateur sur tous les éléments | Iterator[Any] |
| `sum()` | Somme de tous les éléments | Union[int, float] |
| `mean()` | Moyenne arithmétique | float |
| `min()` | Élément minimum | Any |
| `max()` | Élément maximum | Any |

---

## Exemples Avancés

### Exemple 1: Manipulation de Matrices 3D

```python
# Créer une matrice 3D pour représenter des images RGB
images = MultiDimTable.create((4, 32, 32), fill=0)  # 4 images de 32x32

# Modifier un pixel dans la première image
images[0, 10, 15] = 255

# Aplatir toutes les images
flat_images = images.flatten()
print(f"Total de pixels: {flat_images.size}")  # 4096

# Remodelage pour créer des données d'entraînement
reshaped = flat_images.reshape((4, 1024))
print(reshaped.shape)  # (4, 1024) - batch x features
```

### Exemple 2: Traitement de Données Tabellaires

```python
# Données de ventes: produit x mois x année
sales = MultiDimTable([
    [[100, 110, 120], [150, 160, 170]],  # Produit 1
    [[200, 210, 220], [250, 260, 270]],  # Produit 2
])

print(sales.shape)  # (2, 2, 3)

# Total des ventes par produit
for i in range(sales.shape[0]):
    product_sales = MultiDimTable(sales._data[i]).flatten()
    print(f"Produit {i+1}: {product_sales.sum()} unités")

# Augmentation des ventes de 10%
sales_augmented = sales.apply(lambda x: int(x * 1.1))
```

### Exemple 3: Batch Processing

```python
# Diviser un grand dataset en batches
full_data = MultiDimTable.create((1000, 128), fill=1)

batches = full_data.split(10, axis=0)
print(f"Nombre de batches: {len(batches)}")
print(f"Taille d'un batch: {batches[0].shape}")  # (100, 128)

# Traiter chaque batch
for batch in batches:
    normalized = batch.apply(lambda x: (x - 0.5) / 0.5)
    # Traitement du batch normalisé
```

### Exemple 4: Fusion de Données

```python
# Fusionner plusieurs sources de données
data_source_1 = MultiDimTable([[1, 2, 3], [4, 5, 6]])
data_source_2 = MultiDimTable([[7, 8, 9]])
data_source_3 = MultiDimTable([[10, 11, 12]])

# Concaténation
merged = data_source_1.concatenate(data_source_2, axis=0)
merged = merged.concatenate(data_source_3, axis=0)

print(merged.shape)  # (4, 3)
print(f"Total d'éléments: {merged.size}")  # 12
```

---

## Dépannage

### Erreurs Communes

#### ShapeError: Inconsistent dimensions

```python
# ❌ Erreur - dimensions inconsistentes
try:
    t = MultiDimTable([[1, 2], [3, 4, 5]])  # Lignes de tailles différentes
except ShapeError as e:
    print(f"Erreur: {e}")

# ✅ Correct
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])  # Lignes uniformes
```

#### IndexError_: Index out of bounds

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])

# ❌ Erreur - index hors limites
try:
    value = t[5, 5]  # Hors limites
except IndexError_ as e:
    print(f"Erreur: {e}")

# ✅ Correct
value = t[0, 0]  # Valide
value = t[1, 2]  # Valide
```

#### ShapeError: Cannot reshape

```python
t = MultiDimTable([1, 2, 3, 4, 5])  # 5 éléments

# ❌ Erreur - 5 éléments ne peuvent pas former une matrice 2x3 (6 éléments)
try:
    t2d = t.reshape((2, 3))
except ShapeError as e:
    print(f"Erreur: {e}")

# ✅ Correct
t2d = t.reshape((5, 1))  # ou (1, 5)
```

---

## Notes de Performance

- Pour les très grandes dimensions (>10⁷ éléments), considérez NumPy pour de meilleures performances.
- MultiDimTable utilise des listes Python imbriquées, adaptées aux tableaux de taille petite à moyenne.
- Les opérations de copie (`copy()`) créent des copies profondes - utilisez avec prudence sur de grands tableaux.

---

**MultiDimTable v1.0.0** | Auteur: MIDInosaure | Licence: MIT
