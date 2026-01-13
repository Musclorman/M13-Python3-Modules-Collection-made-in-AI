"""
Examples of Multi-Dimensional Table Usage

This file contains 15+ practical examples showing how to use the Table module
for various operations with 1D, 2D, 3D, and higher dimensional arrays.
"""

from multitable import Table


def example_1_basic_1d_creation():
    """Example 1: Create and use basic 1D table."""
    print("\n=== Example 1: Basic 1D Table ===")
    
    # Create 1D table
    t = Table.create_1d(5, fill=0)
    print(f"Created 1D table: {t}")
    
    # Set some values
    for i in range(5):
        t.set_element([i], i * 10)
    
    print(f"After setting values: {t.data}")
    print(f"Shape: {t.shape}, Size: {t.size}")


def example_2_basic_2d_creation():
    """Example 2: Create and use basic 2D table."""
    print("\n=== Example 2: Basic 2D Table ===")
    
    # Create 2D table
    t = Table.create_2d(3, 4, fill=0)
    print(f"Created 2D table: {t}")
    
    # Fill with pattern
    for i in range(3):
        for j in range(4):
            t.set_element([i, j], i * 4 + j)
    
    print(f"Shape: {t.shape}")
    print(f"Data: {t.data}")


def example_3_3d_table():
    """Example 3: Create and use 3D table."""
    print("\n=== Example 3: 3D Table ===")
    
    # Create 3D table (cube)
    t = Table.create_3d(3, 3, 3, fill=0)
    
    # Fill with sequential numbers
    counter = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                t.set_element([i, j, k], counter)
                counter += 1
    
    print(f"Created 3D table: {t}")
    print(f"Element at [1, 1, 1]: {t.get_element([1, 1, 1])}")
    print(f"Element at [2, 2, 2]: {t.get_element([2, 2, 2])}")


def example_4_nd_table():
    """Example 4: Create arbitrary n-dimensional table."""
    print("\n=== Example 4: 4D Table ===")
    
    # Create 4D table
    t = Table.create_nd((2, 3, 4, 5), fill=42)
    print(f"Created 4D table: {t}")
    print(f"Total elements: {t.size}")


def example_5_flatten_reshape():
    """Example 5: Flatten and reshape operations."""
    print("\n=== Example 5: Flatten & Reshape ===")
    
    # Create 2D table
    t = Table.create_2d(3, 4, fill=0)
    for i in range(3):
        for j in range(4):
            t.set_element([i, j], i * 4 + j + 1)
    
    print(f"Original shape: {t.shape}")
    print(f"Original data: {t.data}")
    
    # Flatten to 1D
    flat = t.flatten()
    print(f"Flattened shape: {flat.shape}")
    print(f"Flattened data: {flat.data}")
    
    # Reshape to different dimensions
    reshaped = flat.reshape((4, 3))
    print(f"Reshaped to (4, 3): {reshaped.data}")
    
    reshaped_2 = flat.reshape((2, 2, 3))
    print(f"Reshaped to (2, 2, 3): shape = {reshaped_2.shape}")


def example_6_slicing():
    """Example 6: Slicing operations."""
    print("\n=== Example 6: Slicing ===")
    
    # Create 2D table
    t = Table([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]])
    
    print(f"Original table:\n{t.data}")
    
    # Slice rows
    row_slice = t.slice([slice(1, 3), slice(None)])
    print(f"\nSlice rows [1:3]: {row_slice.data}")
    
    # Slice columns
    col_slice = t.slice([slice(None), slice(1, 3)])
    print(f"Slice columns [:, 1:3]: {col_slice.data}")
    
    # Slice both
    sub_matrix = t.slice([slice(1, 3), slice(1, 3)])
    print(f"Submatrix [1:3, 1:3]: {sub_matrix.data}")


def example_7_transpose():
    """Example 7: Transpose operations."""
    print("\n=== Example 7: Transpose ===")
    
    # Create 2D table
    t = Table([[1, 2, 3],
               [4, 5, 6]])
    
    print(f"Original shape: {t.shape}")
    print(f"Original:\n{t.data}")
    
    # Transpose
    transposed = t.transpose_2d()
    print(f"Transposed shape: {transposed.shape}")
    print(f"Transposed:\n{transposed.data}")


