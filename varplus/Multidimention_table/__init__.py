# -*- coding: utf-8 -*-
"""
Multidimention_table - Multidimensional Data Structure Management

A comprehensive package for handling multidimensional tables and arrays:
- Support for 1D, 2D, 3D and n-dimensional data structures
- Easy creation, indexing, reshaping, and slicing operations
- Table merging and conversion capabilities
- Complete data manipulation functionality
- Includes multidimention_paint for geometric operations on points

Components:
- MultiDimTable: Core multidimensional table implementation
- multitable: Advanced multitable operations
- multidimention_paint: Point and geometric shape management

This module is part of the variableplus project.

Project: variableplus
Created by: Musclor13
Developed with AI assistance

Version: 1.0.0
License: MIT

Features:
- MultiDimTable: Create and manage multidimensional arrays
- ShapeError: Exception for shape-related errors
- IndexError_: Custom indexing error handling
- Support for complex data operations

Example:
    >>> from Multidimention_table import MultiDimTable
    >>> table = MultiDimTable(shape=(3, 4, 5))
    >>> table[0, 0, 0] = 42
    >>> print(table.get_dimensions())

For complete documentation, see README.md
Documentation available in: English, French
"""

from .multidim_table import (
    MultiDimTable,
    ShapeError,
    IndexError_
)

__module__ = 'Multidimention_table'
__project__ = 'variableplus'
__author__ = 'Musclor13'
__version__ = '1.0.0'
__license__ = 'MIT'
__copyright__ = 'Copyright 2026 - Created with AI assistance'

__all__ = [
    'MultiDimTable',
    'ShapeError',
    'IndexError_',
    'multidim_table',
    'multitable',
    'multidimention_paint',
]
