# Generic Tree - Comprehensive Tree Data Structure

## Overview

`generic_tree.py` provides a complete implementation of a generic n-ary tree structure that allows storing and manipulating **all types of values** in a hierarchical organization.

## Key Features

✓ **Support for all value types** - Integers, strings, floats, dictionaries, lists, custom objects  
✓ **N-ary structure** - Each node can have unlimited children  
✓ **Metadata support** - Key-value pairs per node  
✓ **Multiple traversal modes** - PRE_ORDER, POST_ORDER, LEVEL_ORDER, IN_ORDER  
✓ **Search capabilities** - DFS, BFS, by value, by predicate  
✓ **JSON serialization** - Native JSON save/load  
✓ **Functional operations** - Map, filter, reduce, apply  
✓ **Tree analysis** - Height, depth, balance checking, leaf extraction  
✓ **Tree manipulation** - Sorting, reversing, cloning  

## Classes

### TreeNode

Represents a single node in the tree.

```python
node = TreeNode(value=5)
node.add_child(10)
node.set_metadata("color", "red")
```

#### Main Methods

| Method | Description |
|--------|-------------|
| `add_child(value)` | Add a child and return the child node |
| `add_node(node)` | Add an existing node as a child |
| `remove_child(node)` | Remove a child |
| `get_child_by_index(index)` | Get child by index |
| `get_child_by_value(value)` | Get child by value |
| `get_children_by_predicate(func)` | Get children matching predicate |
| `child_count()` | Number of children |
| `is_leaf()` | Check if node is a leaf |
| `is_root()` | Check if node is the root |
| `get_depth()` | Get depth from root |
| `get_path_to_root()` | Get path to root |
| `set_metadata(key, value)` | Set metadata |
| `get_metadata(key, default=None)` | Get metadata |
| `has_metadata(key)` | Check if metadata exists |
| `clear_metadata()` | Clear all metadata |
| `clone(deep=True)` | Clone the node |

### Tree

Manages the complete tree structure.

```python
tree = Tree(root_value="Root")
child = tree.add_child(tree.root, "Child")
```

#### Main Methods

| Method | Description |
|--------|-------------|
| `add_child(parent, value)` | Add child to parent |
| `add_node(parent, node)` | Add existing node |
| `remove_child(parent, child)` | Remove child |
| `get_node_by_value(value)` | Find node by value |
| `get_nodes_by_predicate(func)` | Find nodes by predicate |
| `get_all_leaf_nodes()` | Get all leaf nodes |
| `get_all_nodes()` | Get all nodes |
| `get_node_count()` | Total node count |
| `get_height()` | Tree height |
| `traverse(mode, start=None)` | Traverse tree |
| `to_dict()` | Convert to dictionary |
| `to_json(indent=None)` | Convert to JSON |
| `from_dict(data)` | Create from dictionary |
| `from_json(json_str)` | Create from JSON |
| `save_to_file(filepath)` | Save to JSON file |
| `load_from_file(filepath)` | Load from JSON file |
| `map(func)` | Apply function to all nodes |
| `filter(predicate)` | Create filtered tree |
| `find_path(value)` | Find path to value |
| `get_common_ancestor(n1, n2)` | Find common ancestor |
| `print_tree()` | Print formatted tree |
| `clear()` | Clear tree |
| `reverse_children()` | Reverse children order |
| `sort_children(key=None)` | Sort children |
| `depth_first_search(value)` | DFS search |
| `breadth_first_search(value)` | BFS search |
| `apply(func)` | Apply function to all nodes |
| `reduce(func, initial=None)` | Reduce to single value |
| `get_siblings(node)` | Get sibling nodes |
| `get_subtree_height(node)` | Get subtree height |
| `is_balanced()` | Check if balanced |

## Traversal Modes

```python
TraversalMode.PRE_ORDER    # Parent then children
TraversalMode.POST_ORDER   # Children then parent
TraversalMode.LEVEL_ORDER  # Level by level
TraversalMode.IN_ORDER     # Left subtree, parent, right subtree
```

## Usage Examples

### Creating a Tree

```python
tree = Tree(root_value="Root")
child1 = tree.add_child(tree.root, "Child 1")
child2 = tree.add_child(tree.root, "Child 2")
grandchild = tree.add_child(child1, "Grandchild")

tree.print_tree()
# Output:
# +-- Root
#     |-- Child 1
#     |   +-- Grandchild
#     +-- Child 2
```

### Traversing the Tree

```python
# Pre-order traversal
for node in tree.traverse(TraversalMode.PRE_ORDER):
    print(node.value)

# Level-order traversal
for node in tree.traverse(TraversalMode.LEVEL_ORDER):
    print(node.value)
```

### Searching

```python
# Find by value
node = tree.get_node_by_value("Grandchild")

# Find by predicate
string_nodes = tree.get_nodes_by_predicate(lambda x: isinstance(x, str))

# DFS/BFS
node = tree.depth_first_search("Child 1")
```

### Using Metadata

```python
node = tree.root
node.set_metadata("type", "root")
node.set_metadata("color", "red")

color = node.get_metadata("color")  # "red"
```

### Serialization

```python
# Save to file
tree.save_to_file("my_tree.json")

# Load from file
tree = Tree.load_from_file("my_tree.json")

# To JSON string
json_str = tree.to_json(indent=2)
```

### Functional Operations

```python
# Map: Transform all values
squared_tree = tree.map(lambda x: x * 2 if isinstance(x, int) else x)

# Filter: Create filtered tree
filtered = tree.filter(lambda x: isinstance(x, str))

# Reduce: Combine all values
total = tree.reduce(lambda acc, val: acc + val if isinstance(val, int) else acc)

# Apply: Execute function on all nodes
tree.apply(lambda node: print(f"Node: {node.value}"))
```

### Tree Analysis

```python
# Get height
height = tree.get_height()

# Get all leaves
leaves = tree.get_all_leaf_nodes()

# Get common ancestor
ancestor = tree.get_common_ancestor(node1, node2)

# Check if balanced
is_balanced = tree.is_balanced()

# Get path to value
path = tree.find_path("Grandchild")
```

## Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| add_child | O(1) | O(1) |
| get_node_by_value | O(n) | O(n) (recursion) |
| traverse | O(n) | O(n) |
| height | O(n) | O(h) (recursion) |
| balance check | O(n) | O(h) (recursion) |
| serialization | O(n) | O(n) |

## Installation

No external dependencies required. Simply import the module:

```python
from generic_tree import Tree, TreeNode, TraversalMode
```

## Testing

Run the comprehensive test suite:

```bash
pytest test_generic_tree.py -v
```

## Real-world Use Cases

1. **File Systems** - Directory trees, project hierarchies
2. **DOM Trees** - HTML/XML document structures
3. **Organizational Charts** - Company hierarchies
4. **Menu Systems** - Navigation hierarchies
5. **Dependency Graphs** - Project dependencies
6. **Category Trees** - Product categorization
7. **Decision Trees** - Algorithm structures
8. **Syntax Trees** - Programming language parsing

## License

MIT License

## Author

AI Assistant - January 12, 2026
