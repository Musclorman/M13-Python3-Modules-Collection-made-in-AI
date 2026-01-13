"""
Multi-Dimensional Table Module

A comprehensive module for creating, manipulating, converting, slicing, and merging
multi-dimensional arrays (1D, 2D, 3D, nD) with support for various data types and
flexible operations.

Features:
    - Create tables of any dimension
    - Convert between different dimensions
    - Slice and subset tables
    - Merge and combine tables
    - Transpose operations
    - Reshape operations
    - Fill and pad operations
    - Flatten and unflatten
    - Get/set elements and ranges
    - Statistical operations
    - Export to various formats

Example:
    >>> from multitable import Table
    >>> t = Table.create_2d(3, 4, fill=0)
    >>> t.set_element([0, 0], 5)
    >>> print(t.get_element([0, 0]))
    5
    >>> t2 = t.slice([0:2, 1:3])
    >>> print(t2.shape)
    (2, 2)
"""

from typing import List, Tuple, Any, Union, Optional, Callable
from copy import deepcopy
from functools import reduce
from itertools import product
import json


class TableError(Exception):
    """Base exception for Table operations."""
    pass


class DimensionMismatchError(TableError):
    """Raised when dimensions don't match for an operation."""
    pass


class IndexError(TableError):
    """Raised when an invalid index is provided."""
    pass


class ShapeError(TableError):
    """Raised when shape doesn't match requirements."""
    pass


