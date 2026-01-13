# -*- coding: utf-8 -*-
"""
MultiDimTable: A simple, powerful module for managing multidimensional tables.

Supports creation, indexing, reshaping, slicing, merging and conversion of 
1D, 2D, 3D and n-dimensional arrays/tables.

Author: MIDInosaure
License: MIT
"""

from typing import Any, List, Tuple, Union, Optional, Iterator
from copy import deepcopy
import itertools


class ShapeError(Exception):
    """Raised when shape or dimension mismatch occurs."""
    pass


class IndexError_(Exception):
    """Raised when index is out of bounds."""
    pass


class MultiDimTable:
    """
    A flexible, easy-to-use multidimensional table/array class.
    
    Supports 1D, 2D, 3D and n-dimensional data structures with common operations
    like slicing, reshaping, merging, conversion, and element access.
    
    Examples:
        >>> # Create a 2D table
        >>> t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        >>> t.shape
        (2, 3)
        >>> t[0, 1]
        2
        
        >>> # Create a 3D table
        >>> t3d = MultiDimTable.create((2, 3, 4), fill=0)
        >>> t3d.shape
        (2, 3, 4)
        
        >>> # Reshape
        >>> flat = t.flatten()
        >>> flat.shape
        (6,)
        >>> reshaped = flat.reshape((3, 2))
        >>> reshaped.shape
        (3, 2)
    """
    
    def __init__(self, data: Union[List, "MultiDimTable"]):
        """
        Initialize a MultiDimTable from nested lists or another MultiDimTable.
        
        Args:
            data: Nested list structure or MultiDimTable instance.
        
        Raises:
            ShapeError: If nested lists have inconsistent dimensions.
        """
        if isinstance(data, MultiDimTable):
            self._data = deepcopy(data._data)
            self._shape = tuple(data._shape)
        else:
            self._data = self._validate_and_convert(data)
            self._shape = self._compute_shape()
    
    @staticmethod
    def create(shape: Tuple[int, ...], fill: Any = None) -> "MultiDimTable":
        """
        Create a MultiDimTable of given shape filled with a default value.
        
        Args:
            shape: Tuple of dimensions (e.g., (2, 3, 4) for 2x3x4 table).
            fill: Default value to fill (default: None).
        
        Returns:
            A new MultiDimTable initialized with the fill value.
        
        Example:
            >>> t = MultiDimTable.create((2, 3), fill=0)
            >>> t.shape
            (2, 3)
        """
        def create_nested(dims: Tuple[int, ...]) -> List:
            if len(dims) == 1:
                return [fill] * dims[0]
            return [create_nested(dims[1:]) for _ in range(dims[0])]
        
        return MultiDimTable(create_nested(shape))
    
    @staticmethod
    def zeros(shape: Tuple[int, ...]) -> "MultiDimTable":
        """Create a table filled with zeros."""
        return MultiDimTable.create(shape, fill=0)
    
    @staticmethod
    def ones(shape: Tuple[int, ...]) -> "MultiDimTable":
        """Create a table filled with ones."""
        return MultiDimTable.create(shape, fill=1)
    
    def _validate_and_convert(self, data: List) -> List:
        """
        Validate nested list structure and ensure consistency.
        
        Raises:
            ShapeError: If dimensions are inconsistent.
        """
        if not isinstance(data, list):
            raise ShapeError(f"Expected list, got {type(data)}")
        
        if len(data) == 0:
            return []
        
        if not isinstance(data[0], list):
            # 1D array
            return data
        
        # Check consistency of inner dimensions
        first_shape = self._get_list_shape(data[0])
        for item in data[1:]:
            if self._get_list_shape(item) != first_shape:
                raise ShapeError("Inconsistent dimensions in nested lists")
        
        return data
    
    @staticmethod
    def _get_list_shape(lst: List) -> Tuple[int, ...]:
        """Recursively compute shape of a nested list."""
        if not isinstance(lst, list):
            return ()
        if len(lst) == 0:
            return (0,)
        if not isinstance(lst[0], list):
            return (len(lst),)
        inner_shape = MultiDimTable._get_list_shape(lst[0])
        return (len(lst),) + inner_shape
    
    def _compute_shape(self) -> Tuple[int, ...]:
        """Compute the shape tuple of the table."""
        if not self._data:
            return (0,)
        return self._get_list_shape(self._data)
    
    @property
    def shape(self) -> Tuple[int, ...]:
        """Return the shape of the table."""
        return self._shape
    
    @property
    def ndim(self) -> int:
        """Return the number of dimensions."""
        return len(self._shape)
    
    @property
    def size(self) -> int:
        """Return the total number of elements."""
        result = 1
        for dim in self._shape:
            result *= dim
        return result
    
    def _get_element(self, indices: Union[int, Tuple[int, ...]]) -> Any:
        """Get element by index/indices."""
        if isinstance(indices, int):
            indices = (indices,)
        
        current = self._data
        for idx in indices:
            if not isinstance(current, list):
                raise IndexError_(f"Index out of bounds: {indices}")
            if idx < 0 or idx >= len(current):
                raise IndexError_(f"Index out of bounds: {indices}")
            current = current[idx]
        return current
    
    def _set_element(self, indices: Union[int, Tuple[int, ...]], value: Any):
        """Set element by index/indices."""
        if isinstance(indices, int):
            indices = (indices,)
        
        current = self._data
        for idx in indices[:-1]:
            if not isinstance(current, list):
                raise IndexError_(f"Index out of bounds: {indices}")
            if idx < 0 or idx >= len(current):
                raise IndexError_(f"Index out of bounds: {indices}")
            current = current[idx]
        
        if not isinstance(current, list):
            raise IndexError_(f"Index out of bounds: {indices}")
        
        final_idx = indices[-1]
        if final_idx < 0 or final_idx >= len(current):
            raise IndexError_(f"Index out of bounds: {indices}")
        
        current[final_idx] = value
    
    def __getitem__(self, index: Union[int, Tuple[int, ...], slice]) -> Any:
        """Get element or slice."""
        if isinstance(index, slice):
            raise NotImplementedError("Slice support not yet implemented")
        return self._get_element(index)
    
    def __setitem__(self, index: Union[int, Tuple[int, ...]], value: Any):
        """Set element."""
        self._set_element(index, value)
    
    def __repr__(self) -> str:
        """String representation."""
        return f"MultiDimTable(shape={self.shape}, ndim={self.ndim})"
    
    def __str__(self) -> str:
        """User-friendly string representation."""
        return self._format_data(self._data)
    
    @staticmethod
    def _format_data(data: Any, indent: int = 0) -> str:
        """Format nested list for display."""
        if not isinstance(data, list):
            return str(data)
        if len(data) == 0:
            return "[]"
        if not isinstance(data[0], list):
            return "[" + ", ".join(str(x) for x in data) + "]"
        
        lines = ["["]
        for i, item in enumerate(data):
            formatted = MultiDimTable._format_data(item, indent + 2)
            comma = "," if i < len(data) - 1 else ""
            lines.append(" " * (indent + 2) + formatted + comma)
        lines.append(" " * indent + "]")
        return "\n".join(lines)
    
    def flatten(self) -> "MultiDimTable":
        """
        Flatten the table to 1D.
        
        Example:
            >>> t = MultiDimTable([[1, 2], [3, 4]])
            >>> flat = t.flatten()
            >>> flat.shape
            (4,)
        """
        flat = []
        
        def recurse(data: Any):
            if isinstance(data, list):
                for item in data:
                    recurse(item)
            else:
                flat.append(data)
        
        recurse(self._data)
        return MultiDimTable(flat)
    
    def reshape(self, new_shape: Tuple[int, ...]) -> "MultiDimTable":
        """
        Reshape the table to new dimensions.
        
        Args:
            new_shape: New shape tuple.
        
        Returns:
            A new MultiDimTable with the requested shape.
        
        Raises:
            ShapeError: If the total size doesn't match.
        
        Example:
            >>> t = MultiDimTable([1, 2, 3, 4, 5, 6])
            >>> t2d = t.reshape((2, 3))
            >>> t2d.shape
            (2, 3)
        """
        if self.size != self._compute_total_size(new_shape):
            raise ShapeError(
                f"Cannot reshape from {self.shape} to {new_shape}: "
                f"size mismatch ({self.size} != "
                f"{self._compute_total_size(new_shape)})"
            )
        
        flat_data = self.flatten()._data
        return self._reshape_from_flat(flat_data, new_shape)
    
    @staticmethod
    def _compute_total_size(shape: Tuple[int, ...]) -> int:
        """Compute total size from shape."""
        if not shape:
            return 0
        result = 1
        for dim in shape:
            result *= dim
        return result
    
    @staticmethod
    def _reshape_from_flat(flat_data: List, shape: Tuple[int, ...]) -> "MultiDimTable":
        """Reshape flat list to nested structure."""
        if len(shape) == 1:
            return MultiDimTable(flat_data)
        
        chunk_size = MultiDimTable._compute_total_size(shape[1:])
        chunks = [
            flat_data[i * chunk_size:(i + 1) * chunk_size]
            for i in range(shape[0])
        ]
        
        if len(shape) == 2:
            return MultiDimTable(chunks)
        
        nested = []
        for chunk in chunks:
            inner = MultiDimTable._reshape_from_flat(chunk, shape[1:])
            nested.append(inner._data)
        
        return MultiDimTable(nested)
    
    def transpose(self) -> "MultiDimTable":
        """
        Transpose a 2D table (swap rows and columns).
        
        Example:
            >>> t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
            >>> t.shape
            (2, 3)
            >>> tp = t.transpose()
            >>> tp.shape
            (3, 2)
        """
        if self.ndim != 2:
            raise ShapeError("Transpose only supported for 2D tables")
        
        new_data = [
            [self._data[i][j] for i in range(len(self._data))]
            for j in range(len(self._data[0]))
        ]
        return MultiDimTable(new_data)
    
    def concatenate(self, other: "MultiDimTable", axis: int = 0) -> "MultiDimTable":
        """
        Concatenate with another table along an axis.
        
        Args:
            other: Another MultiDimTable.
            axis: Axis along which to concatenate (0=rows, 1=columns, etc).
        
        Returns:
            New concatenated MultiDimTable.
        
        Example:
            >>> t1 = MultiDimTable([[1, 2], [3, 4]])
            >>> t2 = MultiDimTable([[5, 6]])
            >>> t3 = t1.concatenate(t2, axis=0)
            >>> t3.shape
            (3, 2)
        """
        if self.ndim != other.ndim:
            raise ShapeError(
                f"Cannot concatenate tables with different dimensions: "
                f"{self.ndim} vs {other.ndim}"
            )
        
        for i, (s1, s2) in enumerate(zip(self.shape, other.shape)):
            if i != axis and s1 != s2:
                raise ShapeError(
                    f"Shapes {self.shape} and {other.shape} not compatible "
                    f"for concatenation on axis {axis}"
                )
        
        if axis == 0:
            return MultiDimTable(self._data + other._data)
        else:
            # For higher axes, recursively concatenate inner tables
            new_data = [
                MultiDimTable(self._data[i]).concatenate(
                    MultiDimTable(other._data[i]), axis - 1
                )._data
                for i in range(len(self._data))
            ]
            return MultiDimTable(new_data)
    
    def split(self, indices_or_sections: Union[int, List[int]], axis: int = 0) -> List["MultiDimTable"]:
        """
        Split table into multiple parts.
        
        Args:
            indices_or_sections: Either number of equal parts or list of indices.
            axis: Axis along which to split.
        
        Returns:
            List of MultiDimTable objects.
        
        Example:
            >>> t = MultiDimTable([[1, 2, 3, 4], [5, 6, 7, 8]])
            >>> parts = t.split(2, axis=1)
            >>> len(parts)
            2
            >>> parts[0].shape
            (2, 2)
        """
        if axis != 0:
            raise NotImplementedError("Split only supported on axis=0 currently")
        
        if isinstance(indices_or_sections, int):
            # Equal split
            n_parts = indices_or_sections
            if len(self._data) % n_parts != 0:
                raise ShapeError(
                    f"Cannot split {len(self._data)} items into "
                    f"{n_parts} equal parts"
                )
            chunk_size = len(self._data) // n_parts
            indices = [i * chunk_size for i in range(1, n_parts)]
        else:
            indices = indices_or_sections
        
        # Convert indices to split points
        result = []
        prev = 0
        for idx in indices:
            result.append(MultiDimTable(self._data[prev:idx]))
            prev = idx
        result.append(MultiDimTable(self._data[prev:]))
        
        return result
    
    def stack(self, tables: List["MultiDimTable"], axis: int = 0) -> "MultiDimTable":
        """
        Stack multiple tables together along a new axis.
        
        Args:
            tables: List of MultiDimTable objects to stack with self.
            axis: New axis position.
        
        Returns:
            Stacked MultiDimTable.
        
        Example:
            >>> t1 = MultiDimTable([1, 2, 3])
            >>> t2 = MultiDimTable([4, 5, 6])
            >>> stacked = t1.stack([t2], axis=0)
            >>> stacked.shape
            (2, 3)
        """
        all_tables = [self] + tables
        
        # Check all have same shape
        first_shape = all_tables[0].shape
        for t in all_tables[1:]:
            if t.shape != first_shape:
                raise ShapeError(f"All tables must have same shape")
        
        if axis == 0:
            combined = []
            for t in all_tables:
                combined.append(t._data)
            return MultiDimTable(combined)
        else:
            raise NotImplementedError("Stack only supported on axis=0 currently")
    
    def to_list(self) -> List:
        """
        Convert to nested Python list.
        
        Example:
            >>> t = MultiDimTable([[1, 2], [3, 4]])
            >>> t.to_list()
            [[1, 2], [3, 4]]
        """
        return deepcopy(self._data)
    
    def to_flat_list(self) -> List:
        """
        Convert to flat Python list.
        
        Example:
            >>> t = MultiDimTable([[1, 2], [3, 4]])
            >>> t.to_flat_list()
            [1, 2, 3, 4]
        """
        return self.flatten()._data
    
    def copy(self) -> "MultiDimTable":
        """Create a deep copy of the table."""
        return MultiDimTable(self)
    
    def apply(self, func) -> "MultiDimTable":
        """
        Apply a function to each element.
        
        Args:
            func: Function to apply.
        
        Returns:
            New MultiDimTable with function applied.
        
        Example:
            >>> t = MultiDimTable([[1, 2], [3, 4]])
            >>> t2 = t.apply(lambda x: x * 2)
            >>> t2.to_list()
            [[2, 4], [6, 8]]
        """
        def apply_recursive(data):
            if isinstance(data, list):
                return [apply_recursive(item) for item in data]
            return func(data)
        
        return MultiDimTable(apply_recursive(self._data))
    
    def iterate(self) -> Iterator[Any]:
        """
        Iterate over all elements (flattened).
        
        Example:
            >>> t = MultiDimTable([[1, 2], [3, 4]])
            >>> list(t.iterate())
            [1, 2, 3, 4]
        """
        def recurse(data):
            if isinstance(data, list):
                for item in data:
                    yield from recurse(item)
            else:
                yield data
        
        return recurse(self._data)
    
    def sum(self) -> Union[int, float]:
        """Sum all elements."""
        try:
            return sum(self.iterate())
        except TypeError:
            raise TypeError("Cannot sum non-numeric elements")
    
    def mean(self) -> float:
        """Compute mean of all elements."""
        try:
            total = sum(self.iterate())
            return total / self.size
        except TypeError:
            raise TypeError("Cannot compute mean of non-numeric elements")
    
    def min(self) -> Any:
        """Find minimum element."""
        return min(self.iterate())
    
    def max(self) -> Any:
        """Find maximum element."""
        return max(self.iterate())
