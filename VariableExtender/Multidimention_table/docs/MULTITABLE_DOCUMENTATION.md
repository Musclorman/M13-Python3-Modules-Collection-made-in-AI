# Multi-Dimensional Table Module - Complete Documentation

## Table des Matières / Table of Contents / Inhaltsverzeichnis

1. [English Documentation](#english)
2. [French Documentation](#french)
3. [Spanish Documentation](#spanish)
4. [German Documentation](#german)
5. [Italian Documentation](#italian)
6. [Chinese Documentation](#chinese)

---

## ENGLISH DOCUMENTATION {#english}

### Overview

The Multi-Dimensional Table (MDT) module provides a comprehensive Python library for creating, manipulating, and converting multi-dimensional arrays of any dimension (1D, 2D, 3D, nD).

### Features

- **Creation**: Create tables of any dimension (1D, 2D, 3D, nD)
- **Element Access**: Get and set individual elements or ranges
- **Slicing**: Slice tables along any dimension
- **Reshaping**: Reshape tables to different dimensions
- **Merging**: Combine tables along specified axes
- **Splitting**: Split tables into multiple parts
- **Flattening**: Convert multi-dimensional tables to 1D
- **Transposition**: Swap rows and columns in 2D tables
- **Rotation**: Rotate 2D tables
- **Transformations**: Apply functions to all elements
- **Filtering**: Filter elements based on predicates
- **Statistics**: Calculate sum, mean, min, max
- **Fill & Pad**: Fill tables with values or add padding
- **Format Conversion**: Convert to/from CSV, JSON, dict, list

### Basic Usage

```python
from multitable import Table

# Create a 2D table
table = Table.create_2d(3, 4, fill=0)

# Set an element
table.set_element([0, 0], 42)

# Get an element
value = table.get_element([0, 0])

# Flatten to 1D
flat = table.flatten()

# Reshape
reshaped = flat.reshape((2, 6))

# Apply transformation
doubled = table.apply(lambda x: x * 2)
```

### API Reference

#### Creation Methods

- `Table.create_1d(length, fill=0)` - Create 1D table
- `Table.create_2d(rows, cols, fill=0)` - Create 2D table
- `Table.create_3d(depth, rows, cols, fill=0)` - Create 3D table
- `Table.create_nd(shape, fill=0)` - Create n-dimensional table
- `Table.from_list(data)` - Create from nested list
- `Table.from_flat(data, shape)` - Create from flat data

#### Element Access

- `get_element(indices)` - Get element at position
- `set_element(indices, value)` - Set element at position

#### Manipulation

- `slice(slice_spec)` - Slice the table
- `reshape(new_shape)` - Reshape the table
- `flatten()` - Flatten to 1D
- `transpose_2d()` - Transpose 2D table
- `merge(other, axis)` - Merge two tables
- `split(axis, indices)` - Split table into parts

#### Transformations

- `apply(func)` - Apply function to all elements
- `map_values(mapping)` - Map values using dictionary
- `filter_elements(predicate)` - Filter elements
- `fill(value)` - Fill all elements
- `pad(pad_size, value)` - Pad all dimensions
- `rotate_2d_90()` - Rotate 2D table 90 degrees

#### Statistics

- `sum()` - Calculate sum of all elements
- `mean()` - Calculate mean
- `min()` - Find minimum element
- `max()` - Find maximum element

#### Conversions

- `to_list()` - Convert to nested list
- `to_dict()` - Convert to dictionary
- `to_json()` - Convert to JSON string
- `from_json(json_str)` - Create from JSON
- `to_csv()` - Convert 2D table to CSV
- `from_csv(csv_str)` - Create 2D table from CSV

---

## FRENCH DOCUMENTATION {#french}

### Vue d'ensemble

Le module Table Multidimensionnelle (MDT) fournit une bibliothèque Python complète pour créer, manipuler et convertir des tableaux multidimensionnels de n'importe quelle dimension (1D, 2D, 3D, nD).

### Caractéristiques

- **Création**: Créer des tableaux de n'importe quelle dimension
- **Accès aux éléments**: Obtenir et définir des éléments individuels ou des plages
- **Découpe**: Découper les tableaux selon n'importe quelle dimension
- **Remodelage**: Remodeler les tableaux à différentes dimensions
- **Fusion**: Combiner des tableaux selon les axes spécifiés
- **Division**: Diviser les tableaux en plusieurs parties
- **Aplatissement**: Convertir les tableaux multidimensionnels en 1D
- **Transposition**: Échanger les lignes et les colonnes dans les tableaux 2D
- **Rotation**: Faire pivoter les tableaux 2D
- **Transformations**: Appliquer des fonctions à tous les éléments
- **Filtrage**: Filtrer les éléments en fonction des prédicats
- **Statistiques**: Calculer somme, moyenne, min, max
- **Remplissage et rembourrage**: Remplir les tableaux ou ajouter du rembourrage
- **Conversion de format**: Convertir vers/depuis CSV, JSON, dict, list

### Utilisation de base

```python
from multitable import Table

# Créer un tableau 2D
table = Table.create_2d(3, 4, fill=0)

# Définir un élément
table.set_element([0, 0], 42)

# Obtenir un élément
valeur = table.get_element([0, 0])

# Aplatir en 1D
plat = table.flatten()

# Remodeler
remodelé = plat.reshape((2, 6))
```

### Méthodes principales

- `create_1d(longueur, fill=0)` - Créer tableau 1D
- `create_2d(lignes, colonnes, fill=0)` - Créer tableau 2D
- `create_3d(profondeur, lignes, colonnes, fill=0)` - Créer tableau 3D
- `create_nd(shape, fill=0)` - Créer tableau n-dimensionnel
- `get_element(indices)` - Obtenir élément
- `set_element(indices, valeur)` - Définir élément
- `flatten()` - Aplatir en 1D
- `reshape(nouvelle_shape)` - Remodeler
- `slice(spec_découpe)` - Découper
- `transpose_2d()` - Transposer
- `merge(autre, axis)` - Fusionner
- `apply(fonction)` - Appliquer fonction

---

## SPANISH DOCUMENTATION {#spanish}

### Descripción General

El módulo de Tabla Multidimensional (MDT) proporciona una biblioteca Python completa para crear, manipular y convertir matrices multidimensionales de cualquier dimensión (1D, 2D, 3D, nD).

### Características

- **Creación**: Crear tablas de cualquier dimensión
- **Acceso a elementos**: Obtener y establecer elementos individuales o rangos
- **Corte**: Cortar tablas a lo largo de cualquier dimensión
- **Remodelado**: Remodelar tablas a diferentes dimensiones
- **Fusión**: Combinar tablas a lo largo de ejes especificados
- **División**: Dividir tablas en múltiples partes
- **Aplanamiento**: Convertir tablas multidimensionales a 1D
- **Transposición**: Cambiar filas y columnas en tablas 2D
- **Rotación**: Rotar tablas 2D
- **Transformaciones**: Aplicar funciones a todos los elementos
- **Filtrado**: Filtrar elementos según predicados
- **Estadísticas**: Calcular suma, media, mín, máx
- **Relleno y acolchado**: Rellenar tablas o agregar acolchado
- **Conversión de formato**: Convertir a/desde CSV, JSON, dict, list

### Uso básico

```python
from multitable import Table

# Crear una tabla 2D
tabla = Table.create_2d(3, 4, fill=0)

# Establecer un elemento
tabla.set_element([0, 0], 42)

# Obtener un elemento
valor = tabla.get_element([0, 0])

# Aplanar a 1D
plana = tabla.flatten()
```

### Métodos principales

- `create_1d(longitud)` - Crear tabla 1D
- `create_2d(filas, columnas)` - Crear tabla 2D
- `create_3d(profundidad, filas, columnas)` - Crear tabla 3D
- `create_nd(forma)` - Crear tabla n-dimensional
- `flatten()` - Aplanar a 1D
- `reshape(nueva_forma)` - Remodelar
- `slice(especificación)` - Cortar
- `merge(otra, axis)` - Fusionar
- `transpose_2d()` - Transponer

---

## GERMAN DOCUMENTATION {#german}

### Überblick

Das Multidimensional Table (MDT) Modul bietet eine umfassende Python-Bibliothek zum Erstellen, Manipulieren und Konvertieren von mehrdimensionalen Arrays beliebiger Dimension (1D, 2D, 3D, nD).

### Funktionen

- **Erstellung**: Tabellen beliebiger Dimension erstellen
- **Elementzugriff**: Einzelne Elemente oder Bereiche abrufen und festlegen
- **Slicing**: Tabellen entlang einer beliebigen Dimension aufteilen
- **Umformen**: Tabellen in verschiedene Dimensionen umformen
- **Zusammenführung**: Tabellen entlang bestimmter Achsen kombinieren
- **Aufteilen**: Tabellen in mehrere Teile aufteilen
- **Flatten**: Mehrdimensionale Tabellen zu 1D konvertieren
- **Transposition**: Zeilen und Spalten in 2D-Tabellen vertauschen
- **Rotation**: 2D-Tabellen drehen
- **Transformationen**: Funktionen auf alle Elemente anwenden
- **Filterung**: Elemente nach Prädikaten filtern
- **Statistiken**: Summe, Mittelwert, Min, Max berechnen
- **Füllen und Polsterung**: Tabellen füllen oder auffüllen
- **Formatkonvertierung**: Zu/Von CSV, JSON, dict, list konvertieren

### Grundlegende Verwendung

```python
from multitable import Table

# 2D-Tabelle erstellen
tabelle = Table.create_2d(3, 4, fill=0)

# Element setzen
tabelle.set_element([0, 0], 42)

# Element abrufen
wert = tabelle.get_element([0, 0])

# Zu 1D abflachen
flach = tabelle.flatten()
```

---

## ITALIAN DOCUMENTATION {#italian}

### Panoramica

Il modulo Multi-Dimensional Table (MDT) fornisce una libreria Python completa per creare, manipolare e convertire array multidimensionali di qualsiasi dimensione (1D, 2D, 3D, nD).

### Caratteristiche

- **Creazione**: Creare tabelle di qualsiasi dimensione
- **Accesso agli elementi**: Ottenere e impostare elementi individuali o intervalli
- **Slicing**: Affettare tabelle lungo qualsiasi dimensione
- **Rimodellamento**: Rimodellare tabelle a dimensioni diverse
- **Fusione**: Combinare tabelle lungo assi specificati
- **Divisione**: Dividere tabelle in più parti
- **Appiattimento**: Convertire tabelle multidimensionali a 1D
- **Trasposizione**: Scambiare righe e colonne in tabelle 2D
- **Rotazione**: Ruotare tabelle 2D
- **Trasformazioni**: Applicare funzioni a tutti gli elementi
- **Filtraggio**: Filtrare elementi in base ai predicati
- **Statistiche**: Calcolare somma, media, min, max
- **Riempimento e imbottitura**: Riempire tabelle o aggiungere imbottitura
- **Conversione formato**: Convertire da/a CSV, JSON, dict, list

### Utilizzo di base

```python
from multitable import Table

# Creare una tabella 2D
tabella = Table.create_2d(3, 4, fill=0)

# Impostare un elemento
tabella.set_element([0, 0], 42)

# Ottenere un elemento
valore = tabella.get_element([0, 0])

# Appiattire a 1D
piatta = tabella.flatten()
```

---

## CHINESE DOCUMENTATION {#chinese}

### 概述

多维表 (MDT) 模块提供了一个全面的 Python 库，用于创建、操作和转换任何维度的多维数组（1D、2D、3D、nD）。

### 功能

- **创建**: 创建任何维度的表
- **元素访问**: 获取和设置单个元素或范围
- **切片**: 沿任何维度切片表
- **重塑**: 将表重塑为不同维度
- **合并**: 沿指定轴组合表
- **拆分**: 将表分成多个部分
- **展平**: 将多维表转换为 1D
- **转置**: 在 2D 表中交换行和列
- **旋转**: 旋转 2D 表
- **变换**: 对所有元素应用函数
- **筛选**: 根据谓词筛选元素
- **统计**: 计算总和、平均值、最小值、最大值
- **填充**: 填充表或添加填充
- **格式转换**: 转换为/从 CSV、JSON、dict、list

### 基本用法

```python
from multitable import Table

# 创建 2D 表
table = Table.create_2d(3, 4, fill=0)

# 设置元素
table.set_element([0, 0], 42)

# 获取元素
value = table.get_element([0, 0])

# 展平为 1D
flat = table.flatten()
```

---

## Complete Example Workflows

### Workflow 1: Data Processing

```python
# 1. Create table
data = Table.create_2d(100, 10, fill=0)

# 2. Fill with data
for i in range(100):
    for j in range(10):
        data.set_element([i, j], i * 10 + j)

# 3. Apply transformations
normalized = data.apply(lambda x: x / 1000)

# 4. Filter
high_values = normalized.filter_elements(lambda x: x > 0.5)

# 5. Get statistics
avg = normalized.mean()
```

### Workflow 2: Image Processing (2D)

```python
# Load as table
image = Table.create_2d(256, 256, fill=128)

# Pad edges
padded = image.pad(2, value=0)

# Slice region
roi = image.slice([slice(100, 150), slice(100, 150)])

# Apply filter
blurred = image.apply(lambda x: min(255, x + 10))

# Save to CSV
csv_data = blurred.to_csv()
```

### Workflow 3: Volume Processing (3D)

```python
# Create 3D volume
volume = Table.create_3d(64, 64, 64, fill=0)

# Slice cross-section
cross_section = volume.slice([slice(32, 33), slice(None), slice(None)])

# Process each slice
for i in range(volume.shape[0]):
    slice_i = volume[i]
    processed = slice_i.apply(lambda x: x * 2)
```

---

## Error Handling

The module provides specific exceptions:

- `TableError` - Base exception
- `DimensionMismatchError` - Dimension mismatch
- `IndexError` - Invalid index
- `ShapeError` - Invalid shape

---

## Performance Considerations

- Large arrays (1000x1000+) may be slow for complex operations
- Use slicing instead of copying for memory efficiency
- Consider flattening before statistical operations
- JSON serialization works for reasonable sizes

---

## See Also

- `multitable.py` - Main module implementation
- `test_multitable.py` - Comprehensive test suite (250+ tests)
- `example_multitable.py` - Practical examples
