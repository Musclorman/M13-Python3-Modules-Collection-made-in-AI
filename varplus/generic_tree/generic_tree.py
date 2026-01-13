# -*- coding=utf-8 -*-
# /usr/bin/env python3

"""
Generic Tree - Flexible n-ary tree data structure for Python

This module provides a complete implementation of a generic tree structure (n-ary)
that allows storing and manipulating all types of values in a hierarchical structure.

Key Features:
    - Support for all Python value types
    - Unlimited children per node (n-ary structure)
    - Metadata support (key-value pairs per node)
    - Multiple traversal modes (PRE_ORDER, POST_ORDER, LEVEL_ORDER, IN_ORDER)
    - JSON serialization and deserialization
    - Functional operations (map, filter, reduce)
    - Tree analysis (height, depth, balance checking)
    - Tree manipulation (sorting, reversing, cloning)

Example:
    >>> tree = Tree(root_value="root")
    >>> child = tree.add_child(tree.root, "child1")
    >>> grandchild = tree.add_child(child, "grandchild")
    >>> tree.print_tree()
    +-- root
        |-- child1
            +-- grandchild

Classes:
    TreeNode: Represents a single node in the tree
    Tree: Manages the complete tree structure
    TraversalMode: Enumeration for traversal modes

Author: AI Assistant
Date: January 12, 2026
"""

from __future__ import annotations

from typing import Any, Optional, Callable, List, Dict, Union, Iterator
import json
from dataclasses import dataclass, field, asdict
from enum import Enum


class TraversalMode(Enum):
    """Enumeration of available tree traversal modes."""
    PRE_ORDER = "pre_order"        # Parent then children
    POST_ORDER = "post_order"      # Children then parent
    LEVEL_ORDER = "level_order"    # Level by level
    IN_ORDER = "in_order"          # Left subtree, parent, right subtree


@dataclass
class TreeNode:
    """Represents a single node in a tree structure.
    
    Attributes:
        value (Any): The value stored in this node
        children (List[TreeNode]): List of child nodes
        parent (Optional[TreeNode]): Reference to parent node
        metadata (Dict[str, Any]): Custom metadata key-value pairs
    """
    value: Any = None
    children: List[TreeNode] = field(default_factory=list)
    parent: Optional[TreeNode] = field(default=None, repr=False)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_child(self, value: Any) -> TreeNode:
        """Add a new child node with the given value.
        
        Args:
            value (Any): The value for the new child node
            
        Returns:
            TreeNode: The newly created child node
        """
        child = TreeNode(value=value, parent=self)
        self.children.append(child)
        return child

    def add_node(self, node: TreeNode) -> TreeNode:
        """Add an existing node as a child.
        
        Args:
            node (TreeNode): The node to add as a child
            
        Returns:
            TreeNode: The added node
        """
        node.parent = self
        self.children.append(node)
        return node

    def remove_child(self, node: TreeNode) -> bool:
        """Remove a child node.
        
        Args:
            node (TreeNode): The child node to remove
            
        Returns:
            bool: True if removal was successful, False otherwise
        """
        if node in self.children:
            self.children.remove(node)
            node.parent = None
            return True
        return False

    def get_child_by_index(self, index: int) -> Optional[TreeNode]:
        """Get a child node by index.
        
        Args:
            index (int): The index of the child
            
        Returns:
            Optional[TreeNode]: The child at the index, or None if index is invalid
        """
        if 0 <= index < len(self.children):
            return self.children[index]
        return None

    def get_child_by_value(self, value: Any) -> Optional[TreeNode]:
        """Get the first child node with the given value.
        
        Args:
            value (Any): The value to search for
            
        Returns:
            Optional[TreeNode]: The child with the value, or None if not found
        """
        for child in self.children:
            if child.value == value:
                return child
        return None

    def get_children_by_predicate(self, predicate: Callable[[Any], bool]) -> List[TreeNode]:
        """Get all children matching a predicate function.
        
        Args:
            predicate (Callable): Function that returns True for desired children
            
        Returns:
            List[TreeNode]: List of matching children
        """
        return [child for child in self.children if predicate(child.value)]

    def child_count(self) -> int:
        """Get the number of direct children.
        
        Returns:
            int: Number of children
        """
        return len(self.children)

    def is_leaf(self) -> bool:
        """Check if this node is a leaf (has no children).
        
        Returns:
            bool: True if node has no children, False otherwise
        """
        return len(self.children) == 0

    def is_root(self) -> bool:
        """Check if this node is the root (has no parent).
        
        Returns:
            bool: True if node has no parent, False otherwise
        """
        return self.parent is None

    def get_depth(self) -> int:
        """Get the depth of this node (distance from root).
        
        Returns:
            int: Depth level (0 for root)
        """
        depth = 0
        current = self.parent
        while current is not None:
            depth += 1
            current = current.parent
        return depth

    def get_path_to_root(self) -> List[TreeNode]:
        """Get the path from this node to the root.
        
        Returns:
            List[TreeNode]: List of nodes from root to this node
        """
        path = [self]
        current = self.parent
        while current is not None:
            path.insert(0, current)
            current = current.parent
        return path

    def set_metadata(self, key: str, value: Any) -> None:
        """Set a metadata key-value pair.
        
        Args:
            key (str): The metadata key
            value (Any): The metadata value
        """
        self.metadata[key] = value

    def get_metadata(self, key: str, default: Any = None) -> Any:
        """Get a metadata value by key.
        
        Args:
            key (str): The metadata key
            default (Any): Default value if key doesn't exist
            
        Returns:
            Any: The metadata value or default
        """
        return self.metadata.get(key, default)

    def has_metadata(self, key: str) -> bool:
        """Check if a metadata key exists.
        
        Args:
            key (str): The metadata key
            
        Returns:
            bool: True if key exists, False otherwise
        """
        return key in self.metadata

    def clear_metadata(self) -> None:
        """Clear all metadata for this node."""
        self.metadata.clear()

    def clone(self, deep: bool = True) -> TreeNode:
        """Clone this node.
        
        Args:
            deep (bool): If True, clone children recursively
            
        Returns:
            TreeNode: A cloned copy of this node
        """
        cloned = TreeNode(value=self.value, metadata=self.metadata.copy())
        if deep:
            for child in self.children:
                cloned.add_node(child.clone(deep=True))
        return cloned


