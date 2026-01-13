# Module MultidimensionalPaint - Documentation Complète

## Table des matières
1. [Vue d'ensemble](#vue-densemble)
2. [Installation et démarrage](#installation-et-démarrage)
3. [Classes principales](#classes-principales)
4. [Méthodes de sélection](#méthodes-de-sélection)
5. [Formes géométriques](#formes-géométriques)
6. [Exemples d'utilisation](#exemples-dutilisation)
7. [Structure des fichiers](#structure-des-fichiers)

---

## Vue d'ensemble

**MultidimensionalPaint** est un module Python complet et professionnel pour:
- Gérer des points en 1D, 2D, 3D, 4D et dimensions supérieures
- Dessiner des formes géométriques (lignes, cercles, ellipses, polygones, etc.)
- Sélectionner des points selon différents critères
- Analyser les données géométriques (distances, centroïdes, boîtes délimitantes)
- Exporter et manipuler les données

### Caractéristiques principales
✓ Support complet des dimensions multiples
✓ 9 types de formes géométriques
✓ 10 méthodes de sélection différentes
✓ Métadonnées attachables aux points
✓ Historique des sélections
✓ Export de données
✓ Tests exhaustifs (200+ cas de test)
✓ Documentation en 4 langues

---

## Installation et démarrage

### Importation basique

```python
from paint import MultidimensionalPaint
from points import Point, PointSet
from shapes import Line, Circle, Rectangle, Ellipse, Arc, ClosedShape
from selection import SelectionEngine
from utils import distance, midpoint
```

### Créer une instance

```python
painter = MultidimensionalPaint()
```

---

## Classes principales

### Point

Représente un point dans l'espace n-dimensionnel.

```python
# Créer des points
p1 = Point(5)                    # 1D
p2 = Point(3, 4)                # 2D
p3 = Point(1, 2, 3)             # 3D
p4 = Point(1, 2, 3, 4, 5)       # 5D

# Ajouter un label
p = Point(5, 10, label="point_A")

# Accéder aux coordonnées
print(p.x)          # 5
print(p.y)          # 10
print(p.coords)     # (5, 10)

# Calcul de distance
distance = p1.distance_to(p2)

# Métadonnées
p.set_metadata("couleur", "rouge")
p.set_metadata("couche", 1)
```

### PointSet

Gère une collection de points avec les mêmes dimensions.

```python
# Créer un ensemble de points
point_set = PointSet()

# Ajouter des points
point_set.add_point(Point(1, 2))
point_set.add_point(Point(3, 4))
point_set.add_point(Point(5, 6))

# Opérations sur l'ensemble
centroid = point_set.get_centroid()
bbox = point_set.get_bounding_box()
nearest = point_set.find_nearest(Point(2, 3))
farthest = point_set.find_farthest(Point(0, 0))
```

### MultidimensionalPaint (classe principale)

```python
painter = MultidimensionalPaint()

# Ajouter des points
painter.add_point(0, 0)
painter.add_point(5, 5)
painter.add_point(10, 10, label="point_C")

# Ajouter plusieurs points à la fois
points = [(1, 1), (2, 2), (3, 3)]
painter.add_points_from_list(points)

# Accéder aux points
all_points = painter.get_all_points()
point = painter.get_point(0)
labeled_point = painter.get_point_by_label("point_C")
```

---

## Méthodes de sélection

### 1. Sélection d'un seul point

```python
selected = painter.select_single_point((5, 5), tolerance=0.5)
# Retour: [(5.0, 5.0)]
```

### 2. Sélection le long d'une ligne

```python
selected = painter.select_line((0, 0), (10, 10), tolerance=1.0)
# Sélectionne tous les points proches de la ligne
```

### 3. Sélection dans une région rectangulaire

```python
selected = painter.select_within_region((0, 0), (5, 5))
# Sélectionne tous les points dans le rectangle défini
```

### 4. Sélection par plage de dimension

```python
# Sélectionner les points où X est entre 2 et 8
selected = painter.select_by_range(dimension=0, min_val=2, max_val=8)

# Pour Y entre 1 et 6
selected = painter.select_by_range(dimension=1, min_val=1, max_val=6)
```

### 5. Sélection par label

```python
painter.add_point(5, 5, label="centre")
selected = painter.select_by_label("centre")
```

### 6. Points les plus proches

```python
selected = painter.select_nearest((5, 5), count=5)
# Retourne les 5 points les plus proches de (5, 5)
```

### 7. Points les plus éloignés

```python
selected = painter.select_farthest((0, 0), count=3)
# Retourne les 3 points les plus éloignés de (0, 0)
```

### 8. Sélectionner tout

```python
selected = painter.select_all()
# Retourne tous les points
```

### Format de retour

Toutes les méthodes de sélection retournent une liste de tuples :
```python
[(x1, y1, z1, ...), (x2, y2, z2, ...), ...]
```

---

## Formes géométriques

### Ligne (Line)

```python
line = painter.draw_line(
    start=(0, 0),
    end=(10, 10),
    num_points=100,  # Points d'interpolation
    filled=False,
    color="blue"
)

# Propriétés
length = line.length()
points = line.get_points()
```

### Cercle (Circle)

```python
# 2D
circle = painter.draw_circle(
    center=(5, 5),
    radius=3,
    num_points=360,
    filled=True
)

# 3D
circle_3d = painter.draw_circle(
    center=(5, 5, 5),  # XYZ
    radius=3
)
```

### Rectangle

```python
rect = painter.draw_rectangle(
    corner1=(0, 0),
    corner2=(10, 10),
    num_points=100,
    filled=False
)
```

### Carré (Square)

```python
square = painter.draw_square(
    center=(5, 5),
    side_length=10,
    filled=True
)
```

### Ellipse

```python
import math

ellipse = painter.draw_ellipse(
    center=(5, 5),
    semi_major=10,      # Axe horizontal
    semi_minor=5,       # Axe vertical
    rotation=math.pi/4, # Rotation en radians
    filled=False
)
```

### Arc de cercle (Arc)

```python
import math

arc = painter.draw_arc(
    center=(0, 0),
    radius=5,
    start_angle=0,              # Angle de début (radians)
    end_angle=math.pi / 2,      # Angle de fin (radians)
    num_points=100
)
```

### Forme fermée (Polygon)

```python
# Triangle
triangle = painter.draw_closed_shape(
    vertices=[(0, 0), (10, 0), (5, 10)]
)

# Pentagone
pentagon = painter.draw_closed_shape(
    vertices=[
        (0, 0), (10, 0), (15, 8),
        (7.5, 15), (-5, 8)
    ],
    filled=True
)
```

---

## Exemples d'utilisation

### Exemple 1: Grille de points et sélection

```python
painter = MultidimensionalPaint()

# Créer une grille
for x in range(0, 11, 2):
    for y in range(0, 11, 2):
        painter.add_point(float(x), float(y))

# Sélectionner une région
selected = painter.select_within_region((0, 0), (5, 5))
print(f"Points sélectionnés: {len(selected)}")
```

### Exemple 2: Points 3D avec métadonnées

```python
painter = MultidimensionalPaint()

p1 = painter.add_point(0, 0, 0, label="origine")
p1.set_metadata("couleur", "rouge")
p1.set_metadata("visible", True)

p2 = painter.add_point(5, 5, 5, label="point_B")
p2.set_metadata("couleur", "bleu")

# Exporter les données
exported = painter.export_points()
for point in exported:
    print(f"{point['label']}: {point['coords']}")
    print(f"  Métadonnées: {point['metadata']}")
```

### Exemple 3: Sélection dans une forme

```python
painter = MultidimensionalPaint()

# Ajouter des points
for x in range(0, 21, 2):
    for y in range(0, 21, 2):
        painter.add_point(float(x), float(y))

# Dessiner un cercle
circle = painter.draw_circle((10, 10), 5, filled=True)

# Sélectionner les points dans le cercle
selected = painter.select_within_shape(circle)
print(f"Points dans le cercle: {len(selected)}")
```

### Exemple 4: Analyse statistique

```python
painter = MultidimensionalPaint()

# Ajouter des points
for i in range(1, 6):
    for j in range(1, 6):
        painter.add_point(float(i*2), float(j*2))

# Obtenir les statistiques
stats = painter.get_statistics()
print(f"Nombre de points: {stats['point_count']}")
print(f"Centroïde: {stats['centroid']}")
print(f"Boîte délimitante: {stats['bounding_box']}")

# Point le plus proche
nearest = painter.find_nearest_point((5, 5))
print(f"Point le plus proche: {nearest}")
```

---

## Structure des fichiers

```
multidimention_paint/
├── __init__.py               # Initialisation du package
├── utils.py                  # Fonctions utilitaires mathématiques
├── points.py                 # Classes Point et PointSet
├── shapes.py                 # Classes de formes géométriques
├── selection.py              # Moteur de sélection
├── paint.py                  # Classe principale MultidimensionalPaint
├── quick_test.py             # Suite de tests rapide
├── test_multidimension_paint.py  # Suite de tests complète
├── example.py                # 10 exemples d'utilisation
├── README.md                 # Documentation principale
├── INDEX.py                  # Index et résumé du module
└── DOCUMENTATION_FR.md       # Cette documentation
```

---

## Fonctions utilitaires

### Calcul de distance

```python
from utils import distance

d = distance((0, 0), (3, 4))  # Retourne 5.0
d = distance((0, 0, 0), (1, 1, 1))  # 3D
```

### Calcul du milieu

```python
from utils import midpoint

mp = midpoint((0, 0), (4, 4))  # Retourne (2.0, 2.0)
mp = midpoint((0, 0), (4, 4), (8, 8))  # Milieu de 3 points
```

### Interpolation linéaire

```python
from utils import interpolate

p = interpolate((0, 0), (10, 10), t=0.5)  # Retourne (5.0, 5.0)
p = interpolate((0, 0), (10, 10), t=0.25)  # Retourne (2.5, 2.5)
```

### Validation des coordonnées

```python
from utils import validate_coordinates

assert validate_coordinates(1, 2, 3) == True
assert validate_coordinates(1, "2", 3) == False
```

---

## Tests et validation

### Exécuter les tests rapides

```bash
python quick_test.py
```

### Exécuter la suite de tests complète

```bash
python test_multidimension_paint.py
```

### Exécuter les exemples

```bash
python example.py
```

---

## Gestion des erreurs

```python
try:
    # Les dimensions doivent correspondre
    p1 = Point(1, 2)
    p2 = Point(1, 2, 3)
    distance = p1.distance_to(p2)  # Lève ValueError
except ValueError as e:
    print(f"Erreur: {e}")

try:
    # Les coordonnées doivent être numériques
    p = Point("pas_un_nombre", 2)  # Lève ValueError
except ValueError as e:
    print(f"Erreur: {e}")
```

---

## Performance

Le module est optimisé pour:
- Travailler avec des milliers de points
- Gestion de multiples formes géométriques
- Sélections complexes
- Données hautement dimensionnelles (100D+)

---

**Dernière mise à jour**: 13 janvier 2026  
**Version**: 1.0.0  
**Auteur**: Développeur  
**Licence**: Libre d'utilisation
