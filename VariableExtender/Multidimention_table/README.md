# MultiDimTable - Simple & Powerful Multidimensional Arrays

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A lightweight, intuitive Python module for managing 1D, 2D, 3D and n-dimensional tables/arrays. Perfect for console and graphical applications.

## Features

✨ **Easy to Use**
- Intuitive API inspired by NumPy but simpler
- No external dependencies (pure Python)
- Works with any Python 3.6+ installation

📊 **Powerful Operations**
- Create arrays with various methods (`create`, `zeros`, `ones`)
- Flatten and reshape arrays
- Transpose 2D matrices
- Concatenate and split arrays
- Stack multiple arrays
- Apply functions element-wise
- Statistical operations (sum, mean, min, max)

🔧 **Flexible**
- Support for any data types (numbers, strings, objects, etc.)
- Clean error handling with custom exceptions
- Deep copy support
- Iterator interface

🎯 **Compatible**
- Easy to integrate into any project
- Works with console libraries
- Works with GUI frameworks
- No special dependencies

📊 **Data Transformation**
- Apply custom functions to all elements
- Filter elements based on predicates
- Map values using dictionaries
- Fill and pad operations
- Statistical operations (sum, mean, min, max)

🔄 **Format Conversions**
- Convert to/from nested lists
- CSV export and import
- JSON serialization and deserialization
- Dictionary representation
- Full round-trip support

## Installation

```bash
# Clone or copy the module
from multitable import Table
```

## Quick Start

### Create Tables

```python
from multitable import Table

# 1D table
t1d = Table.create_1d(10, fill=0)

# 2D table
t2d = Table.create_2d(3, 4, fill=0)

# 3D table
t3d = Table.create_3d(2, 3, 4, fill=0)

# n-dimensional table
tnd = Table.create_nd((2, 3, 4, 5), fill=0)

# From existing data
from_list = Table.from_list([[1, 2, 3], [4, 5, 6]])

# From flat data
from_flat = Table.from_flat([1, 2, 3, 4, 5, 6], shape=(2, 3))
```

### Element Access

```python
# Get element
value = table.get_element([0, 1, 2])

# Set element
table.set_element([0, 1, 2], 42)

# Using indexing
table[0, 1, 2] = 42
value = table[0, 1, 2]
```

### Slicing

```python
# Slice rows (2D)
rows = table.slice([slice(0, 2), slice(None)])

# Slice columns (2D)
cols = table.slice([slice(None), slice(1, 3)])

# Slice submatrix (2D)
sub = table.slice([slice(1, 3), slice(1, 3)])

# With step (2D)
step = table.slice([slice(0, None, 2), slice(None)])
```

### Reshaping

```python
# Flatten to 1D
flat = table.flatten()

# Reshape to different dimensions
reshaped = flat.reshape((4, 3))
reshaped_3d = flat.reshape((2, 2, 3))
```

### Merging and Splitting

```python
# Merge tables
merged = table1.merge(table2, axis=0)  # Row-wise
merged = table1.merge(table2, axis=1)  # Column-wise

# Split table
parts = table.split(0, [2, 4])  # Split at indices 2 and 4
```

### Transformations

```python
# Apply function
squared = table.apply(lambda x: x ** 2)

# Map values
mapping = {0: 'zero', 1: 'one'}
mapped = table.map_values(mapping)

# Filter elements
evens = table.filter_elements(lambda x: x % 2 == 0)

# Fill and pad
table.fill(0)  # Fill all with 0
padded = table.pad(2, fill=0)  # Pad with 2 on each side
```

### Statistics

```python
total = table.sum()
average = table.mean()
minimum = table.min()
maximum = table.max()
```

### Format Conversions

```python
# To various formats
as_list = table.to_list()
as_dict = table.to_dict()
as_csv = table.to_csv()  # 2D only
as_json = table.to_json()

# From various formats
from_csv_str = Table.from_csv(csv_string)
from_json_str = Table.from_json(json_string)
```

### Special Operations

```python
# Transpose (2D)
transposed = table.transpose_2d()

# Rotate 90 degrees (2D)
rotated = table.rotate_2d_90()

# Copy (deep copy)
copy = table.copy()

# Arithmetic operations
result = table1 + table2
scaled = table * 2
```

## Examples

### Example 1: Image Processing

```python
# Create a 256x256 image
image = Table.create_2d(256, 256, fill=128)

# Fill with pattern
for i in range(256):
    for j in range(256):
        image.set_element([i, j], (i + j) % 256)

# Apply brightness adjustment
brighter = image.apply(lambda x: min(255, x + 30))

# Extract region of interest
roi = image.slice([slice(100, 150), slice(100, 150)])

# Save to CSV
csv_data = brighter.to_csv()
```

### Example 2: 3D Volume Processing

