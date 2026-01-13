"""
Selection engine for MultidimensionalPaint module.

This module provides functionality for selecting points based on various criteria,
including geometric shapes and spatial regions.
"""

from typing import List, Tuple, Optional, Set
try:
    from .points import Point, PointSet
    from .shapes import Shape
    from .utils import bounding_box, points_in_bbox, distance
except ImportError:
    from points import Point, PointSet
    from shapes import Shape
    from utils import bounding_box, points_in_bbox, distance


class SelectionEngine:
    """
    Engine for selecting points based on various criteria.
    """
    
    def __init__(self):
        """Initialize the selection engine."""
        self.selected_points: Set[Point] = set()
        self.selection_history: List[Set[Point]] = []
    
    def select_single_point(self, point_set: PointSet, target: Tuple, 
                           tolerance: float = 0.1) -> List[Tuple]:
        """
        Select a single point.
        
        Args:
            point_set: PointSet to select from
            target: Target coordinates
            tolerance: Selection tolerance
            
        Returns:
            List[Tuple]: Coordinates of selected point(s)
        """
        result = []
        
        for point in point_set:
            if point.distance_to(Point(*target)) <= tolerance:
                result.append(point.coords)
        
        self.selected_points = set(p for p in point_set if p.coords in result)
        return result
    
    def select_line(self, point_set: PointSet, start: Tuple, end: Tuple,
                   tolerance: float = 0.1) -> List[Tuple]:
        """
        Select all points along a line.
        
        Args:
            point_set: PointSet to select from
            start: Line start coordinates
            end: Line end coordinates
            tolerance: Selection tolerance
            
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        try:
            from .utils import point_on_line
        except ImportError:
            from utils import point_on_line
        result = []
        
        for point in point_set:
            if point_on_line(point.coords, start, end, tolerance):
                result.append(point.coords)
        
        self.selected_points = set(p for p in point_set if p.coords in result)
        return result
    
    def select_within_shape(self, point_set: PointSet, shape: Shape) -> List[Tuple]:
        """
        Select all points within or on a shape.
        
        Args:
            point_set: PointSet to select from
            shape: Shape to select within
            
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        result = []
        
        for point in point_set:
            if shape.contains_point(point.coords):
                result.append(point.coords)
        
        self.selected_points = set(p for p in point_set if p.coords in result)
        return result
    
    def select_within_bounding_box(self, point_set: PointSet, bbox: Tuple) -> List[Tuple]:
        """
        Select all points within a bounding box.
        
        Args:
            point_set: PointSet to select from
            bbox: Bounding box ((min_coords), (max_coords))
            
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        result = points_in_bbox(
            [p.coords for p in point_set],
            bbox
        )
        
        self.selected_points = set(p for p in point_set if p.coords in result)
        return result
    
    def select_by_range(self, point_set: PointSet, dimension: int, 
                       min_val: float, max_val: float) -> List[Tuple]:
        """
        Select points within a range in a specific dimension.
        
        Args:
            point_set: PointSet to select from
            dimension: Dimension index
            min_val: Minimum value
            max_val: Maximum value
            
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        result = []
        
        for point in point_set:
            if point.dimensions > dimension:
                coord = point.coords[dimension]
                if min_val <= coord <= max_val:
                    result.append(point.coords)
        
        self.selected_points = set(p for p in point_set if p.coords in result)
        return result
    
    def select_by_label(self, point_set: PointSet, label: str) -> List[Tuple]:
        """
        Select points with a specific label.
        
        Args:
            point_set: PointSet to select from
            label: Label to search for
            
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        result = []
        
        for point in point_set:
            if point.label == label:
                result.append(point.coords)
        
        self.selected_points = set(p for p in point_set if p.coords in result)
        return result
    
    def select_nearest(self, point_set: PointSet, target: Tuple, count: int = 1) -> List[Tuple]:
        """
        Select N nearest points to a target.
        
        Args:
            point_set: PointSet to select from
            target: Target coordinates
            count: Number of points to select
            
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        target_point = Point(*target)
        distances = [(p, p.distance_to(target_point)) for p in point_set]
        distances.sort(key=lambda x: x[1])
        
        result = [p.coords for p, _ in distances[:count]]
        self.selected_points = set(p for p, _ in distances[:count])
        
        return result
    
    def select_farthest(self, point_set: PointSet, target: Tuple, count: int = 1) -> List[Tuple]:
        """
        Select N farthest points from a target.
        
        Args:
            point_set: PointSet to select from
            target: Target coordinates
            count: Number of points to select
            
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        target_point = Point(*target)
        distances = [(p, p.distance_to(target_point)) for p in point_set]
        distances.sort(key=lambda x: x[1], reverse=True)
        
        result = [p.coords for p, _ in distances[:count]]
        self.selected_points = set(p for p, _ in distances[:count])
        
        return result
    
    def select_all(self, point_set: PointSet) -> List[Tuple]:
        """
        Select all points.
        
        Args:
            point_set: PointSet to select from
            
        Returns:
            List[Tuple]: Coordinates of all points
        """
        result = [p.coords for p in point_set]
        self.selected_points = set(point_set.points)
        
        return result
    
    def select_by_metadata(self, point_set: PointSet, key: str, value) -> List[Tuple]:
        """
        Select points with specific metadata.
        
        Args:
            point_set: PointSet to select from
            key: Metadata key
            value: Metadata value
            
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        result = []
        
        for point in point_set:
            if point.get_metadata(key) == value:
                result.append(point.coords)
        
        self.selected_points = set(p for p in point_set if p.coords in result)
        return result
    
    def add_to_selection(self, selection: List[Tuple]) -> None:
        """
        Add points to current selection.
        
        Args:
            selection: List of coordinates to add
        """
        for coords in selection:
            self.selected_points.add(Point(*coords))
    
    def remove_from_selection(self, selection: List[Tuple]) -> None:
        """
        Remove points from current selection.
        
        Args:
            selection: List of coordinates to remove
        """
        for coords in selection:
            point = Point(*coords)
            self.selected_points.discard(point)
    
    def invert_selection(self, point_set: PointSet) -> None:
        """
        Invert the current selection.
        
        Args:
            point_set: Full PointSet for inversion reference
        """
        all_points = set(point_set.points)
        self.selected_points = all_points - self.selected_points
    
    def clear_selection(self) -> None:
        """Clear the current selection."""
        self.selected_points.clear()
    
    def get_selection(self) -> List[Tuple]:
        """
        Get current selection as list of coordinates.
        
        Returns:
            List[Tuple]: Coordinates of selected points
        """
        return [p.coords for p in sorted(self.selected_points, key=lambda p: p.coords)]
    
    def save_selection(self) -> None:
        """Save current selection to history."""
        self.selection_history.append(set(self.selected_points))
    
    def load_selection(self, index: int = -1) -> None:
        """
        Load selection from history.
        
        Args:
            index: History index (default: -1 for last)
        """
        if index < -len(self.selection_history) or index >= len(self.selection_history):
            raise IndexError("Selection history index out of range")
        
        self.selected_points = set(self.selection_history[index])
    
    def get_selection_count(self) -> int:
        """Get number of selected points."""
        return len(self.selected_points)
