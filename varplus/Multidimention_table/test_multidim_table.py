# -*- coding: utf-8 -*-
"""
Comprehensive test suite for MultiDimTable module.

Tests cover:
- Creation and initialization
- Shape and dimension properties
- Element access (get/set)
- Flattening and reshaping
- Transposition
- Concatenation and splitting
- Stacking
- Conversion operations
- Iteration and aggregation
- Error handling
- Edge cases
"""

import sys
import unittest
from typing import List
from Multidimention_table import MultiDimTable, ShapeError, IndexError_


class TestMultiDimTableCreation(unittest.TestCase):
    """Test table creation and initialization."""
    
    def test_create_from_1d_list(self):
        """Test creation from 1D list."""
        t = MultiDimTable([1, 2, 3, 4, 5])
        self.assertEqual(t.shape, (5,))
        self.assertEqual(t.ndim, 1)
        self.assertEqual(t.size, 5)
    
    def test_create_from_2d_list(self):
        """Test creation from 2D nested list."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(t.shape, (2, 3))
        self.assertEqual(t.ndim, 2)
        self.assertEqual(t.size, 6)
    
    def test_create_from_3d_list(self):
        """Test creation from 3D nested list."""
        data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        t = MultiDimTable(data)
        self.assertEqual(t.shape, (2, 2, 2))
        self.assertEqual(t.ndim, 3)
        self.assertEqual(t.size, 8)
    
    def test_create_4d_array(self):
        """Test creation of 4D array."""
        data = [[[[1]]]]
        t = MultiDimTable(data)
        self.assertEqual(t.shape, (1, 1, 1, 1))
        self.assertEqual(t.ndim, 4)
    
    def test_create_with_create_method(self):
        """Test create() class method."""
        t = MultiDimTable.create((3, 4, 5), fill=0)
        self.assertEqual(t.shape, (3, 4, 5))
        self.assertEqual(t.size, 60)
        self.assertEqual(t[0, 0, 0], 0)
    
    def test_zeros_creation(self):
        """Test zeros() class method."""
        t = MultiDimTable.zeros((2, 3))
        self.assertEqual(t.shape, (2, 3))
        for val in t.iterate():
            self.assertEqual(val, 0)
    
    def test_ones_creation(self):
        """Test ones() class method."""
        t = MultiDimTable.ones((2, 3))
        self.assertEqual(t.shape, (2, 3))
        for val in t.iterate():
            self.assertEqual(val, 1)
    
    def test_copy_constructor(self):
        """Test creation from another MultiDimTable."""
        t1 = MultiDimTable([[1, 2], [3, 4]])
        t2 = MultiDimTable(t1)
        self.assertEqual(t1.shape, t2.shape)
        self.assertEqual(t1.to_list(), t2.to_list())
        # Ensure deep copy
        t2[0, 0] = 99
        self.assertNotEqual(t1[0, 0], t2[0, 0])
    
    def test_empty_list_handling(self):
        """Test handling of empty lists."""
        t = MultiDimTable([])
        self.assertEqual(t.shape, (0,))
        self.assertEqual(t.size, 0)
    
    def test_inconsistent_dimensions_error(self):
        """Test error on inconsistent nested list dimensions."""
        with self.assertRaises(ShapeError):
            MultiDimTable([[1, 2], [3, 4, 5]])  # Second row longer
    
    def test_invalid_input_type_error(self):
        """Test error on invalid input type."""
        with self.assertRaises(ShapeError):
            MultiDimTable("not a list")


class TestElementAccess(unittest.TestCase):
    """Test element access operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.t1d = MultiDimTable([10, 20, 30, 40])
        self.t2d = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        self.t3d = MultiDimTable.create((2, 3, 2), fill=5)
    
    def test_1d_element_access(self):
        """Test accessing 1D elements."""
        self.assertEqual(self.t1d[0], 10)
        self.assertEqual(self.t1d[1], 20)
        self.assertEqual(self.t1d[3], 40)
    
    def test_2d_element_access(self):
        """Test accessing 2D elements."""
        self.assertEqual(self.t2d[0, 0], 1)
        self.assertEqual(self.t2d[0, 2], 3)
        self.assertEqual(self.t2d[1, 1], 5)
        self.assertEqual(self.t2d[1, 2], 6)
    
    def test_3d_element_access(self):
        """Test accessing 3D elements."""
        self.assertEqual(self.t3d[0, 0, 0], 5)
        self.assertEqual(self.t3d[1, 2, 1], 5)
    
    def test_element_modification_1d(self):
        """Test modifying 1D elements."""
        self.t1d[0] = 100
        self.assertEqual(self.t1d[0], 100)
    
    def test_element_modification_2d(self):
        """Test modifying 2D elements."""
        self.t2d[0, 0] = 99
        self.assertEqual(self.t2d[0, 0], 99)
        self.t2d[1, 2] = -5
        self.assertEqual(self.t2d[1, 2], -5)
    
    def test_element_modification_3d(self):
        """Test modifying 3D elements."""
        self.t3d[0, 1, 0] = 123
        self.assertEqual(self.t3d[0, 1, 0], 123)
    
    def test_out_of_bounds_access_raises_error(self):
        """Test IndexError_ on out of bounds access."""
        with self.assertRaises(IndexError_):
            _ = self.t1d[100]
    
    def test_negative_index_raises_error(self):
        """Test that negative indices raise error."""
        with self.assertRaises(IndexError_):
            _ = self.t1d[-1]
    
    def test_2d_out_of_bounds(self):
        """Test out of bounds in 2D."""
        with self.assertRaises(IndexError_):
            _ = self.t2d[5, 5]
    
    def test_row_access_2d(self):
        """Test accessing entire row in 2D table."""
        row = self.t2d[0]
        self.assertEqual(row, [1, 2, 3])
        row = self.t2d[1]
        self.assertEqual(row, [4, 5, 6])