```python
# Create 3D volume
volume = Table.create_3d(64, 64, 64, fill=0)

# Fill with data
for z in range(64):
    for y in range(64):
        for x in range(64):
            value = (x + y + z) % 256
            volume.set_element([z, y, x], value)

# Get a 2D slice
z_slice = volume.slice([slice(32, 33), slice(None), slice(None)])

# Process entire volume
processed = volume.apply(lambda x: x * 2)

# Calculate statistics
average = volume.mean()
```

### Example 3: Data Transformation

```python
# Create data table
data = Table.create_2d(100, 10, fill=0)

# Fill with sample data
for i in range(100):
    for j in range(10):
        data.set_element([i, j], i * j)

# Normalize
max_val = data.max()
normalized = data.apply(lambda x: x / max_val)

# Filter outliers
filtered = normalized.filter_elements(lambda x: x < 0.9)

# Get statistics
stats = {
    'sum': normalized.sum(),
    'mean': normalized.mean(),
    'min': normalized.min(),
    'max': normalized.max(),
}

# Export to JSON
json_data = normalized.to_json()
```

## API Reference

### Creation Methods

| Method | Description |
|--------|-------------|
| `create_1d(length, fill=0)` | Create 1D table |
| `create_2d(rows, cols, fill=0)` | Create 2D table |
| `create_3d(depth, rows, cols, fill=0)` | Create 3D table |
| `create_nd(shape, fill=0)` | Create n-dimensional table |
| `from_list(data)` | Create from nested list |
| `from_flat(data, shape)` | Create from flat list |

### Element Access

| Method | Description |
|--------|-------------|
| `get_element(indices)` | Get element at indices |
| `set_element(indices, value)` | Set element at indices |

### Manipulation

| Method | Description |
|--------|-------------|
| `slice(slice_spec)` | Slice the table |
| `reshape(new_shape)` | Reshape to new dimensions |
| `flatten()` | Flatten to 1D |
| `transpose_2d()` | Transpose 2D table |
| `merge(other, axis)` | Merge with another table |
| `split(axis, indices)` | Split table into parts |

### Transformations

| Method | Description |
|--------|-------------|
| `apply(func)` | Apply function to all elements |
| `map_values(mapping)` | Map values using dictionary |
| `filter_elements(predicate)` | Filter elements |
| `fill(value)` | Fill all elements |
| `pad(pad_size, value)` | Pad all dimensions |
| `rotate_2d_90()` | Rotate 2D 90 degrees |

### Statistics

| Method | Description |
|--------|-------------|
| `sum()` | Sum of all elements |
| `mean()` | Mean of all elements |
| `min()` | Minimum element |
| `max()` | Maximum element |

### Conversions

| Method | Description |
|--------|-------------|
| `to_list()` | Convert to nested list |
| `to_dict()` | Convert to dictionary |
| `to_json()` | Convert to JSON string |
| `from_json(json_str)` | Create from JSON |
| `to_csv()` | Convert 2D to CSV |
| `from_csv(csv_str)` | Create from CSV |

## Properties

| Property | Description |
|----------|-------------|
| `shape` | Tuple of dimensions |
| `ndim` | Number of dimensions |
| `size` | Total number of elements |
| `data` | Underlying nested list |

## Testing

The module includes 250+ comprehensive test cases:

```bash
pytest test_multitable.py -v
```

Test coverage includes:
- All creation methods
- Element access and modification
- Slicing operations
- Reshaping and flattening
- Merging and splitting
- Transposition and rotation
- Functional transformations
- Format conversions
- Statistical operations
- Error handling
- Edge cases
- Complex workflows

## Examples

Run the example file to see 19+ practical examples:

```bash
python example_multitable.py
```

## Performance

- Suitable for tables up to ~100,000 elements
- For larger data, consider NumPy arrays
- Slicing and reshaping are efficient (copy-on-write not implemented)
- All operations preserve data integrity

## Limitations

- No built-in parallelization
- No sparse array support
- JSON serialization limited by Python's limitations
- CSV export/import for 2D tables only
- No NumPy integration (pure Python)

## Error Handling

The module provides specific exceptions:

```python
from multitable import (
    TableError,           # Base exception
    DimensionMismatchError,  # Dimension mismatch
    IndexError,          # Invalid index
    ShapeError,          # Invalid shape
)
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions welcome! Please ensure:
- All tests pass
- Code follows PEP 8
- New features include tests
- Documentation is updated

## Support

For issues, questions, or suggestions:
1. Check the documentation files
2. Review test cases for usage patterns
3. Check example files for workflows
4. Open an issue with detailed description

## Version

Current Version: 1.0.0
Python: 3.7+
Dependencies: None (pure Python)

---

**Happy table manipulating! 📊**