def example_8_merge():
    """Example 8: Merge operations."""
    print("\n=== Example 8: Merge ===")
    
    # Create two 2D tables
    t1 = Table([[1, 2],
                [3, 4]])
    
    t2 = Table([[5, 6],
                [7, 8]])
    
    print(f"Table 1:\n{t1.data}")
    print(f"Table 2:\n{t2.data}")
    
    # Merge along rows
    merged_rows = t1.merge(t2, axis=0)
    print(f"Merged along rows (axis=0):\n{merged_rows.data}")
    
    # Merge along columns
    merged_cols = t1.merge(t2, axis=1)
    print(f"Merged along columns (axis=1):\n{merged_cols.data}")


def example_9_split():
    """Example 9: Split operations."""
    print("\n=== Example 9: Split ===")
    
    # Create 1D table
    t = Table([1, 2, 3, 4, 5, 6, 7, 8])
    
    print(f"Original: {t.data}")
    
    # Split at single point
    parts = t.split(0, [3])
    print(f"Split at index 3:")
    for i, part in enumerate(parts):
        print(f"  Part {i}: {part.data}")
    
    # Split at multiple points
    parts = t.split(0, [2, 5])
    print(f"Split at indices [2, 5]:")
    for i, part in enumerate(parts):
        print(f"  Part {i}: {part.data}")


def example_10_apply_function():
    """Example 10: Apply function to all elements."""
    print("\n=== Example 10: Apply Function ===")
    
    # Create table
    t = Table([[1, 2, 3],
               [4, 5, 6]])
    
    print(f"Original:\n{t.data}")
    
    # Apply square function
    squared = t.apply(lambda x: x ** 2)
    print(f"Squared:\n{squared.data}")
    
    # Apply custom transformation
    result = t.apply(lambda x: x * 10 + 1)
    print(f"Transformed (x*10+1):\n{result.data}")


def example_11_filter():
    """Example 11: Filter elements."""
    print("\n=== Example 11: Filter ===")
    
    # Create table
    t = Table([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]])
    
    print(f"Original:\n{t.data}")
    
    # Filter even numbers
    evens = t.filter_elements(lambda x: x % 2 == 0)
    print(f"Even numbers: {evens}")
    
    # Filter numbers > 5
    greater_5 = t.filter_elements(lambda x: x > 5)
    print(f"Numbers > 5: {greater_5}")


