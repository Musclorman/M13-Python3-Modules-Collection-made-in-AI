# MultidimensionalPaint Module

**Language versions:** [English](#english) | [Français](#français) | [Español](#español) | [Deutsch](#deutsch)

---

## English

### Overview

MultidimensionalPaint is a comprehensive Python module for working with points and geometric shapes in multidimensional spaces (1D, 2D, 3D, 4D, and beyond). It provides powerful tools for:

- **Point Management**: Create and manipulate points in any number of dimensions
- **Geometric Shapes**: Draw lines, circles, rectangles, squares, ellipses, arcs, and custom closed shapes
- **Point Selection**: Select points using various criteria (single point, lines, regions, shapes, metadata, etc.)
- **Analysis**: Calculate distances, centroids, bounding boxes, and other geometric properties
- **Data Export**: Export points and shapes for further processing

### Installation

```python
from multidimention_paint import MultidimensionalPaint, Point, PointSet
```

### Quick Start

```python
# Create a painter instance
painter = MultidimensionalPaint()

# Add points
painter.add_point(0, 0)
painter.add_point(5, 5)
painter.add_point(10, 10)

# Draw shapes
painter.draw_circle((5, 5), 3)
painter.draw_rectangle((0, 0), (10, 10))

# Select points
selected = painter.select_within_region((0, 0), (5, 5))
print(f"Selected {len(selected)} points")

# Get statistics
stats = painter.get_statistics()
print(stats)
```

### Core Classes

#### Point

Represents a point in n-dimensional space.

```python
# Create points in various dimensions
p1d = Point(5)
p2d = Point(3, 4)
p3d = Point(1, 2, 3)
p4d = Point(1, 2, 3, 4)
p5d = Point(1, 2, 3, 4, 5)

# Access coordinates
print(p2d.x)        # 3
print(p2d.y)        # 4
print(p3d.z)        # 3

# Calculate distance
distance = p1.distance_to(p2)

# Work with metadata
p2d.set_metadata("color", "red")
p2d.set_metadata("visible", True)
```

#### PointSet

Manages a collection of points with the same dimensions.

```python
point_set = PointSet()

# Add points
point_set.add_point(Point(1, 2))
point_set.add_point(Point(3, 4))

# Find nearest/farthest
nearest = point_set.find_nearest(Point(1.5, 2))
farthest = point_set.find_farthest(Point(0, 0))

# Get bounding box
bbox = point_set.get_bounding_box()

# Get centroid
centroid = point_set.get_centroid()
```

#### MultidimensionalPaint (Main Class)

The main interface for drawing and selecting.

```python
painter = MultidimensionalPaint()

# Point operations
painter.add_point(0, 0)
painter.add_point(1, 2, 3)
points = painter.get_all_points()

# Shape drawing
painter.draw_line((0, 0), (10, 10))
painter.draw_circle((5, 5), 3, filled=True)
painter.draw_rectangle((0, 0), (10, 10))
painter.draw_ellipse((5, 5), 6, 4)

# Point selection
selected = painter.select_single_point((5, 5), tolerance=0.1)
selected = painter.select_within_region((0, 0), (5, 5))
selected = painter.select_nearest((5, 5), count=3)

# Analysis
bbox = painter.get_bounding_box()
centroid = painter.get_centroid()
stats = painter.get_statistics()

# Export
points_data = painter.export_points()
shapes_data = painter.export_shapes()
```

### Shape Types

#### Line

A line segment between two points.

```python
line = painter.draw_line((0, 0), (10, 10), num_points=100, filled=False)
length = line.length()
points = line.get_points()
```

#### Circle

A circle in 2D or 3D space.

```python
# 2D circle
circle = painter.draw_circle((5, 5), radius=3, num_points=360)

# 3D circle (in XY plane at Z=5)
circle_3d = painter.draw_circle((5, 5, 5), radius=3)

# Filled circle
circle_filled = painter.draw_circle((5, 5), radius=3, filled=True)
```

#### Rectangle

A rectangle defined by two opposite corners.

```python
rect = painter.draw_rectangle((0, 0), (10, 10), filled=False)
rect_filled = painter.draw_rectangle((0, 0), (10, 10), filled=True)
```

#### Square

A square defined by center and side length.

```python
square = painter.draw_square((5, 5), side_length=10)
```

#### Ellipse

An ellipse with semi-major and semi-minor axes.

```python
ellipse = painter.draw_ellipse(
    (5, 5),           # center
    semi_major=10,    # horizontal
    semi_minor=5,     # vertical
    rotation=0        # rotation in radians
)
```

#### Arc

A circular arc segment.

```python
import math

arc = painter.draw_arc(
    (0, 0),                    # center
    radius=5,
    start_angle=0,             # radians
    end_angle=math.pi / 2,     # quarter circle
    num_points=100
)
```

#### ClosedShape

A custom polygon shape defined by vertices.

```python
# Triangle
triangle = painter.draw_closed_shape([
    (0, 0),
    (10, 0),
    (5, 10)
])

# Pentagon
pentagon = painter.draw_closed_shape([
    (0, 0), (10, 0), (15, 8),
    (7.5, 15), (-5, 8)
])
```

### Point Selection Methods

#### Select Single Point

```python
selected = painter.select_single_point((5, 5), tolerance=0.1)
```

#### Select Along Line

```python
selected = painter.select_line((0, 0), (10, 10), tolerance=0.5)
```

#### Select Within Region

```python
selected = painter.select_within_region((0, 0), (5, 5))
```

#### Select Within Shape

```python
circle = painter.draw_circle((5, 5), 3)
selected = painter.select_within_shape(circle)
```

#### Select by Dimension Range

```python
# Select points where X coordinate is between 2 and 8
selected = painter.select_by_range(dimension=0, min_val=2, max_val=8)
```

#### Select Nearest Points

```python
selected = painter.select_nearest((5, 5), count=5)
```

#### Select Farthest Points

```python
selected = painter.select_farthest((0, 0), count=3)
```

#### Select by Label

```python
point = painter.add_point(5, 5, label="origin")
selected = painter.select_by_label("origin")
```

### Selection Return Format

All selection methods return a list of lists containing coordinates:

```python
selection = painter.select_within_region((0, 0), (10, 10))
# Result: [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0), ...]
```

### Utility Functions

```python
from multidimention_paint import distance, midpoint, normalize_vector

# Calculate distance
d = distance((0, 0), (3, 4))  # Returns 5.0

# Calculate midpoint
mp = midpoint((0, 0), (4, 4))  # Returns (2.0, 2.0)

# Interpolate between points
from multidimention_paint import interpolate
p = interpolate((0, 0), (10, 10), t=0.5)  # Returns (5.0, 5.0)

# Get bounding box
from multidimention_paint import bounding_box
bbox = bounding_box((1, 1), (5, 5), (3, 3))
# Returns ((1, 1), (5, 5))
```

### Advanced Features

#### Point Metadata

```python
point = painter.add_point(5, 5)
point.set_metadata("color", "red")
point.set_metadata("opacity", 0.8)
point.set_metadata("layer", 1)

color = point.get_metadata("color")
```

#### Selection History

```python
painter.select_all()
painter.save_selection()

painter.clear_selection()
painter.select_single_point((5, 5))
painter.save_selection()

painter.load_selection(0)  # Load first selection
painter.load_selection(-1) # Load last selection
```

#### Export Data

```python
# Export points
points_data = painter.export_points()
# Returns: [
#   {'coords': (1.0, 2.0), 'label': 'point1', 'dimensions': 2, 'metadata': {...}},
#   ...
# ]

# Export shapes
shapes_data = painter.export_shapes()
# Returns: [
#   {'type': 'Circle', 'filled': True, 'color': None, 'points': [...]},
#   ...
# ]
```

#### Statistics

```python
stats = painter.get_statistics()
# Returns:
# {
#   'point_count': 100,
#   'shape_count': 5,
#   'dimensions': 2,
#   'bounding_box': ((0, 0), (100, 100)),
#   'centroid': (50, 50),
#   'selection_count': 10
# }
```

### Error Handling

```python
try:
    # Dimension mismatch
    point_set = PointSet()
    point_set.add_point(Point(1, 2))
    point_set.add_point(Point(1, 2, 3))  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

try:
    # Invalid coordinates
    p = Point("not_a_number", 2)  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

---

## Français

### Aperçu

MultidimensionalPaint est un module Python complet pour travailler avec des points et des formes géométriques dans des espaces multidimensionnels (1D, 2D, 3D, 4D et plus). Il fournit des outils puissants pour :

- **Gestion des Points** : Créer et manipuler des points dans n'importe quel nombre de dimensions
- **Formes Géométriques** : Dessiner des lignes, cercles, rectangles, carrés, ellipses, arcs et formes fermées personnalisées
- **Sélection de Points** : Sélectionner des points selon divers critères
- **Analyse** : Calculer les distances, centroïdes, boîtes délimitantes et d'autres propriétés géométriques
- **Export de Données** : Exporter les points et formes pour un traitement ultérieur

### Démarrage Rapide

```python
from multidimention_paint import MultidimensionalPaint

painter = MultidimensionalPaint()

# Ajouter des points
painter.add_point(0, 0)
painter.add_point(5, 5)
painter.add_point(10, 10)

# Dessiner des formes
painter.draw_circle((5, 5), 3)
painter.draw_rectangle((0, 0), (10, 10))

# Sélectionner des points
selected = painter.select_within_region((0, 0), (5, 5))
print(f"Points sélectionnés : {len(selected)}")
```

### Classes Principales

**Point** : Représente un point dans un espace n-dimensionnel.

```python
p = Point(1, 2, 3, label="mon_point")
distance = p.distance_to(Point(4, 5, 6))
```

**PointSet** : Gère une collection de points.

```python
point_set = PointSet()
point_set.add_point(Point(1, 2))
nearest = point_set.find_nearest(Point(1.5, 2))
```

**MultidimensionalPaint** : Interface principale.

### Méthodes de Sélection

- `select_single_point(target, tolerance)` - Sélectionner un seul point
- `select_line(start, end, tolerance)` - Sélectionner le long d'une ligne
- `select_within_region(corner1, corner2)` - Sélectionner dans une région
- `select_within_shape(shape)` - Sélectionner dans une forme
- `select_nearest(target, count)` - Sélectionner les points les plus proches
- `select_farthest(target, count)` - Sélectionner les points les plus éloignés
- `select_all()` - Sélectionner tous les points

---

## Español

### Descripción General

MultidimensionalPaint es un módulo Python completo para trabajar con puntos y formas geométricas en espacios multidimensionales (1D, 2D, 3D, 4D y más). Proporciona herramientas poderosas para:

- **Gestión de Puntos** : Crear y manipular puntos en cualquier número de dimensiones
- **Formas Geométricas** : Dibujar líneas, círculos, rectángulos, cuadrados, elipses, arcos y formas cerradas personalizadas
- **Selección de Puntos** : Seleccionar puntos según varios criterios
- **Análisis** : Calcular distancias, centroides, cuadros delimitadores y otras propiedades geométricas
- **Exportación de Datos** : Exportar puntos y formas para su procesamiento posterior

### Inicio Rápido

```python
from multidimention_paint import MultidimensionalPaint

pintor = MultidimensionalPaint()

# Agregar puntos
pintor.add_point(0, 0)
pintor.add_point(5, 5)

# Dibujar formas
pintor.draw_circle((5, 5), 3)

# Seleccionar puntos
seleccionados = pintor.select_within_region((0, 0), (5, 5))
```

---

## Deutsch

### Übersicht

MultidimensionalPaint ist ein umfassendes Python-Modul für die Arbeit mit Punkten und geometrischen Formen in mehrdimensionalen Räumen (1D, 2D, 3D, 4D und darüber hinaus). Es bietet leistungsstarke Tools für:

- **Punktverwaltung** : Erstellen und Bearbeiten von Punkten in beliebig vielen Dimensionen
- **Geometrische Formen** : Zeichnen von Linien, Kreisen, Rechtecken, Quadraten, Ellipsen, Bögen und benutzerdefinierten geschlossenen Formen
- **Punktauswahl** : Punkte nach verschiedenen Kriterien auswählen
- **Analyse** : Abstände, Schwerpunkte, Begrenzungsrahmen und andere geometrische Eigenschaften berechnen
- **Datenexport** : Punkte und Formen für die weitere Verarbeitung exportieren

### Schnellstart

```python
from multidimention_paint import MultidimensionalPaint

maler = MultidimensionalPaint()

# Punkte hinzufügen
maler.add_point(0, 0)
maler.add_point(5, 5)

# Formen zeichnen
maler.draw_circle((5, 5), 3)

# Punkte auswählen
ausgewählt = maler.select_within_region((0, 0), (5, 5))
```

---

## Additional Resources

- **Module File Structure**:
  - `__init__.py` - Package initialization
  - `points.py` - Point and PointSet classes
  - `shapes.py` - Geometric shape classes
  - `selection.py` - Selection engine
  - `paint.py` - Main MultidimensionalPaint class
  - `utils.py` - Utility functions
  - `test_multidimension_paint.py` - Comprehensive test suite

- **Testing**: Run tests with `python -m pytest test_multidimension_paint.py`

- **Performance**: The module is optimized for:
  - Working with thousands of points
  - Multiple geometric shapes
  - Complex selection operations
  - High-dimensional data

---

*Last updated: January 13, 2026*