class TestShapeAndDimensions(unittest.TestCase):
    """Test shape and dimension properties."""
    
    def test_shape_property_1d(self):
        """Test shape property for 1D."""
        t = MultiDimTable([1, 2, 3])
        self.assertEqual(t.shape, (3,))
    
    def test_shape_property_2d(self):
        """Test shape property for 2D."""
        t = MultiDimTable([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(t.shape, (3, 2))
    
    def test_shape_property_3d(self):
        """Test shape property for 3D."""
        t = MultiDimTable([[[1]], [[2]]])
        self.assertEqual(t.shape, (2, 1, 1))
    
    def test_ndim_property(self):
        """Test ndim property."""
        t1d = MultiDimTable([1, 2, 3])
        t2d = MultiDimTable([[1, 2], [3, 4]])
        t3d = MultiDimTable([[[1, 2], [3, 4]]])
        
        self.assertEqual(t1d.ndim, 1)
        self.assertEqual(t2d.ndim, 2)
        self.assertEqual(t3d.ndim, 3)
    
    def test_size_property(self):
        """Test size property."""
        t = MultiDimTable.create((2, 3, 4), fill=0)
        self.assertEqual(t.size, 24)
        
        t = MultiDimTable([1, 2, 3, 4, 5])
        self.assertEqual(t.size, 5)


class TestFlattening(unittest.TestCase):
    """Test flattening operations."""
    
    def test_flatten_2d_to_1d(self):
        """Test flattening 2D to 1D."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        flat = t.flatten()
        self.assertEqual(flat.shape, (6,))
        self.assertEqual(flat.to_list(), [1, 2, 3, 4, 5, 6])
    
    def test_flatten_3d_to_1d(self):
        """Test flattening 3D to 1D."""
        t = MultiDimTable([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        flat = t.flatten()
        self.assertEqual(flat.shape, (8,))
        self.assertEqual(flat.to_list(), [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_flatten_already_1d(self):
        """Test flattening already 1D array."""
        t = MultiDimTable([1, 2, 3])
        flat = t.flatten()
        self.assertEqual(flat.shape, (3,))
        self.assertEqual(flat.to_list(), [1, 2, 3])
    
    def test_flatten_preserves_order(self):
        """Test that flatten preserves row-major order."""
        t = MultiDimTable([[1, 2], [3, 4], [5, 6]])
        flat = t.flatten()
        self.assertEqual(flat.to_list(), [1, 2, 3, 4, 5, 6])


class TestReshaping(unittest.TestCase):
    """Test reshaping operations."""
    
    def test_reshape_1d_to_2d(self):
        """Test reshaping 1D to 2D."""
        t = MultiDimTable([1, 2, 3, 4, 5, 6])
        reshaped = t.reshape((2, 3))
        self.assertEqual(reshaped.shape, (2, 3))
        self.assertEqual(reshaped.to_list(), [[1, 2, 3], [4, 5, 6]])
    
    def test_reshape_2d_to_1d(self):
        """Test reshaping 2D to 1D."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        reshaped = t.reshape((6,))
        self.assertEqual(reshaped.shape, (6,))
        self.assertEqual(reshaped.to_list(), [1, 2, 3, 4, 5, 6])
    
    def test_reshape_1d_to_3d(self):
        """Test reshaping 1D to 3D."""
        t = MultiDimTable(list(range(24)))
        reshaped = t.reshape((2, 3, 4))
        self.assertEqual(reshaped.shape, (2, 3, 4))
        self.assertEqual(reshaped.size, 24)
    
    def test_reshape_2d_to_2d_different_dims(self):
        """Test reshaping 2D to different 2D."""
        t = MultiDimTable([[1, 2, 3, 4, 5, 6]])
        reshaped = t.reshape((3, 2))
        self.assertEqual(reshaped.shape, (3, 2))
    
    def test_reshape_size_mismatch_error(self):
        """Test error on reshape size mismatch."""
        t = MultiDimTable([1, 2, 3, 4, 5])
        with self.assertRaises(ShapeError):
            t.reshape((2, 3))  # 5 != 6
    
    def test_reshape_to_single_column(self):
        """Test reshape to single column."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        reshaped = t.reshape((6, 1))
        self.assertEqual(reshaped.shape, (6, 1))


class TestTransposition(unittest.TestCase):
    """Test transposition operations."""
    
    def test_transpose_2x3_to_3x2(self):
        """Test transpose 2x3 to 3x2."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        tp = t.transpose()
        self.assertEqual(tp.shape, (3, 2))
        self.assertEqual(tp.to_list(), [[1, 4], [2, 5], [3, 6]])
    
    def test_transpose_square_matrix(self):
        """Test transpose of square matrix."""
        t = MultiDimTable([[1, 2], [3, 4]])
        tp = t.transpose()
        self.assertEqual(tp.shape, (2, 2))
        self.assertEqual(tp.to_list(), [[1, 3], [2, 4]])
    
    def test_transpose_1xN(self):
        """Test transpose of row vector."""
        t = MultiDimTable([[1, 2, 3, 4]])
        tp = t.transpose()
        self.assertEqual(tp.shape, (4, 1))
    
    def test_transpose_Nx1(self):
        """Test transpose of column vector."""
        t = MultiDimTable([[1], [2], [3]])
        tp = t.transpose()
        self.assertEqual(tp.shape, (1, 3))
        self.assertEqual(tp.to_list(), [[1, 2, 3]])
    
    def test_transpose_non_2d_raises_error(self):
        """Test error on transpose of non-2D table."""
        t3d = MultiDimTable.create((2, 2, 2), fill=1)
        with self.assertRaises(ShapeError):
            t3d.transpose()
    
    def test_transpose_double_gives_original(self):
        """Test that double transpose gives original."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        double_tp = t.transpose().transpose()
        self.assertEqual(t.to_list(), double_tp.to_list())


class TestConcatenation(unittest.TestCase):
    """Test concatenation operations."""
    
    def test_concatenate_2d_axis0(self):
        """Test concatenate 2D along axis 0."""
        t1 = MultiDimTable([[1, 2], [3, 4]])
        t2 = MultiDimTable([[5, 6]])
        result = t1.concatenate(t2, axis=0)
        self.assertEqual(result.shape, (3, 2))
        self.assertEqual(result.to_list(), [[1, 2], [3, 4], [5, 6]])
    
    def test_concatenate_1d(self):
        """Test concatenate 1D arrays."""
        t1 = MultiDimTable([1, 2, 3])
        t2 = MultiDimTable([4, 5, 6])
        result = t1.concatenate(t2, axis=0)
        self.assertEqual(result.shape, (6,))
        self.assertEqual(result.to_list(), [1, 2, 3, 4, 5, 6])
    
    def test_concatenate_different_ndim_error(self):
        """Test error on concatenating different ndim."""
        t1d = MultiDimTable([1, 2, 3])
        t2d = MultiDimTable([[1, 2]])
        with self.assertRaises(ShapeError):
            t1d.concatenate(t2d, axis=0)
    
    def test_concatenate_incompatible_shapes_error(self):
        """Test error on incompatible shapes."""
        t1 = MultiDimTable([[1, 2, 3]])  # 1x3
        t2 = MultiDimTable([[1, 2]])  # 1x2
        with self.assertRaises(ShapeError):
            t1.concatenate(t2, axis=0)
    
    def test_concatenate_multiple_times(self):
        """Test multiple concatenations."""
        t1 = MultiDimTable([1, 2])
        t2 = MultiDimTable([3, 4])
        t3 = MultiDimTable([5, 6])
        
        result = t1.concatenate(t2, axis=0).concatenate(t3, axis=0)
        self.assertEqual(result.shape, (6,))
        self.assertEqual(result.to_list(), [1, 2, 3, 4, 5, 6])


class TestSplitting(unittest.TestCase):
    """Test splitting operations."""
    
    def test_split_equal_parts(self):
        """Test splitting into equal parts."""
        t = MultiDimTable([[1, 2, 3, 4], [5, 6, 7, 8]])
        parts = t.split(2, axis=0)
        self.assertEqual(len(parts), 2)
        self.assertEqual(parts[0].shape, (1, 4))
        self.assertEqual(parts[1].shape, (1, 4))
    
    def test_split_unequal_error(self):
        """Test error on unequal split."""
        t = MultiDimTable([[1, 2], [3, 4], [5, 6]])
        with self.assertRaises(ShapeError):
            t.split(2, axis=0)  # 3 rows can't split into 2 equal parts
    
    def test_split_by_indices(self):
        """Test splitting by specific indices."""
        t = MultiDimTable([1, 2, 3, 4, 5, 6])
        parts = t.split([2, 4], axis=0)
        self.assertEqual(len(parts), 3)
        self.assertEqual(parts[0].to_list(), [1, 2])
        self.assertEqual(parts[1].to_list(), [3, 4])
        self.assertEqual(parts[2].to_list(), [5, 6])
    
    def test_split_into_single_element(self):
        """Test splitting into single elements."""
        t = MultiDimTable([1, 2, 3])
        parts = t.split(3, axis=0)
        self.assertEqual(len(parts), 3)
        for part in parts:
            self.assertEqual(part.size, 1)


class TestStacking(unittest.TestCase):
    """Test stacking operations."""
    
    def test_stack_1d_arrays(self):
        """Test stacking 1D arrays."""
        t1 = MultiDimTable([1, 2, 3])
        t2 = MultiDimTable([4, 5, 6])
        stacked = t1.stack([t2], axis=0)
        self.assertEqual(stacked.shape, (2, 3))
        self.assertEqual(stacked.to_list(), [[1, 2, 3], [4, 5, 6]])
    
    def test_stack_multiple_arrays(self):
        """Test stacking multiple arrays."""
        t1 = MultiDimTable([1, 2])
        t2 = MultiDimTable([3, 4])
        t3 = MultiDimTable([5, 6])
        
        stacked = t1.stack([t2, t3], axis=0)
        self.assertEqual(stacked.shape, (3, 2))
        self.assertEqual(stacked.to_list(), [[1, 2], [3, 4], [5, 6]])
    
    def test_stack_incompatible_shapes_error(self):
        """Test error on incompatible shapes."""
        t1 = MultiDimTable([1, 2, 3])
        t2 = MultiDimTable([1, 2])
        with self.assertRaises(ShapeError):
            t1.stack([t2], axis=0)
    
    def test_stack_2d_arrays(self):
        """Test stacking 2D arrays."""
        t1 = MultiDimTable([[1, 2], [3, 4]])
        t2 = MultiDimTable([[5, 6], [7, 8]])
        stacked = t1.stack([t2], axis=0)
        self.assertEqual(stacked.shape, (2, 2, 2))


class TestConversion(unittest.TestCase):
    """Test conversion operations."""
    
    def test_to_list(self):
        """Test conversion to nested list."""
        data = [[1, 2, 3], [4, 5, 6]]
        t = MultiDimTable(data)
        self.assertEqual(t.to_list(), data)
    
    def test_to_flat_list(self):
        """Test conversion to flat list."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        flat = t.to_flat_list()
        self.assertEqual(flat, [1, 2, 3, 4, 5, 6])
    
    def test_to_list_preserves_structure(self):
        """Test that to_list preserves original structure."""
        t = MultiDimTable.create((2, 3, 4), fill=5)
        lst = t.to_list()
        self.assertEqual(len(lst), 2)
        self.assertEqual(len(lst[0]), 3)
        self.assertEqual(len(lst[0][0]), 4)
    
    def test_copy(self):
        """Test copy creates independent copy."""
        t1 = MultiDimTable([[1, 2], [3, 4]])
        t2 = t1.copy()
        
        t2[0, 0] = 99
        self.assertNotEqual(t1[0, 0], t2[0, 0])


class TestIteration(unittest.TestCase):
    """Test iteration operations."""
    
    def test_iterate_1d(self):
        """Test iterating 1D array."""
        t = MultiDimTable([1, 2, 3, 4])
        values = list(t.iterate())
        self.assertEqual(values, [1, 2, 3, 4])
    
    def test_iterate_2d(self):
        """Test iterating 2D array."""
        t = MultiDimTable([[1, 2], [3, 4]])
        values = list(t.iterate())
        self.assertEqual(values, [1, 2, 3, 4])
    
    def test_iterate_3d(self):
        """Test iterating 3D array."""
        t = MultiDimTable([[[1, 2], [3, 4]]])
        values = list(t.iterate())
        self.assertEqual(values, [1, 2, 3, 4])
    
    def test_iterate_order(self):
        """Test that iteration order is row-major."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        values = list(t.iterate())
        self.assertEqual(values, [1, 2, 3, 4, 5, 6])


class TestAggregation(unittest.TestCase):
    """Test aggregation operations."""
    
    def test_sum_2d(self):
        """Test sum of 2D array."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(t.sum(), 21)
    
    def test_sum_1d(self):
        """Test sum of 1D array."""
        t = MultiDimTable([1, 2, 3, 4, 5])
        self.assertEqual(t.sum(), 15)
    
    def test_mean(self):
        """Test mean calculation."""
        t = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        self.assertAlmostEqual(t.mean(), 3.5)
    
    def test_min(self):
        """Test minimum element."""
        t = MultiDimTable([[5, 2, 8], [1, 9, 3]])
        self.assertEqual(t.min(), 1)
    
    def test_max(self):
        """Test maximum element."""
        t = MultiDimTable([[5, 2, 8], [1, 9, 3]])
        self.assertEqual(t.max(), 9)
    
    def test_sum_negative_numbers(self):
        """Test sum with negative numbers."""
        t = MultiDimTable([-1, -2, 3, 4])
        self.assertEqual(t.sum(), 4)
    
    def test_mean_with_floats(self):
        """Test mean with floating point numbers."""
        t = MultiDimTable([1.0, 2.0, 3.0])
        self.assertAlmostEqual(t.mean(), 2.0)


class TestApply(unittest.TestCase):
    """Test apply operations."""
    
    def test_apply_simple_function(self):
        """Test applying simple function."""
        t = MultiDimTable([[1, 2], [3, 4]])
        t2 = t.apply(lambda x: x * 2)
        self.assertEqual(t2.to_list(), [[2, 4], [6, 8]])
    
    def test_apply_power_function(self):
        """Test applying power function."""
        t = MultiDimTable([1, 2, 3])
        t2 = t.apply(lambda x: x ** 2)
        self.assertEqual(t2.to_list(), [1, 4, 9])
    
    def test_apply_preserves_shape(self):
        """Test that apply preserves shape."""
        t = MultiDimTable.create((2, 3, 4), fill=5)
        t2 = t.apply(lambda x: x + 1)
        self.assertEqual(t.shape, t2.shape)
    
    def test_apply_with_type_conversion(self):
        """Test apply with type conversion."""
        t = MultiDimTable([1.5, 2.7, 3.2])
        t2 = t.apply(int)
        self.assertEqual(t2.to_list(), [1, 2, 3])
    
    def test_apply_complex_function(self):
        """Test apply with complex function."""
        t = MultiDimTable([0, 1, -1])
        t2 = t.apply(lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero")
        self.assertEqual(t2.to_list(), ["zero", "positive", "negative"])


class TestStringRepresentation(unittest.TestCase):
    """Test string representation."""
    
    def test_repr(self):
        """Test __repr__ method."""
        t = MultiDimTable([[1, 2], [3, 4]])
        r = repr(t)
        self.assertIn("shape=(2, 2)", r)
        self.assertIn("ndim=2", r)
    
    def test_str_1d(self):
        """Test __str__ for 1D."""
        t = MultiDimTable([1, 2, 3])
        s = str(t)
        self.assertIn("1", s)
        self.assertIn("2", s)
        self.assertIn("3", s)
    
    def test_str_2d(self):
        """Test __str__ for 2D."""
        t = MultiDimTable([[1, 2], [3, 4]])
        s = str(t)
        self.assertTrue(len(s) > 0)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios."""
    
    def test_single_element_table(self):
        """Test table with single element."""
        t = MultiDimTable([42])
        self.assertEqual(t.shape, (1,))
        self.assertEqual(t[0], 42)
        self.assertEqual(t.size, 1)
    
    def test_large_dimension_count(self):
        """Test with many dimensions."""
        t = MultiDimTable.create((2, 2, 2, 2, 2), fill=0)
        self.assertEqual(t.ndim, 5)
        self.assertEqual(t.size, 32)
    
    def test_mixed_numeric_types(self):
        """Test with mixed numeric types."""
        t = MultiDimTable([1, 2.5, 3])
        self.assertEqual(t[0], 1)
        self.assertEqual(t[1], 2.5)
        self.assertEqual(t[2], 3)
    
    def test_string_elements(self):
        """Test with string elements."""
        t = MultiDimTable(["a", "b", "c"])
        self.assertEqual(t[0], "a")
        self.assertEqual(t[1], "b")
    
    def test_none_elements(self):
        """Test with None elements."""
        t = MultiDimTable.create((2, 2), fill=None)
        self.assertIsNone(t[0, 0])
    
    def test_heterogeneous_elements(self):
        """Test with mixed element types."""
        t = MultiDimTable([1, "two", 3.0, None])
        self.assertEqual(t[0], 1)
        self.assertEqual(t[1], "two")
        self.assertEqual(t[2], 3.0)
        self.assertIsNone(t[3])


class TestComplexOperations(unittest.TestCase):
    """Test combinations of operations."""
    
    def test_flatten_reshape_roundtrip(self):
        """Test flatten then reshape returns original."""
        original = MultiDimTable([[1, 2, 3], [4, 5, 6]])
        flat = original.flatten()
        restored = flat.reshape((2, 3))
        self.assertEqual(original.to_list(), restored.to_list())
    
    def test_transpose_concatenate_apply(self):
        """Test combining transpose, concatenate, and apply."""
        t1 = MultiDimTable([[1, 2], [3, 4]])
        t2 = MultiDimTable([[5, 6], [7, 8]])
        
        tp1 = t1.transpose()
        combined = tp1.concatenate(t2.transpose(), axis=0)
        result = combined.apply(lambda x: x ** 2)
        
        self.assertEqual(result.shape, (4, 2))
        self.assertEqual(result[0, 0], 1)  # 1^2
        self.assertEqual(result[2, 0], 25)  # 5^2
    
    def test_split_apply_concatenate(self):
        """Test splitting, applying function, then concatenating."""
        t = MultiDimTable([1, 2, 3, 4, 5, 6])
        parts = t.split(2, axis=0)
        
        modified_parts = [part.apply(lambda x: x * 10) for part in parts]
        
        # Manual concatenation since it works on axis 0
        result = modified_parts[0]
        for part in modified_parts[1:]:
            result = result.concatenate(part, axis=0)
        
        self.assertEqual(result.to_list(), [10, 20, 30, 40, 50, 60])


class TestPerformance(unittest.TestCase):
    """Test performance with larger datasets."""
    
    def test_large_1d_array(self):
        """Test with large 1D array."""
        t = MultiDimTable(list(range(10000)))
        self.assertEqual(t.size, 10000)
        self.assertEqual(t.sum(), 49995000)
    
    def test_large_2d_array(self):
        """Test with large 2D array."""
        data = [[i * 100 + j for j in range(100)] for i in range(100)]
        t = MultiDimTable(data)
        self.assertEqual(t.shape, (100, 100))
        self.assertEqual(t.size, 10000)
    
    def test_reshape_large_array(self):
        """Test reshape on large array."""
        t = MultiDimTable(list(range(10000)))
        reshaped = t.reshape((100, 100))
        self.assertEqual(reshaped.shape, (100, 100))
        self.assertEqual(reshaped[50, 50], 5050)


if __name__ == "__main__":
    # Run all tests with verbose output
    unittest.main(verbosity=2)