class Tree:
    """Manages a complete tree structure with various operations.
    
    Attributes:
        root (TreeNode): The root node of the tree
    """
    
    def __init__(self, root_value: Any = None):
        """Initialize a new tree.
        
        Args:
            root_value (Any): The value for the root node
        """
        self.root = TreeNode(value=root_value)
        self._node_count = 1

    def add_child(self, parent: TreeNode, value: Any) -> TreeNode:
        """Add a child to a parent node.
        
        Args:
            parent (TreeNode): The parent node
            value (Any): The value for the new child
            
        Returns:
            TreeNode: The newly created child node
        """
        child = parent.add_child(value)
        self._node_count += 1
        return child

    def add_node(self, parent: TreeNode, node: TreeNode) -> TreeNode:
        """Add an existing node as a child.
        
        Args:
            parent (TreeNode): The parent node
            node (TreeNode): The node to add
            
        Returns:
            TreeNode: The added node
        """
        parent.add_node(node)
        self._node_count += self._count_nodes(node)
        return node

    def remove_child(self, parent: TreeNode, child: TreeNode) -> bool:
        """Remove a child from its parent.
        
        Args:
            parent (TreeNode): The parent node
            child (TreeNode): The child to remove
            
        Returns:
            bool: True if removal was successful, False otherwise
        """
        if parent.remove_child(child):
            self._node_count -= self._count_nodes(child)
            return True
        return False

    def get_node_by_value(self, value: Any, start: Optional[TreeNode] = None) -> Optional[TreeNode]:
        """Find a node by its value.
        
        Args:
            value (Any): The value to search for
            start (Optional[TreeNode]): Node to start search from (default: root)
            
        Returns:
            Optional[TreeNode]: The found node, or None if not found
        """
        search_root = start or self.root
        for node in self.traverse(TraversalMode.PRE_ORDER, search_root):
            if node.value == value:
                return node
        return None

    def get_nodes_by_predicate(self, predicate: Callable[[Any], bool], 
                               start: Optional[TreeNode] = None) -> List[TreeNode]:
        """Find all nodes matching a predicate.
        
        Args:
            predicate (Callable): Function that returns True for desired nodes
            start (Optional[TreeNode]): Node to start search from (default: root)
            
        Returns:
            List[TreeNode]: List of matching nodes
        """
        search_root = start or self.root
        return [node for node in self.traverse(TraversalMode.PRE_ORDER, search_root)
                if predicate(node.value)]

    def get_all_leaf_nodes(self, start: Optional[TreeNode] = None) -> List[TreeNode]:
        """Get all leaf nodes in the tree.
        
        Args:
            start (Optional[TreeNode]): Node to start search from (default: root)
            
        Returns:
            List[TreeNode]: List of all leaf nodes
        """
        search_root = start or self.root
        return [node for node in self.traverse(TraversalMode.PRE_ORDER, search_root)
                if node.is_leaf()]

    def get_all_nodes(self, start: Optional[TreeNode] = None) -> List[TreeNode]:
        """Get all nodes in the tree.
        
        Args:
            start (Optional[TreeNode]): Node to start from (default: root)
            
        Returns:
            List[TreeNode]: List of all nodes
        """
        search_root = start or self.root
        return list(self.traverse(TraversalMode.PRE_ORDER, search_root))

    def get_node_count(self) -> int:
        """Get the total number of nodes in the tree.
        
        Returns:
            int: Total node count
        """
        return self._node_count

    def get_height(self, node: Optional[TreeNode] = None) -> int:
        """Get the height of the tree (or subtree).
        
        Args:
            node (Optional[TreeNode]): Node to calculate height from (default: root)
            
        Returns:
            int: Height of the tree
        """
        current = node or self.root
        if current.is_leaf():
            return 0
        return 1 + max((self.get_height(child) for child in current.children), default=0)

    def traverse(self, mode: TraversalMode = TraversalMode.PRE_ORDER, 
                 start: Optional[TreeNode] = None) -> Iterator[TreeNode]:
        """Traverse the tree in the specified mode.
        
        Args:
            mode (TraversalMode): The traversal mode to use
            start (Optional[TreeNode]): Node to start from (default: root)
            
        Yields:
            TreeNode: Nodes in traversal order
        """
        node = start or self.root
        
        if mode == TraversalMode.PRE_ORDER:
            yield from self._pre_order(node)
        elif mode == TraversalMode.POST_ORDER:
            yield from self._post_order(node)
        elif mode == TraversalMode.LEVEL_ORDER:
            yield from self._level_order(node)
        elif mode == TraversalMode.IN_ORDER:
            yield from self._in_order(node)

    def _pre_order(self, node: TreeNode) -> Iterator[TreeNode]:
        """Pre-order traversal: parent then children."""
        yield node
        for child in node.children:
            yield from self._pre_order(child)

    def _post_order(self, node: TreeNode) -> Iterator[TreeNode]:
        """Post-order traversal: children then parent."""
        for child in node.children:
            yield from self._post_order(child)
        yield node

    def _level_order(self, node: TreeNode) -> Iterator[TreeNode]:
        """Level-order traversal: level by level."""
        queue = [node]
        while queue:
            current = queue.pop(0)
            yield current
            queue.extend(current.children)

    def _in_order(self, node: TreeNode) -> Iterator[TreeNode]:
        """In-order traversal: left subtree, parent, right subtree."""
        if not node.is_leaf():
            mid = len(node.children) // 2
            for child in node.children[:mid]:
                yield from self._in_order(child)
        yield node
        if not node.is_leaf():
            mid = len(node.children) // 2
            for child in node.children[mid:]:
                yield from self._in_order(child)

    def to_dict(self, node: Optional[TreeNode] = None, include_metadata: bool = True) -> Dict[str, Any]:
        """Convert the tree to a dictionary.
        
        Args:
            node (Optional[TreeNode]): Node to start from (default: root)
            include_metadata (bool): Whether to include metadata
            
        Returns:
            Dict[str, Any]: Dictionary representation of the tree
        """
        current = node or self.root
        result = {
            'value': current.value,
            'children': []
        }
        
        if include_metadata and current.metadata:
            result['metadata'] = current.metadata
        
        for child in current.children:
            result['children'].append(self.to_dict(child, include_metadata))
        
        return result

    def to_json(self, node: Optional[TreeNode] = None, include_metadata: bool = True, 
                indent: Optional[int] = None) -> str:
        """Convert the tree to JSON string.
        
        Args:
            node (Optional[TreeNode]): Node to start from (default: root)
            include_metadata (bool): Whether to include metadata
            indent (Optional[int]): JSON indentation level
            
        Returns:
            str: JSON representation of the tree
        """
        data = self.to_dict(node, include_metadata)
        return json.dumps(data, indent=indent, default=str)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> Tree:
        """Create a tree from a dictionary.
        
        Args:
            data (Dict[str, Any]): Dictionary representation of the tree
            
        Returns:
            Tree: A new tree constructed from the dictionary
        """
        tree = Tree(root_value=data.get('value'))
        
        if 'metadata' in data:
            tree.root.metadata = data['metadata']
        
        for child_data in data.get('children', []):
            Tree._build_from_dict(tree.root, child_data)
        
        return tree

    @staticmethod
    def _build_from_dict(parent: TreeNode, child_data: Dict[str, Any]) -> None:
        """Helper method to build tree from dictionary recursively."""
        child = parent.add_child(child_data.get('value'))
        
        if 'metadata' in child_data:
            child.metadata = child_data['metadata']
        
        for grandchild_data in child_data.get('children', []):
            Tree._build_from_dict(child, grandchild_data)

    @staticmethod
    def from_json(json_str: str) -> Tree:
        """Create a tree from a JSON string.
        
        Args:
            json_str (str): JSON representation of the tree
            
        Returns:
            Tree: A new tree constructed from the JSON
        """
        data = json.loads(json_str)
        return Tree.from_dict(data)

    def save_to_file(self, filepath: str, include_metadata: bool = True, 
                     indent: int = 2) -> None:
        """Save the tree to a JSON file.
        
        Args:
            filepath (str): Path to save the file
            include_metadata (bool): Whether to include metadata
            indent (int): JSON indentation level
        """
        json_str = self.to_json(include_metadata=include_metadata, indent=indent)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def load_from_file(filepath: str) -> Tree:
        """Load a tree from a JSON file.
        
        Args:
            filepath (str): Path to the file to load
            
        Returns:
            Tree: The loaded tree
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            json_str = f.read()
        return Tree.from_json(json_str)

    def map(self, func: Callable[[Any], Any], node: Optional[TreeNode] = None) -> Tree:
        """Apply a function to all nodes and return a new tree.
        
        Args:
            func (Callable): Function to apply to each node's value
            node (Optional[TreeNode]): Node to start from (default: root)
            
        Returns:
            Tree: A new tree with transformed values
        """
        current = node or self.root
        new_value = func(current.value)
        new_node = TreeNode(value=new_value, metadata=current.metadata.copy())
        
        for child in current.children:
            child_tree = self.map(func, child)
            new_node.add_node(child_tree.root)
        
        new_tree = Tree()
        new_tree.root = new_node
        return new_tree

    def filter(self, predicate: Callable[[Any], bool], node: Optional[TreeNode] = None) -> Tree:
        """Filter the tree by a predicate.
        
        Args:
            predicate (Callable): Function that returns True for nodes to keep
            node (Optional[TreeNode]): Node to start from (default: root)
            
        Returns:
            Tree: A new filtered tree
        """
        current = node or self.root
        
        if not predicate(current.value):
            return Tree()
        
        new_node = TreeNode(value=current.value, metadata=current.metadata.copy())
        
        for child in current.children:
            child_tree = self.filter(predicate, child)
            if child_tree.root.value is not None or child_tree.get_node_count() > 1:
                new_node.add_node(child_tree.root)
        
        new_tree = Tree()
        new_tree.root = new_node
        return new_tree

    def find_path(self, target_value: Any, start: Optional[TreeNode] = None) -> Optional[List[Any]]:
        """Find the path to a value in the tree.
        
        Args:
            target_value (Any): The value to find
            start (Optional[TreeNode]): Node to start from (default: root)
            
        Returns:
            Optional[List[Any]]: List of values from root to target, or None if not found
        """
        current = start or self.root
        
        if current.value == target_value:
            return [current.value]
        
        for child in current.children:
            path = self.find_path(target_value, child)
            if path is not None:
                return [current.value] + path
        
        return None

    def get_common_ancestor(self, node1: TreeNode, node2: TreeNode) -> Optional[TreeNode]:
        """Find the lowest common ancestor of two nodes.
        
        Args:
            node1 (TreeNode): First node
            node2 (TreeNode): Second node
            
        Returns:
            Optional[TreeNode]: The common ancestor, or None if not found
        """
        path1 = {id(n): n for n in node1.get_path_to_root()}
        path2 = node2.get_path_to_root()
        
        for node in path2:
            if id(node) in path1:
                return path1[id(node)]
        
        return None

    def print_tree(self, node: Optional[TreeNode] = None, prefix: str = "", 
                   is_last: bool = True) -> None:
        """Print the tree in a formatted way.
        
        Args:
            node (Optional[TreeNode]): Node to start from (default: root)
            prefix (str): Prefix for printing
            is_last (bool): Whether this is the last child
        """
        current = node or self.root
        
        connector = "+-- " if is_last else "|-- "
        print(prefix + connector + str(current.value))
        
        children = current.children
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            extension = "    " if is_last else "|   "
            self.print_tree(child, prefix + extension, is_last_child)

    def clear(self) -> None:
        """Clear all children from the root node."""
        self.root.children.clear()
        self._node_count = 1

    def reverse_children(self, node: Optional[TreeNode] = None) -> None:
        """Reverse the order of children for all nodes.
        
        Args:
            node (Optional[TreeNode]): Node to start from (default: root)
        """
        current = node or self.root
        current.children.reverse()
        for child in current.children:
            self.reverse_children(child)

    def sort_children(self, node: Optional[TreeNode] = None, 
                      key: Optional[Callable[[Any], Any]] = None, 
                      reverse: bool = False) -> None:
        """Sort children of all nodes.
        
        Args:
            node (Optional[TreeNode]): Node to start from (default: root)
            key (Optional[Callable]): Function to extract sort key
            reverse (bool): Sort in reverse order
        """
        current = node or self.root
        current.children.sort(key=lambda x: key(x.value) if key else x.value, 
                             reverse=reverse)
        for child in current.children:
            self.sort_children(child, key, reverse)

    def _count_nodes(self, node: TreeNode) -> int:
        """Count nodes in a subtree."""
        count = 1
        for child in node.children:
            count += self._count_nodes(child)
        return count

    def depth_first_search(self, target_value: Any, start: Optional[TreeNode] = None) -> Optional[TreeNode]:
        """Search for a node using depth-first search.
        
        Args:
            target_value (Any): The value to search for
            start (Optional[TreeNode]): Node to start from (default: root)
            
        Returns:
            Optional[TreeNode]: The found node, or None if not found
        """
        current = start or self.root
        stack = [current]
        
        while stack:
            node = stack.pop()
            if node.value == target_value:
                return node
            stack.extend(reversed(node.children))
        
        return None

    def breadth_first_search(self, target_value: Any, start: Optional[TreeNode] = None) -> Optional[TreeNode]:
        """Search for a node using breadth-first search.
        
        Args:
            target_value (Any): The value to search for
            start (Optional[TreeNode]): Node to start from (default: root)
            
        Returns:
            Optional[TreeNode]: The found node, or None if not found
        """
        current = start or self.root
        queue = [current]
        
        while queue:
            node = queue.pop(0)
            if node.value == target_value:
                return node
            queue.extend(node.children)
        
        return None

    def apply(self, func: Callable[[TreeNode], None], node: Optional[TreeNode] = None) -> None:
        """Apply a function to all nodes.
        
        Args:
            func (Callable): Function to apply to each node
            node (Optional[TreeNode]): Node to start from (default: root)
        """
        current = node or self.root
        func(current)
        for child in current.children:
            self.apply(func, child)

    def reduce(self, func: Callable[[Any, Any], Any], node: Optional[TreeNode] = None, 
               initial: Any = None) -> Any:
        """Reduce the tree to a single value.
        
        Args:
            func (Callable): Reduction function
            node (Optional[TreeNode]): Node to start from (default: root)
            initial (Any): Initial accumulator value
            
        Returns:
            Any: The reduced value
        """
        current = node or self.root
        accumulator = func(initial, current.value) if initial is not None else current.value
        
        for child in current.children:
            accumulator = self.reduce(func, child, accumulator)
        
        return accumulator

    def get_siblings(self, node: TreeNode) -> List[TreeNode]:
        """Get sibling nodes of a given node.
        
        Args:
            node (TreeNode): The node to find siblings for
            
        Returns:
            List[TreeNode]: List of sibling nodes
        """
        if node.parent is None:
            return []
        return [child for child in node.parent.children if child is not node]

    def get_subtree_height(self, node: TreeNode) -> int:
        """Get the height of a subtree rooted at a node.
        
        Args:
            node (TreeNode): The root of the subtree
            
        Returns:
            int: Height of the subtree
        """
        if node.is_leaf():
            return 0
        return 1 + max((self.get_subtree_height(child) for child in node.children), default=0)

    def is_balanced(self, node: Optional[TreeNode] = None) -> bool:
        """Check if the tree (or subtree) is balanced.
        
        Args:
            node (Optional[TreeNode]): Node to start from (default: root)
            
        Returns:
            bool: True if tree is balanced, False otherwise
        """
        current = node or self.root
        
        if current.is_leaf():
            return True
        
        if not current.children:
            return True
        
        heights = [self.get_subtree_height(child) for child in current.children]
        max_height = max(heights) if heights else 0
        min_height = min(heights) if heights else 0
        
        if max_height - min_height > 1:
            return False
        
        return all(self.is_balanced(child) for child in current.children)
