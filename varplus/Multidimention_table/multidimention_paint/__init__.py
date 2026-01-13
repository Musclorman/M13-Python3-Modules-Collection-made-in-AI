# -*- coding: utf-8 -*-
"""
MultidimensionalPaint - Multidimensional Point and Geometric Shape Management

A comprehensive package for working with points and geometric shapes in
n-dimensional spaces (1D, 2D, 3D, 4D, and beyond).

Features:
- Points in 1D to ND (tested up to 100D+)
- 9 geometric shape types
- 10 advanced selection methods
- Flexible metadata system
- Selection history management
- Statistical analysis capabilities

This module is part of the variableplus project.

Project: variableplus
Created by: Musclor13
Developed with AI assistance

Version: 1.0.0
License: MIT

Main Classes:
- MultidimensionalPaint: Main API class
- Point: Represents a point in n-dimensional space
- PointSet: Collection management for points
- Shape: Base class for geometric shapes
- Line, Circle, Rectangle, Square, Ellipse, Arc, ClosedShape: Shape implementations
- SelectionEngine: Advanced point selection engine

Example:
    >>> from paint import MultidimensionalPaint
    >>> painter = MultidimensionalPaint()
    >>> painter.add_point(0, 0)
    >>> painter.add_point(5, 5)
    >>> painter.draw_circle((2.5, 2.5), 2)
    >>> selection = painter.select_within_region((0, 0), (5, 5))

For complete documentation, see README files in multiple languages.
"""

try:
    from .paint import MultidimensionalPaint
    from .points import Point, PointSet
    from .shapes import Shape, Line, Circle, Rectangle, Square, Ellipse, Arc, ClosedShape
    from .selection import SelectionEngine
    from .utils import distance, midpoint, validate_coordinates
except ImportError:
    from paint import MultidimensionalPaint
    from points import Point, PointSet
    from shapes import Shape, Line, Circle, Rectangle, Square, Ellipse, Arc, ClosedShape
    from selection import SelectionEngine
    from utils import distance, midpoint, validate_coordinates

__module__ = 'multidimention_paint'
__project__ = 'variableplus'
__author__ = 'Musclor13'
__version__ = '1.0.0'
__license__ = 'MIT'
__copyright__ = 'Copyright 2026 - Created with AI assistance'

__all__ = [
    'MultidimensionalPaint',
    'Point',
    'PointSet',
    'Shape',
    'Line',
    'Circle',
    'Rectangle',
    'Square',
    'Ellipse',
    'Arc',
    'ClosedShape',
    'SelectionEngine',
    'distance',
    'midpoint',
    'validate_coordinates',
]
