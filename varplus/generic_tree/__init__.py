# -*- coding: utf-8 -*-
"""
generic_tree - Complete N-ary Tree Data Structure

A flexible, feature-rich tree implementation for Python that supports:
- All Python data types as node values
- N-ary tree structure (unlimited children per node)
- Multiple traversal modes (pre-order, post-order, level-order, etc.)
- JSON serialization and deserialization
- Functional operations and tree analysis
- Complete tree manipulation capabilities

This module is part of the variableplus project.

Project: variableplus
Created by: Musclor13
Developed with AI assistance

Version: 1.0.0
License: MIT

Example:
    >>> from generic_tree import Tree, TraversalMode
    >>> tree = Tree(root_value="root")
    >>> child = tree.add_child(tree.root, "child")
    >>> for node in tree.traverse(TraversalMode.PRE_ORDER):
    ...     print(node.value)
    root
    child

For complete documentation, see README.md
Documentation available in: English, French, Spanish, German, Italian, Chinese
"""

from .generic_tree import (
    Tree,
    TreeNode,
    TraversalMode,
)

__module__ = 'generic_tree'
__project__ = 'variableplus'
__author__ = 'Musclor13'
__version__ = '1.0.0'
__license__ = 'MIT'
__copyright__ = 'Copyright 2026 - Created with AI assistance'

__all__ = [
    'Tree',
    'TreeNode',
    'TraversalMode',
]
