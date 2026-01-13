"""
Point management for MultidimensionalPaint module.

This module defines classes for representing and managing points
in n-dimensional space.
"""

from typing import Tuple, List, Optional, Iterator
try:
    from .utils import validate_coordinates, distance
except ImportError:
    from utils import validate_coordinates, distance


class Point:
    """
    Represents a point in n-dimensional space.
    
    Attributes:
        coords (Tuple): Coordinates of the point
        label (Optional[str]): Optional label for the point
        metadata (dict): Additional metadata
    """
    
    def __init__(self, *coords, label: Optional[str] = None):
        """
        Initialize a point with given coordinates.
        
        Args:
            *coords: Variable number of coordinate values
            label: Optional label for the point
            
        Raises:
            ValueError: If coordinates are not numeric
        """
        if not coords:
            raise ValueError("At least one coordinate required")
        
        if not validate_coordinates(*coords):
            raise ValueError("All coordinates must be numeric")
        
        self.coords = tuple(coords)
        self.label = label
        self.metadata = {}
    
    @property
    def dimensions(self) -> int:
        """Get the number of dimensions."""
        return len(self.coords)
    
    @property
    def x(self) -> float:
        """Get x coordinate (first dimension)."""
        return self.coords[0]
    
    @property
    def y(self) -> Optional[float]:
        """Get y coordinate (second dimension)."""
        return self.coords[1] if self.dimensions >= 2 else None
    
    @property
    def z(self) -> Optional[float]:
        """Get z coordinate (third dimension)."""
        return self.coords[2] if self.dimensions >= 3 else None
    
    @property
    def w(self) -> Optional[float]:
        """Get w coordinate (fourth dimension)."""
        return self.coords[3] if self.dimensions >= 4 else None
    
    def get_coordinate(self, dimension: int) -> float:
        """
        Get coordinate at specific dimension.
        
        Args:
            dimension: Dimension index (0-based)
            
        Returns:
            float: Coordinate value
            
        Raises:
            IndexError: If dimension is out of range
        """
        if dimension < 0 or dimension >= self.dimensions:
            raise IndexError(f"Dimension {dimension} out of range")
        return self.coords[dimension]
    
    def distance_to(self, other: 'Point') -> float:
        """
        Calculate distance to another point.
        
        Args:
            other: Another point
            
        Returns:
            float: Euclidean distance
            
        Raises:
            ValueError: If points have different dimensions
        """
        if self.dimensions != other.dimensions:
            raise ValueError(f"Points must have same dimensions: {self.dimensions} != {other.dimensions}")
        
        return distance(self.coords, other.coords)
    
    def set_metadata(self, key: str, value):
        """Set metadata value."""
        self.metadata[key] = value
    
    def get_metadata(self, key: str, default=None):
        """Get metadata value."""
        return self.metadata.get(key, default)
    
    def __repr__(self) -> str:
        """String representation."""
        if self.label:
            return f"Point{self.dimensions}D({', '.join(map(str, self.coords))}, label='{self.label}')"
        return f"Point{self.dimensions}D({', '.join(map(str, self.coords))})"
    
    def __str__(self) -> str:
        """Readable string representation."""
        coords_str = ', '.join(f"{c:.2f}" for c in self.coords)
        if self.label:
            return f"{self.label}: ({coords_str})"
        return f"({coords_str})"
    
    def __eq__(self, other) -> bool:
        """Check equality."""
        if not isinstance(other, Point):
            return False
        return self.coords == other.coords
    
    def __hash__(self) -> int:
        """Get hash for use in sets/dicts."""
        return hash(self.coords)
    
    def __getitem__(self, index: int) -> float:
        """Get coordinate by index."""
        return self.coords[index]
    
    def __iter__(self) -> Iterator[float]:
        """Iterate over coordinates."""
        return iter(self.coords)


class PointSet:
    """
    Manages a collection of points.
    
    Attributes:
        points (List[Point]): List of points in the set
    """
    
    def __init__(self, points: Optional[List[Point]] = None):
        """
        Initialize a point set.
        
        Args:
            points: Optional initial list of points
        """
        self.points = points or []
        self._validate_consistency()
    
    def _validate_consistency(self):
        """Ensure all points have the same dimensions."""
        if not self.points:
            return
        
        first_dim = self.points[0].dimensions
        for point in self.points[1:]:
            if point.dimensions != first_dim:
                raise ValueError("All points must have the same dimensions")
    
    @property
    def dimensions(self) -> Optional[int]:
        """Get the number of dimensions."""
        return self.points[0].dimensions if self.points else None
    
    @property
    def count(self) -> int:
        """Get number of points in set."""
        return len(self.points)
    
    def add_point(self, point: Point) -> None:
        """
        Add a point to the set.
        
        Args:
            point: Point to add
        """
        if self.points and point.dimensions != self.dimensions:
            raise ValueError(f"Point dimensions {point.dimensions} don't match set dimensions {self.dimensions}")
        
        self.points.append(point)
    
    def remove_point(self, point: Point) -> bool:
        """
        Remove a point from the set.
        
        Args:
            point: Point to remove
            
        Returns:
            bool: True if point was removed, False if not found
        """
        try:
            self.points.remove(point)
            return True
        except ValueError:
            return False
    
    def get_point(self, index: int) -> Point:
        """
        Get point at index.
        
        Args:
            index: Point index
            
        Returns:
            Point: The point at the index
        """
        return self.points[index]
    
    def get_by_label(self, label: str) -> Optional[Point]:
        """
        Get point by label.
        
        Args:
            label: Point label
            
        Returns:
            Optional[Point]: Point with given label or None
        """
        for point in self.points:
            if point.label == label:
                return point
        return None
    
    def find_nearest(self, point: Point) -> Optional[Point]:
        """
        Find nearest point in set.
        
        Args:
            point: Reference point
            
        Returns:
            Optional[Point]: Nearest point or None if set is empty
        """
        if not self.points:
            return None
        
        return min(self.points, key=lambda p: p.distance_to(point))
    
    def find_farthest(self, point: Point) -> Optional[Point]:
        """
        Find farthest point in set.
        
        Args:
            point: Reference point
            
        Returns:
            Optional[Point]: Farthest point or None if set is empty
        """
        if not self.points:
            return None
        
        return max(self.points, key=lambda p: p.distance_to(point))
    
    def get_bounding_box(self) -> Optional[Tuple]:
        """
        Get bounding box of all points.
        
        Returns:
            Optional[Tuple]: ((min_coords), (max_coords)) or None if empty
        """
        if not self.points:
            return None
        
        try:
            from .utils import bounding_box
        except ImportError:
            from utils import bounding_box
        return bounding_box(*[p.coords for p in self.points])
    
    def get_centroid(self) -> Optional[Point]:
        """
        Calculate centroid of all points.
        
        Returns:
            Optional[Point]: Centroid point or None if empty
        """
        if not self.points:
            return None
        
        try:
            from .utils import midpoint
        except ImportError:
            from utils import midpoint
        centroid_coords = midpoint(*[p.coords for p in self.points])
        return Point(*centroid_coords, label="centroid")
    
    def clear(self) -> None:
        """Clear all points from the set."""
        self.points.clear()
    
    def __len__(self) -> int:
        """Get number of points."""
        return len(self.points)
    
    def __iter__(self) -> Iterator[Point]:
        """Iterate over points."""
        return iter(self.points)
    
    def __getitem__(self, index: int) -> Point:
        """Get point by index."""
        return self.points[index]
    
    def __repr__(self) -> str:
        """String representation."""
        return f"PointSet({self.count} points, {self.dimensions}D)"