class Table:
    """
    A multi-dimensional table/array implementation supporting n-dimensional arrays.
    
    Supports creation, manipulation, slicing, merging, and various transformations
    of multi-dimensional data structures.
    
    Attributes:
        data: The underlying data structure
        shape: Tuple representing dimensions
        ndim: Number of dimensions
        size: Total number of elements
    """
    
    def __init__(self, data: Any):
        """
        Initialize a Table from raw data.
        
        Args:
            data: Nested list structure representing the table
        """
        self.data = data
        self._calculate_shape()
    
    def _calculate_shape(self) -> None:
        """Calculate and store the shape of the table."""
        shape = []
        current = self.data
        while isinstance(current, list):
            shape.append(len(current))
            current = current[0] if current else None
        self.shape = tuple(shape)
        self.ndim = len(self.shape)
        self.size = reduce(lambda x, y: x * y, self.shape, 1)
    
    @staticmethod
    def create_1d(length: int, fill: Any = 0) -> 'Table':
        """
        Create a 1-dimensional table.
        
        Args:
            length: Length of the array
            fill: Value to fill with
            
        Returns:
            Table: 1D table of specified length
        """
        return Table([fill for _ in range(length)])
    
    @staticmethod
    def create_2d(rows: int, cols: int, fill: Any = 0) -> 'Table':
        """
        Create a 2-dimensional table.
        
        Args:
            rows: Number of rows
            cols: Number of columns
            fill: Value to fill with
            
        Returns:
            Table: 2D table of size (rows, cols)
        """
        return Table([[fill for _ in range(cols)] for _ in range(rows)])
    
    @staticmethod
    def create_3d(depth: int, rows: int, cols: int, fill: Any = 0) -> 'Table':
        """
        Create a 3-dimensional table.
        
        Args:
            depth: Depth dimension
            rows: Number of rows
            cols: Number of columns
            fill: Value to fill with
            
        Returns:
            Table: 3D table of size (depth, rows, cols)
        """
        return Table([[[fill for _ in range(cols)] 
                      for _ in range(rows)] 
                      for _ in range(depth)])
    
    @staticmethod
    def create_nd(shape: Tuple[int, ...], fill: Any = 0) -> 'Table':
        """
        Create an n-dimensional table.
        
        Args:
            shape: Tuple of dimensions
            fill: Value to fill with
            
        Returns:
            Table: N-dimensional table
        """
        if not shape:
            raise ShapeError("Shape cannot be empty")
        
        def create_nested(dims: List[int], fill: Any) -> Any:
            if len(dims) == 1:
                return [fill for _ in range(dims[0])]
            return [create_nested(dims[1:], fill) for _ in range(dims[0])]
        
        return Table(create_nested(list(shape), fill))
    
    @staticmethod
    def from_list(data: List) -> 'Table':
        """
        Create a table from a nested list.
        
        Args:
            data: Nested list structure
            
        Returns:
            Table: Table created from data
        """
        return Table(deepcopy(data))
    
    @staticmethod
    def from_flat(flat_data: List, shape: Tuple[int, ...]) -> 'Table':
        """
        Create a table from flat data and reshape it.
        
        Args:
            flat_data: Flat list of values
            shape: Desired shape
            
        Returns:
            Table: Reshaped table
        """
        total_size = reduce(lambda x, y: x * y, shape, 1)
        if len(flat_data) != total_size:
            raise ShapeError(f"Data size {len(flat_data)} doesn't match shape {shape}")
        
        table = Table.create_nd(shape)
        table._set_from_flat(flat_data, 0)
        return table
    
    def _set_from_flat(self, flat_data: List, index: int) -> int:
        """Recursively set values from flat data."""
        if self.ndim == 1:
            for i in range(len(self.data)):
                self.data[i] = flat_data[index]
                index += 1
        else:
            for i in range(len(self.data)):
                subtable = Table(self.data[i])
                index = subtable._set_from_flat(flat_data, index)
        return index
    
    def get_element(self, indices: Union[List[int], Tuple[int, ...]]) -> Any:
        """
        Get element at specified indices.
        
        Args:
            indices: List/tuple of indices
            
        Returns:
            Element at the specified position
        """
        if len(indices) != self.ndim:
            raise DimensionMismatchError(
                f"Expected {self.ndim} indices, got {len(indices)}"
            )
        
        current = self.data
        for i, idx in enumerate(indices):
            if not isinstance(current, list):
                raise IndexError(f"Cannot index further at dimension {i}")
            if idx < 0 or idx >= len(current):
                raise IndexError(f"Index {idx} out of bounds for dimension {i}")
            current = current[idx]
        
        return current
    
    def set_element(self, indices: Union[List[int], Tuple[int, ...]], 
                   value: Any) -> None:
        """
        Set element at specified indices.
        
        Args:
            indices: List/tuple of indices
            value: Value to set
        """
        if len(indices) != self.ndim:
            raise DimensionMismatchError(
                f"Expected {self.ndim} indices, got {len(indices)}"
            )
        
        current = self.data
        for i, idx in enumerate(indices[:-1]):
            if idx < 0 or idx >= len(current):
                raise IndexError(f"Index {idx} out of bounds for dimension {i}")
            current = current[idx]
        
        last_idx = indices[-1]
        if last_idx < 0 or last_idx >= len(current):
            raise IndexError(f"Index {last_idx} out of bounds for last dimension")
        
        current[last_idx] = value
    
    def slice(self, slice_spec: Union[List, Tuple]) -> 'Table':
        """
        Slice the table.
        
        Args:
            slice_spec: List of slice objects (e.g., [0:2, 1:3])
            
        Returns:
            Table: Sliced table
        """
        def slice_recursive(data: Any, specs: List, dim: int) -> Any:
            if dim >= len(specs) or not isinstance(data, list):
                return data
            
            spec = specs[dim]
            if isinstance(spec, slice):
                start = spec.start or 0
                stop = spec.stop or len(data)
                step = spec.step or 1
                return [slice_recursive(item, specs, dim + 1) 
                       for item in data[start:stop:step]]
            elif isinstance(spec, int):
                return slice_recursive(data[spec], specs, dim + 1)
            else:
                return [slice_recursive(item, specs, dim + 1) for item in data]
        
        result = slice_recursive(self.data, slice_spec, 0)
        return Table(result) if isinstance(result, list) else Table([result])
    
    def reshape(self, new_shape: Tuple[int, ...]) -> 'Table':
        """
        Reshape the table to a new shape.
        
        Args:
            new_shape: New shape tuple
            
        Returns:
            Table: Reshaped table
        """
        if self.size != reduce(lambda x, y: x * y, new_shape, 1):
            raise ShapeError(
                f"Cannot reshape size {self.size} to {new_shape}"
            )
        
        flat = self.flatten()
        return Table.from_flat(flat.data, new_shape)
    
    def flatten(self) -> 'Table':
        """
        Flatten the table to 1D.
        
        Args:
            
        Returns:
            Table: 1D flattened table
        """
        def flatten_recursive(data: Any) -> List:
            if not isinstance(data, list):
                return [data]
            result = []
            for item in data:
                result.extend(flatten_recursive(item))
            return result
        
        return Table(flatten_recursive(self.data))
    
    def transpose_2d(self) -> 'Table':
        """
        Transpose a 2D table (swap rows and columns).
        
        Returns:
            Table: Transposed 2D table
        """
        if self.ndim != 2:
            raise DimensionMismatchError("Transpose only works on 2D tables")
        
        rows, cols = self.shape
        result = Table.create_2d(cols, rows)
        for i in range(rows):
            for j in range(cols):
                result.set_element([j, i], self.get_element([i, j]))
        
        return result
    
    def merge(self, other: 'Table', axis: int = 0) -> 'Table':
        """
        Merge this table with another along specified axis.
        
        Args:
            other: Another Table to merge
            axis: Axis along which to merge (0 for rows, 1 for columns)
            
        Returns:
            Table: Merged table
        """
        if self.ndim != other.ndim:
            raise DimensionMismatchError(
                f"Cannot merge tables with different dimensions: {self.ndim} vs {other.ndim}"
            )
        
        if axis == 0:
            # Merge along rows
            if self.shape[1:] != other.shape[1:]:
                raise ShapeError("Tables must have same shape except first dimension")
            
            merged_data = self.data + other.data
            return Table(merged_data)
        
        elif axis == 1:
            # Merge along columns (only for 2D)
            if self.ndim != 2:
                raise DimensionMismatchError("Column merge only works for 2D tables")
            
            if self.shape[0] != other.shape[0]:
                raise ShapeError("Tables must have same number of rows")
            
            result = Table.create_2d(self.shape[0], 
                                    self.shape[1] + other.shape[1])
            
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.set_element([i, j], self.get_element([i, j]))
                for j in range(other.shape[1]):
                    result.set_element([i, self.shape[1] + j], 
                                     other.get_element([i, j]))
            
            return result
        
        else:
            raise ValueError(f"Invalid axis: {axis}")
    
    def split(self, axis: int, indices: List[int]) -> List['Table']:
        """
        Split table along an axis at specified indices.
        
        Args:
            axis: Axis along which to split
            indices: Indices where to split
            
        Returns:
            List of split tables
        """
        if axis >= self.ndim:
            raise ValueError(f"Axis {axis} invalid for {self.ndim}D table")
        
        # Convert single axis operations to slicing
        split_points = [0] + sorted(set(indices)) + [self.shape[axis]]
        tables = []
        
        for i in range(len(split_points) - 1):
            slice_spec = []
            for d in range(self.ndim):
                if d == axis:
                    slice_spec.append(slice(split_points[i], split_points[i + 1]))
                else:
                    slice_spec.append(slice(None))
            
            tables.append(self.slice(slice_spec))
        
        return [t for t in tables if t.size > 0]
    
    def apply(self, func: Callable[[Any], Any]) -> 'Table':
        """
        Apply a function to all elements.
        
        Args:
            func: Function to apply to each element
            
        Returns:
            Table: Table with function applied
        """
        def apply_recursive(data: Any) -> Any:
            if isinstance(data, list):
                return [apply_recursive(item) for item in data]
            return func(data)
        
        return Table(apply_recursive(self.data))
    
    def map_values(self, mapping: dict) -> 'Table':
        """
        Map values using a dictionary.
        
        Args:
            mapping: Dictionary of old_value -> new_value
            
        Returns:
            Table: Table with mapped values
        """
        return self.apply(lambda x: mapping.get(x, x))
    
    def filter_elements(self, predicate: Callable[[Any], bool]) -> List[Any]:
        """
        Filter elements based on predicate.
        
        Args:
            predicate: Function returning True for elements to keep
            
        Returns:
            List of elements matching predicate
        """
        def filter_recursive(data: Any) -> List:
            if isinstance(data, list):
                result = []
                for item in data:
                    result.extend(filter_recursive(item))
                return result
            return [data] if predicate(data) else []
        
        return filter_recursive(self.data)
    
    def sum(self) -> Union[int, float]:
        """Calculate sum of all elements."""
        flat = self.flatten().data
        try:
            return sum(flat)
        except TypeError:
            raise TableError("Cannot sum non-numeric elements")
    
    def mean(self) -> float:
        """Calculate mean of all elements."""
        if self.size == 0:
            raise TableError("Cannot calculate mean of empty table")
        return self.sum() / self.size
    
    def min(self) -> Any:
        """Find minimum element."""
        flat = self.flatten().data
        if not flat:
            raise TableError("Cannot find min of empty table")
        return min(flat)
    
    def max(self) -> Any:
        """Find maximum element."""
        flat = self.flatten().data
        if not flat:
            raise TableError("Cannot find max of empty table")
        return max(flat)
    
    def fill(self, value: Any) -> None:
        """
        Fill all elements with a value.
        
        Args:
            value: Value to fill with
        """
        def fill_recursive(data: Any) -> Any:
            if isinstance(data, list):
                return [fill_recursive(item) for item in data]
            return value
        
        self.data = fill_recursive(self.data)
    
    def pad(self, pad_size: int, fill: Any = 0) -> 'Table':
        """
        Pad all dimensions.
        
        Args:
            pad_size: Size of padding on each side
            fill: Value to pad with
            
        Returns:
            Table: Padded table
        """
        if self.ndim == 1:
            return Table([fill] * pad_size + self.data + [fill] * pad_size)
        
        elif self.ndim == 2:
            rows, cols = self.shape
            new_rows = rows + 2 * pad_size
            new_cols = cols + 2 * pad_size
            
            result = Table.create_2d(new_rows, new_cols, fill)
            
            for i in range(rows):
                for j in range(cols):
                    result.set_element([i + pad_size, j + pad_size],
                                     self.get_element([i, j]))
            
            return result
        
        else:
            raise NotImplementedError("Padding for >2D not yet implemented")
    
    def rotate_2d_90(self) -> 'Table':
        """Rotate 2D table 90 degrees clockwise."""
        if self.ndim != 2:
            raise DimensionMismatchError("Rotation only works on 2D tables")
        
        rows, cols = self.shape
        result = Table.create_2d(cols, rows)
        
        for i in range(rows):
            for j in range(cols):
                result.set_element([j, rows - 1 - i], self.get_element([i, j]))
        
        return result
    
    def copy(self) -> 'Table':
        """Create a deep copy of the table."""
        return Table(deepcopy(self.data))
    
    def to_list(self) -> List:
        """Convert to nested list."""
        return deepcopy(self.data)
    
    def to_dict(self) -> dict:
        """Convert to dictionary format."""
        return {
            'data': self.data,
            'shape': self.shape,
            'ndim': self.ndim,
            'size': self.size
        }
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict())
    
    @staticmethod
    def from_json(json_str: str) -> 'Table':
        """Create table from JSON string."""
        data = json.loads(json_str)
        return Table(data['data'])
    
    def to_csv(self) -> str:
        """Convert 2D table to CSV format."""
        if self.ndim != 2:
            raise DimensionMismatchError("CSV export only works for 2D tables")
        
        lines = []
        for i in range(self.shape[0]):
            row = [str(self.get_element([i, j])) for j in range(self.shape[1])]
            lines.append(','.join(row))
        
        return '\n'.join(lines)
    
    @staticmethod
    def from_csv(csv_str: str) -> 'Table':
        """Create 2D table from CSV string."""
        lines = csv_str.strip().split('\n')
        data = []
        for line in lines:
            row = []
            for cell in line.split(','):
                try:
                    row.append(int(cell))
                except ValueError:
                    try:
                        row.append(float(cell))
                    except ValueError:
                        row.append(cell)
            data.append(row)
        
        return Table(data)
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Table(shape={self.shape}, ndim={self.ndim})"
    
    def __str__(self) -> str:
        """Pretty print representation."""
        return f"Table{self.shape}:\n{self.data}"
    
    def __len__(self) -> int:
        """Length of first dimension."""
        return self.shape[0] if self.shape else 0
    
    def __getitem__(self, key: Union[int, tuple]) -> Any:
        """Index access."""
        if isinstance(key, int):
            return Table(self.data[key])
        elif isinstance(key, tuple):
            return self.get_element(key)
        else:
            raise TypeError(f"Invalid index type: {type(key)}")
    
    def __setitem__(self, key: Union[int, tuple], value: Any) -> None:
        """Index assignment."""
        if isinstance(key, tuple):
            self.set_element(key, value)
        else:
            raise TypeError(f"Invalid index type: {type(key)}")
    
    def __eq__(self, other: 'Table') -> bool:
        """Equality comparison."""
        if not isinstance(other, Table):
            return False
        return self.data == other.data
    
    def __add__(self, other: 'Table') -> 'Table':
        """Element-wise addition."""
        if self.shape != other.shape:
            raise ShapeError("Tables must have same shape for addition")
        
        def add_recursive(d1: Any, d2: Any) -> Any:
            if isinstance(d1, list):
                return [add_recursive(a, b) for a, b in zip(d1, d2)]
            return d1 + d2
        
        return Table(add_recursive(self.data, other.data))
    
    def __mul__(self, scalar: Union[int, float]) -> 'Table':
        """Scalar multiplication."""
        return self.apply(lambda x: x * scalar)