def example_12_statistics():
    """Example 12: Statistical operations."""
    print("\n=== Example 12: Statistics ===")
    
    # Create table with numbers
    t = Table([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
    
    print(f"Table:\n{t.data}")
    print(f"Sum: {t.sum()}")
    print(f"Mean: {t.mean()}")
    print(f"Min: {t.min()}")
    print(f"Max: {t.max()}")


def example_13_fill_pad():
    """Example 13: Fill and pad operations."""
    print("\n=== Example 13: Fill & Pad ===")
    
    # Create table
    t = Table([[1, 2, 3],
               [4, 5, 6]])
    
    print(f"Original shape: {t.shape}")
    print(f"Original:\n{t.data}")
    
    # Fill with value
    t_filled = t.copy()
    t_filled.fill(0)
    print(f"Filled with 0:\n{t_filled.data}")
    
    # Pad the table
    padded = t.pad(1, fill=0)
    print(f"Padded with size 1:\n{padded.data}")


def example_14_conversions():
    """Example 14: Format conversions."""
    print("\n=== Example 14: Format Conversions ===")
    
    # Create table
    t = Table([[1, 2, 3],
               [4, 5, 6]])
    
    print(f"Original:\n{t.data}")
    
    # Convert to CSV
    csv = t.to_csv()
    print(f"As CSV:\n{csv}")
    
    # Convert from CSV
    t_restored = Table.from_csv(csv)
    print(f"Restored from CSV:\n{t_restored.data}")
    
    # Convert to dict
    dict_repr = t.to_dict()
    print(f"As dict keys: {dict_repr.keys()}")
    
    # Convert to JSON and back
    json_str = t.to_json()
    t_json = Table.from_json(json_str)
    print(f"Restored from JSON: {t_json.shape}")


def example_15_rotate():
    """Example 15: Rotation operations."""
    print("\n=== Example 15: Rotation ===")
    
    # Create 2D table
    t = Table([[1, 2, 3],
               [4, 5, 6]])
    
    print(f"Original shape {t.shape}:\n{t.data}")
    
    # Rotate 90 degrees
    rotated = t.rotate_2d_90()
    print(f"Rotated 90° shape {rotated.shape}:\n{rotated.data}")


def example_16_complex_workflow():
    """Example 16: Complex workflow combining multiple operations."""
    print("\n=== Example 16: Complex Workflow ===")
    
    print("Create a 3x4 table and perform multiple operations:")
    
    # Step 1: Create table
    t = Table.from_list([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12]])
    print(f"1. Created table shape {t.shape}")
    
    # Step 2: Apply transformation
    t = t.apply(lambda x: x * 2)
    print(f"2. Applied x*2 transformation")
    
    # Step 3: Filter even (all should be even now)
    evens = t.filter_elements(lambda x: x > 10)
    print(f"3. Filtered values > 10: {evens}")
    
    # Step 4: Flatten and get statistics
    flat = t.flatten()
    print(f"4. Flattened. Sum={flat.sum()}, Mean={flat.mean()}")
    
    # Step 5: Reshape
    reshaped = flat.reshape((4, 3))
    print(f"5. Reshaped to {reshaped.shape}")
    
    # Step 6: Slice and transpose
    sliced = reshaped.slice([slice(None), slice(0, 2)])
    print(f"6. Sliced to {sliced.shape}")
    
    transposed = sliced.transpose_2d()
    print(f"7. Transposed to {transposed.shape}")


def example_17_copy_independence():
    """Example 17: Copy independence."""
    print("\n=== Example 17: Copy Independence ===")
    
    # Create original
    t1 = Table([[1, 2], [3, 4]])
    print(f"Original: {t1.data}")
    
    # Create copy
    t2 = t1.copy()
    
    # Modify copy
    t2.set_element([0, 0], 999)
    
    print(f"After modifying copy:")
    print(f"  Original: {t1.data}")
    print(f"  Copy: {t2.data}")


def example_18_map_values():
    """Example 18: Map values."""
    print("\n=== Example 18: Map Values ===")
    
    # Create table with categorical data
    t = Table([[1, 2, 1], [2, 1, 2]])
    print(f"Original (1=yes, 2=no):\n{t.data}")
    
    # Map values
    mapping = {1: 'yes', 2: 'no'}
    mapped = t.map_values(mapping)
    print(f"Mapped:\n{mapped.data}")


def example_19_arithmetic():
    """Example 19: Arithmetic operations."""
    print("\n=== Example 19: Arithmetic Operations ===")
    
    # Create tables
    t1 = Table([1, 2, 3, 4])
    t2 = Table([10, 20, 30, 40])
    
    print(f"Table 1: {t1.data}")
    print(f"Table 2: {t2.data}")
    
    # Element-wise addition
    result = t1 + t2
    print(f"Addition: {result.data}")
    
    # Scalar multiplication
    scaled = t1 * 5
    print(f"Multiplied by 5: {scaled.data}")


# Run all examples
if __name__ == '__main__':
    example_1_basic_1d_creation()
    example_2_basic_2d_creation()
    example_3_3d_table()
    example_4_nd_table()
    example_5_flatten_reshape()
    example_6_slicing()
    example_7_transpose()
    example_8_merge()
    example_9_split()
    example_10_apply_function()
    example_11_filter()
    example_12_statistics()
    example_13_fill_pad()
    example_14_conversions()
    example_15_rotate()
    example_16_complex_workflow()
    example_17_copy_independence()
    example_18_map_values()
    example_19_arithmetic()
    
    print("\n" + "="*50)
    print("All examples completed successfully!")
    print("="*50)
