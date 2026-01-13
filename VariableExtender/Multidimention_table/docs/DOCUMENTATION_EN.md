# MultiDimTable - Complete Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Quick Start Guide](#quick-start-guide)
4. [API Reference](#api-reference)
5. [Advanced Examples](#advanced-examples)
6. [Troubleshooting](#troubleshooting)

---

## Introduction

**MultiDimTable** is a lightweight and intuitive Python module for managing multidimensional arrays (1D, 2D, 3D, and n-dimensional). It is designed to be easy to import and use in any project, console library, or graphical interface.

### Key Features

- ✅ Native support for 1D, 2D, 3D and n-dimensional arrays
- ✅ Easy creation with `MultiDimTable.create()`, `zeros()`, `ones()`
- ✅ Element access by simple or tuple indices
- ✅ Reshaping and flattening operations
- ✅ Transposition for 2D arrays
- ✅ Concatenation and splitting of arrays
- ✅ Array stacking
- ✅ Conversion to Python lists
- ✅ Element iteration
- ✅ Statistical operations (sum, mean, min, max)
- ✅ Custom function application

---

## Installation

### From the project directory

```python
from Multidimention_table import MultiDimTable
```

Or directly from the path:

```python
import sys
sys.path.insert(0, '/path/to/Multidimention_table')
from __init__ import MultiDimTable
```

---

## Quick Start Guide

### Creating Arrays

```python
from Multidimention_table import MultiDimTable

# Create a 1D array
t1d = MultiDimTable([1, 2, 3, 4, 5])
print(t1d.shape)  # (5,)

# Create a 2D array
t2d = MultiDimTable([[1, 2, 3], [4, 5, 6]])
print(t2d.shape)  # (2, 3)

# Create a 3D array
t3d = MultiDimTable.create((2, 3, 4), fill=0)
print(t3d.shape)  # (2, 3, 4)

# Create with zeros or ones
zeros_table = MultiDimTable.zeros((3, 3))
ones_table = MultiDimTable.ones((2, 4))
```

### Accessing Elements

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])

# 1D access (if applicable)
value = t[1]  # Returns [4, 5, 6]

# 2D access
value = t[0, 1]  # Returns 2
value = t[1, 2]  # Returns 6

# 3D access
t3d = MultiDimTable.create((2, 2, 2), fill=5)
value = t3d[0, 1, 1]  # Returns 5

# Modification
t[0, 0] = 99
print(t[0, 0])  # 99
```

### Reshaping and Flattening

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])

# Flatten to 1D
flat = t.flatten()
print(flat.shape)  # (6,)
print(flat.to_list())  # [1, 2, 3, 4, 5, 6]

# Reshape
reshaped = flat.reshape((3, 2))
print(reshaped.shape)  # (3, 2)
print(reshaped.to_list())  # [[1, 2], [3, 4], [5, 6]]

# 3D reshape
reshaped_3d = flat.reshape((2, 3, 1))
print(reshaped_3d.shape)  # (2, 3, 1)
```

### Concatenation and Splitting

```python
t1 = MultiDimTable([[1, 2], [3, 4]])
t2 = MultiDimTable([[5, 6]])

# Concatenate
concatenated = t1.concatenate(t2, axis=0)
print(concatenated.shape)  # (3, 2)
print(concatenated.to_list())  # [[1, 2], [3, 4], [5, 6]]

# Split
t = MultiDimTable([[1, 2, 3, 4], [5, 6, 7, 8]])
parts = t.split(2, axis=0)
print(len(parts))  # 2
print(parts[0].shape)  # (1, 4)
print(parts[1].shape)  # (1, 4)
```

### Stacking

```python
t1 = MultiDimTable([1, 2, 3])
t2 = MultiDimTable([4, 5, 6])
t3 = MultiDimTable([7, 8, 9])

# Stack
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

### Iteration and Statistical Operations

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])

# Iteration
for value in t.iterate():
    print(value)  # Prints 1, 2, 3, 4, 5, 6

# Statistics
print(t.sum())   # 21
print(t.mean())  # 3.5
print(t.min())   # 1
print(t.max())   # 6

# Function application
t2 = t.apply(lambda x: x ** 2)
print(t2.to_list())  # [[1, 4, 9], [16, 25, 36]]
```

---

## API Reference

### MultiDimTable Class

#### Constructors

| Method | Description | Example |
|--------|-------------|---------|
| `MultiDimTable(data)` | Create from nested lists | `MultiDimTable([[1, 2], [3, 4]])` |
| `create(shape, fill)` | Create with specified dimensions, filled with value | `MultiDimTable.create((2, 3), fill=0)` |
| `zeros(shape)` | Create filled with zeros | `MultiDimTable.zeros((3, 3))` |
| `ones(shape)` | Create filled with ones | `MultiDimTable.ones((2, 4))` |

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `shape` | Tuple[int, ...] | Array dimensions |
| `ndim` | int | Number of dimensions |
| `size` | int | Total number of elements |

#### Data Access

| Method | Description | Example |
|--------|-------------|---------|
| `__getitem__(index)` | Access element or row | `t[0, 1]` |
| `__setitem__(index, value)` | Modify element | `t[0, 1] = 10` |
| `to_list()` | Convert to nested lists | `t.to_list()` |
| `to_flat_list()` | Convert to flat list | `t.to_flat_list()` |

#### Transformations

| Method | Description | Returns |
|--------|-------------|---------|
| `flatten()` | Flatten to 1D | MultiDimTable |
| `reshape(shape)` | Reshape dimensions | MultiDimTable |
| `transpose()` | Transpose (2D only) | MultiDimTable |
| `copy()` | Deep copy | MultiDimTable |
| `apply(func)` | Apply function to elements | MultiDimTable |

#### Merge/Split Operations

| Method | Description | Returns |
|--------|-------------|---------|
| `concatenate(other, axis)` | Concatenate with another array | MultiDimTable |
| `split(sections, axis)` | Split into parts | List[MultiDimTable] |
| `stack(tables, axis)` | Stack arrays together | MultiDimTable |

#### Iteration and Aggregation

| Method | Description | Returns |
|--------|-------------|---------|
| `iterate()` | Iterator over all elements | Iterator[Any] |
| `sum()` | Sum of all elements | Union[int, float] |
| `mean()` | Arithmetic mean | float |
| `min()` | Minimum element | Any |
| `max()` | Maximum element | Any |

---

## Advanced Examples

### Example 1: 3D Matrix Manipulation

```python
# Create 3D matrix for RGB images
images = MultiDimTable.create((4, 32, 32), fill=0)  # 4 images of 32x32

# Modify a pixel in first image
images[0, 10, 15] = 255

# Flatten all images
flat_images = images.flatten()
print(f"Total pixels: {flat_images.size}")  # 4096

# Reshape for training data
reshaped = flat_images.reshape((4, 1024))
print(reshaped.shape)  # (4, 1024) - batch x features
```

### Example 2: Tabular Data Processing

```python
# Sales data: product x month x year
sales = MultiDimTable([
    [[100, 110, 120], [150, 160, 170]],  # Product 1
    [[200, 210, 220], [250, 260, 270]],  # Product 2
])

print(sales.shape)  # (2, 2, 3)

# Total sales per product
for i in range(sales.shape[0]):
    product_sales = MultiDimTable(sales._data[i]).flatten()
    print(f"Product {i+1}: {product_sales.sum()} units")

# Increase sales by 10%
sales_augmented = sales.apply(lambda x: int(x * 1.1))
```

### Example 3: Batch Processing

```python
# Split large dataset into batches
full_data = MultiDimTable.create((1000, 128), fill=1)

batches = full_data.split(10, axis=0)
print(f"Number of batches: {len(batches)}")
print(f"Batch size: {batches[0].shape}")  # (100, 128)

# Process each batch
for batch in batches:
    normalized = batch.apply(lambda x: (x - 0.5) / 0.5)
    # Process normalized batch
```

### Example 4: Data Fusion

```python
# Merge multiple data sources
data_source_1 = MultiDimTable([[1, 2, 3], [4, 5, 6]])
data_source_2 = MultiDimTable([[7, 8, 9]])
data_source_3 = MultiDimTable([[10, 11, 12]])

# Concatenation
merged = data_source_1.concatenate(data_source_2, axis=0)
merged = merged.concatenate(data_source_3, axis=0)

print(merged.shape)  # (4, 3)
print(f"Total elements: {merged.size}")  # 12
```

---

## Troubleshooting

### Common Errors

#### ShapeError: Inconsistent dimensions

```python
# ❌ Error - inconsistent dimensions
try:
    t = MultiDimTable([[1, 2], [3, 4, 5]])  # Rows of different sizes
except ShapeError as e:
    print(f"Error: {e}")

# ✅ Correct
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])  # Uniform rows
```

#### IndexError_: Index out of bounds

```python
t = MultiDimTable([[1, 2, 3], [4, 5, 6]])

# ❌ Error - index out of bounds
try:
    value = t[5, 5]  # Out of bounds
except IndexError_ as e:
    print(f"Error: {e}")

# ✅ Correct
value = t[0, 0]  # Valid
value = t[1, 2]  # Valid
```

#### ShapeError: Cannot reshape

```python
t = MultiDimTable([1, 2, 3, 4, 5])  # 5 elements

# ❌ Error - 5 elements cannot form 2x3 matrix (requires 6)
try:
    t2d = t.reshape((2, 3))
except ShapeError as e:
    print(f"Error: {e}")

# ✅ Correct
t2d = t.reshape((5, 1))  # or (1, 5)
```

---

## Performance Notes

- For very large dimensions (>10⁷ elements), consider NumPy for better performance.
- MultiDimTable uses nested Python lists, suitable for small to medium-sized arrays.
- Copy operations (`copy()`) create deep copies - use cautiously on large arrays.

---

**MultiDimTable v1.0.0** | Author: MIDInosaure | License: MIT
