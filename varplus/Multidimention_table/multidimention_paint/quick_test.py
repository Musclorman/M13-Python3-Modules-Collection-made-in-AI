"""
Simple test script to verify the MultidimensionalPaint module functionality.
Run from within the multidimention_paint directory.
"""

import sys
import io
sys.path.insert(0, '.')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Import all modules directly
from utils import distance, midpoint, validate_coordinates
from points import Point, PointSet
from shapes import Line, Circle, Rectangle, Square, Ellipse, Arc, ClosedShape
from selection import SelectionEngine
from paint import MultidimensionalPaint

def test_basic():
    """Test basic functionality."""
    print("Testing Basic Functionality...")
    
    painter = MultidimensionalPaint()
    painter.add_point(0, 0)
    painter.add_point(5, 5)
    painter.add_point(10, 10)
    
    assert painter.get_point_count() == 3
    print("[OK] Points added successfully")
    
    points = painter.get_all_points()
    assert len(points) == 3
    print("[OK] All points retrieved")
    
    painter.draw_circle((5, 5), 3)
    painter.draw_rectangle((0, 0), (10, 10))
    assert painter.get_shape_count() == 2
    print("[OK] Shapes drawn successfully")
    
    print("[OK] Basic functionality test PASSED\n")


def test_selection():
    """Test point selection."""
    print("Testing Point Selection...")
    
    painter = MultidimensionalPaint()
    
    # Create a grid of points
    for x in range(0, 11, 2):
        for y in range(0, 11, 2):
            painter.add_point(float(x), float(y))
    
    # Single point selection
    selected = painter.select_single_point((4, 4), tolerance=1.0)
    print(f"[OK] Single point selection: {len(selected)} points")
    
    # Line selection
    selected = painter.select_line((0, 0), (10, 10), tolerance=1.0)
    print(f"[OK] Line selection: {len(selected)} points")
    
    # Region selection
    selected = painter.select_within_region((0, 0), (5, 5))
    print(f"[OK] Region selection: {len(selected)} points")
    
    # Nearest points
    selected = painter.select_nearest((5, 5), count=3)
    assert len(selected) == 3
    print(f"[OK] Nearest points selection: {len(selected)} points")
    
    # All points
    selected = painter.select_all()
    assert len(selected) > 0
    print(f"[OK] Select all: {len(selected)} points")
    
    print("[OK] Point selection test PASSED\n")


def test_shapes():
    """Test all shape types."""
    print("Testing Shape Types...")
    
    painter = MultidimensionalPaint()
    
    painter.draw_line((0, 0), (10, 10))
    print("[OK] Line created")
    
    painter.draw_circle((5, 5), 3)
    print("[OK] Circle created")
    
    painter.draw_rectangle((0, 0), (10, 10))
    print("[OK] Rectangle created")
    
    painter.draw_square((15, 15), 10)
    print("[OK] Square created")
    
    painter.draw_ellipse((20, 20), 8, 5)
    print("[OK] Ellipse created")
    
    import math
    painter.draw_arc((25, 25), 5, 0, math.pi/2)
    print("[OK] Arc created")
    
    vertices = [(30, 30), (35, 30), (32.5, 35)]
    painter.draw_closed_shape(vertices)
    print("[OK] Closed shape created")
    
    assert painter.get_shape_count() == 7
    print("[OK] All shape types test PASSED\n")


def test_analysis():
    """Test analysis functions."""
    print("Testing Analysis Functions...")
    
    painter = MultidimensionalPaint()
    
    # Add points in a grid
    for i in range(1, 6):
        for j in range(1, 6):
            painter.add_point(float(i*2), float(j*2))
    
    # Get statistics
    stats = painter.get_statistics()
    assert stats['point_count'] == 25
    assert stats['dimensions'] == 2
    print(f"[OK] Statistics: {stats['point_count']} points, {stats['dimensions']}D")
    
    # Bounding box
    bbox = painter.get_bounding_box()
    assert bbox is not None
    print(f"[OK] Bounding box: {bbox}")
    
    # Centroid
    centroid = painter.get_centroid()
    assert centroid is not None
    print(f"[OK] Centroid: {centroid.coords}")
    
    # Nearest point
    nearest = painter.find_nearest_point((5, 5))
    assert nearest is not None
    print(f"[OK] Nearest point: {nearest}")
    
    print("[OK] Analysis test PASSED\n")


def test_3d_points():
    """Test 3D point handling."""
    print("Testing 3D Points...")
    
    painter = MultidimensionalPaint()
    
    painter.add_point(0, 0, 0, label="origin")
    painter.add_point(1, 2, 3, label="point_a")
    painter.add_point(4, 5, 6, label="point_b")
    
    assert painter.get_point_count() == 3
    print("[OK] 3D points added")
    
    origin = painter.get_point_by_label("origin")
    assert origin is not None
    assert origin.z == 0
    print(f"[OK] Retrieved 3D point: {origin}")
    
    painter.draw_circle((5, 5, 5), 3)
    print("[OK] 3D circle created")
    
    print("[OK] 3D points test PASSED\n")


def test_utilities():
    """Test utility functions."""
    print("Testing Utility Functions...")
    
    # Distance
    d = distance((0, 0), (3, 4))
    assert d == 5.0
    print(f"[OK] Distance: {d}")
    
    # Midpoint
    mp = midpoint((0, 0), (4, 4))
    assert mp == (2.0, 2.0)
    print(f"[OK] Midpoint: {mp}")
    
    # Validate coordinates
    assert validate_coordinates(1, 2, 3) == True
    assert validate_coordinates(1, "2", 3) == False
    print("[OK] Coordinate validation")
    
    print("[OK] Utility functions test PASSED\n")


def test_metadata():
    """Test point metadata."""
    print("Testing Point Metadata...")
    
    painter = MultidimensionalPaint()
    p = painter.add_point(1, 2)
    
    p.set_metadata("color", "red")
    p.set_metadata("layer", 1)
    
    assert p.get_metadata("color") == "red"
    assert p.get_metadata("layer") == 1
    print("[OK] Point metadata stored and retrieved")
    
    exported = painter.export_points()
    assert len(exported) == 1
    assert exported[0]['metadata']['color'] == "red"
    print("[OK] Metadata exported correctly")
    
    print("[OK] Metadata test PASSED\n")


def run_all_tests():
    """Run all tests."""
    print("="*60)
    print("MultidimensionalPaint Module - Test Suite")
    print("="*60 + "\n")
    
    try:
        test_basic()
        test_selection()
        test_shapes()
        test_analysis()
        test_3d_points()
        test_utilities()
        test_metadata()
        
        print("="*60)
        print("ALL TESTS PASSED! [OK]")
        print("="*60 + "\n")
        
    except AssertionError as e:
        print(f"\n[FAIL] TEST FAILED: {e}\n")
        return False
    except Exception as e:
        print(f"\n[FAIL] ERROR: {e}\n")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
