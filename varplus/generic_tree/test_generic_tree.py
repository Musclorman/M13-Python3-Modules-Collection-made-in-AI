import pytest
import json
import tempfile
import os
from generic_tree import Tree, TreeNode, TraversalMode


class TestTreeNodeBasics:
    def test_node_creation_no_value(self):
        node = TreeNode()
        assert node.value is None

    def test_node_creation_with_value(self):
        node = TreeNode(value=42)
        assert node.value == 42

    def test_node_creation_with_string(self):
        node = TreeNode(value="test")
        assert node.value == "test"

    def test_node_creation_with_list(self):
        node = TreeNode(value=[1, 2, 3])
        assert node.value == [1, 2, 3]

    def test_node_creation_with_dict(self):
        node = TreeNode(value={"key": "value"})
        assert node.value == {"key": "value"}

    def test_node_creation_with_float(self):
        node = TreeNode(value=3.14)
        assert node.value == 3.14

    def test_node_creation_with_boolean(self):
        node = TreeNode(value=True)
        assert node.value is True

    def test_node_creation_with_none(self):
        node = TreeNode(value=None)
        assert node.value is None

    def test_node_parent_default_none(self):
        node = TreeNode()
        assert node.parent is None

    def test_node_children_empty_list(self):
        node = TreeNode()
        assert node.children == []

    def test_node_metadata_empty_dict(self):
        node = TreeNode()
        assert node.metadata == {}


class TestTreeNodeChildren:
    def test_add_single_child(self):
        parent = TreeNode(value=1)
        child = parent.add_child(2)
        assert child.value == 2
        assert child.parent is parent
        assert len(parent.children) == 1

    def test_add_multiple_children(self):
        parent = TreeNode(value=1)
        parent.add_child(2)
        parent.add_child(3)
        parent.add_child(4)
        assert len(parent.children) == 3

    def test_add_child_returns_child_node(self):
        parent = TreeNode(value=1)
        child = parent.add_child(2)
        assert isinstance(child, TreeNode)
        assert child.value == 2

    def test_add_children_different_types(self):
        parent = TreeNode()
        parent.add_child(1)
        parent.add_child("string")
        parent.add_child(3.14)
        parent.add_child(None)
        assert len(parent.children) == 4

    def test_add_node_existing(self):
        parent = TreeNode(value=1)
        child = TreeNode(value=2)
        parent.add_node(child)
        assert child.parent is parent
        assert child in parent.children

    def test_add_node_with_metadata(self):
        parent = TreeNode(value=1)
        child = TreeNode(value=2)
        child.set_metadata("color", "red")
        parent.add_node(child)
        assert parent.children[0].get_metadata("color") == "red"

    def test_remove_child_success(self):
        parent = TreeNode(value=1)
        child = parent.add_child(2)
        result = parent.remove_child(child)
        assert result is True
        assert len(parent.children) == 0
        assert child.parent is None

    def test_remove_child_not_found(self):
        parent = TreeNode(value=1)
        child1 = parent.add_child(2)
        child2 = TreeNode(value=3)
        result = parent.remove_child(child2)
        assert result is False
        assert len(parent.children) == 1

    def test_remove_child_empty_list(self):
        parent = TreeNode(value=1)
        child = TreeNode(value=2)
        result = parent.remove_child(child)
        assert result is False

    def test_get_child_by_index_first(self):
        parent = TreeNode()
        parent.add_child(1)
        parent.add_child(2)
        child = parent.get_child_by_index(0)
        assert child.value == 1

    def test_get_child_by_index_middle(self):
        parent = TreeNode()
        parent.add_child(1)
        parent.add_child(2)
        parent.add_child(3)
        child = parent.get_child_by_index(1)
        assert child.value == 2

    def test_get_child_by_index_last(self):
        parent = TreeNode()
        parent.add_child(1)
        parent.add_child(2)
        parent.add_child(3)
        child = parent.get_child_by_index(2)
        assert child.value == 3

    def test_get_child_by_index_negative(self):
        parent = TreeNode()
        parent.add_child(1)
        child = parent.get_child_by_index(-1)
        assert child is None

    def test_get_child_by_index_out_of_range(self):
        parent = TreeNode()
        parent.add_child(1)
        child = parent.get_child_by_index(10)
        assert child is None

    def test_get_child_by_index_empty(self):
        parent = TreeNode()
        child = parent.get_child_by_index(0)
        assert child is None

    def test_get_child_by_value_found(self):
        parent = TreeNode()
        parent.add_child(1)
        parent.add_child(2)
        parent.add_child(3)
        child = parent.get_child_by_value(2)
        assert child is not None
        assert child.value == 2

    def test_get_child_by_value_not_found(self):
        parent = TreeNode()
        parent.add_child(1)
        parent.add_child(2)
        child = parent.get_child_by_value(99)
        assert child is None

    def test_get_child_by_value_duplicate(self):
        parent = TreeNode()
        parent.add_child(2)
        parent.add_child(2)
        child = parent.get_child_by_value(2)
        assert child is not None
        assert child.value == 2

    def test_get_child_by_value_string(self):
        parent = TreeNode()
        parent.add_child("hello")
        parent.add_child("world")
        child = parent.get_child_by_value("hello")
        assert child.value == "hello"

    def test_get_children_by_predicate_all_match(self):
        parent = TreeNode()
        parent.add_child(2)
        parent.add_child(4)
        parent.add_child(6)
        children = parent.get_children_by_predicate(lambda x: x % 2 == 0)
        assert len(children) == 3

    def test_get_children_by_predicate_some_match(self):
        parent = TreeNode()
        parent.add_child(1)
        parent.add_child(2)
        parent.add_child(3)
        parent.add_child(4)
        children = parent.get_children_by_predicate(lambda x: x > 2)
        assert len(children) == 2

    def test_get_children_by_predicate_none_match(self):
        parent = TreeNode()
        parent.add_child(1)
        parent.add_child(2)
        children = parent.get_children_by_predicate(lambda x: x > 100)
        assert len(children) == 0

    def test_get_children_by_predicate_empty(self):
        parent = TreeNode()
        children = parent.get_children_by_predicate(lambda x: True)
        assert len(children) == 0

    def test_child_count_zero(self):
        node = TreeNode()
        assert node.child_count() == 0

    def test_child_count_one(self):
        node = TreeNode()
        node.add_child(1)
        assert node.child_count() == 1

    def test_child_count_many(self):
        node = TreeNode()
        for i in range(100):
            node.add_child(i)
        assert node.child_count() == 100


class TestTreeNodeProperties:
    def test_is_leaf_true(self):
        node = TreeNode()
        assert node.is_leaf() is True

    def test_is_leaf_false(self):
        node = TreeNode()
        node.add_child(1)
        assert node.is_leaf() is False

    def test_is_leaf_multiple_children(self):
        node = TreeNode()
        node.add_child(1)
        node.add_child(2)
        assert node.is_leaf() is False

    def test_is_root_true(self):
        node = TreeNode()
        assert node.is_root() is True

    def test_is_root_false(self):
        parent = TreeNode()
        child = parent.add_child(1)
        assert child.is_root() is False

    def test_get_depth_root(self):
        node = TreeNode()
        assert node.get_depth() == 0

    def test_get_depth_one_level(self):
        parent = TreeNode()
        child = parent.add_child(1)
        assert child.get_depth() == 1

    def test_get_depth_multiple_levels(self):
        root = TreeNode()
        level1 = root.add_child(1)
        level2 = level1.add_child(2)
        level3 = level2.add_child(3)
        assert level3.get_depth() == 3

    def test_get_depth_deep_tree(self):
        current = TreeNode()
        for i in range(10):
            current = current.add_child(i)
        assert current.get_depth() == 10

    def test_get_path_to_root_single_node(self):
        node = TreeNode(value=1)
        path = node.get_path_to_root()
        assert len(path) == 1
        assert path[0] is node

    def test_get_path_to_root_with_parent(self):
        root = TreeNode(value=1)
        child = root.add_child(2)
        path = child.get_path_to_root()
        assert len(path) == 2
        assert path[0] is root
        assert path[1] is child

    def test_get_path_to_root_deep(self):
        root = TreeNode(value=1)
        level1 = root.add_child(2)
        level2 = level1.add_child(3)
        level3 = level2.add_child(4)
        path = level3.get_path_to_root()
        assert len(path) == 4
        assert path[0] is root
        assert path[-1] is level3


class TestTreeNodeMetadata:
    def test_set_metadata_single(self):
        node = TreeNode()
        node.set_metadata("key", "value")
        assert node.metadata["key"] == "value"

    def test_set_metadata_multiple(self):
        node = TreeNode()
        node.set_metadata("key1", "value1")
        node.set_metadata("key2", "value2")
        assert len(node.metadata) == 2

    def test_set_metadata_overwrite(self):
        node = TreeNode()
        node.set_metadata("key", "value1")
        node.set_metadata("key", "value2")
        assert node.metadata["key"] == "value2"

    def test_set_metadata_different_types(self):
        node = TreeNode()
        node.set_metadata("int", 42)
        node.set_metadata("str", "hello")
        node.set_metadata("list", [1, 2, 3])
        node.set_metadata("dict", {"a": 1})
        assert len(node.metadata) == 4

    def test_get_metadata_existing(self):
        node = TreeNode()
        node.set_metadata("key", "value")
        assert node.get_metadata("key") == "value"

    def test_get_metadata_not_existing(self):
        node = TreeNode()
        assert node.get_metadata("nonexistent") is None

    def test_get_metadata_with_default(self):
        node = TreeNode()
        assert node.get_metadata("nonexistent", "default") == "default"

    def test_has_metadata_true(self):
        node = TreeNode()
        node.set_metadata("key", "value")
        assert node.has_metadata("key") is True

    def test_has_metadata_false(self):
        node = TreeNode()
        assert node.has_metadata("nonexistent") is False

    def test_clear_metadata(self):
        node = TreeNode()
        node.set_metadata("key1", "value1")
        node.set_metadata("key2", "value2")
        node.clear_metadata()
        assert len(node.metadata) == 0


class TestTreeNodeCloning:
    def test_clone_shallow(self):
        parent = TreeNode(value=1)
        parent.add_child(2)
        cloned = parent.clone(deep=False)
        assert cloned.value == parent.value
        assert len(cloned.children) == 0

    def test_clone_deep(self):
        parent = TreeNode(value=1)
        parent.add_child(2)
        parent.add_child(3)
        cloned = parent.clone(deep=True)
        assert cloned.value == parent.value
        assert len(cloned.children) == 2

    def test_clone_with_metadata(self):
        node = TreeNode(value=1)
        node.set_metadata("color", "red")
        cloned = node.clone(deep=True)
        assert cloned.get_metadata("color") == "red"

    def test_clone_independence(self):
        node = TreeNode(value=1)
        node.set_metadata("key", "value")
        cloned = node.clone(deep=True)
        cloned.set_metadata("key", "different")
        assert node.get_metadata("key") == "value"


class TestTreeBasics:
    def test_tree_creation_no_root(self):
        tree = Tree()
        assert tree.root is not None
        assert tree.root.value is None

    def test_tree_creation_with_root(self):
        tree = Tree(root_value=42)
        assert tree.root.value == 42

    def test_tree_root_is_root(self):
        tree = Tree()
        assert tree.root.is_root() is True

    def test_tree_node_count_initial(self):
        tree = Tree()
        assert tree.get_node_count() == 1

    def test_add_child_increments_count(self):
        tree = Tree()
        tree.add_child(tree.root, 1)
        assert tree.get_node_count() == 2

    def test_add_multiple_children_count(self):
        tree = Tree()
        tree.add_child(tree.root, 1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        assert tree.get_node_count() == 4

    def test_remove_child_decrements_count(self):
        tree = Tree()
        child = tree.add_child(tree.root, 1)
        tree.remove_child(tree.root, child)
        assert tree.get_node_count() == 1


class TestTreeSearchOperations:
    def test_get_node_by_value_found(self):
        tree = Tree()
        tree.add_child(tree.root, 5)
        node = tree.get_node_by_value(5)
        assert node is not None
        assert node.value == 5

    def test_get_node_by_value_not_found(self):
        tree = Tree()
        tree.add_child(tree.root, 5)
        node = tree.get_node_by_value(99)
        assert node is None

    def test_get_node_by_value_nested(self):
        tree = Tree()
        child = tree.add_child(tree.root, 1)
        grandchild = tree.add_child(child, 2)
        node = tree.get_node_by_value(2)
        assert node is grandchild

    def test_get_nodes_by_predicate_multiple(self):
        tree = Tree(root_value=0)
        for i in range(1, 5):
            tree.add_child(tree.root, i)
        even = tree.get_nodes_by_predicate(lambda x: isinstance(x, int) and x % 2 == 0)
        assert len(even) == 3

    def test_get_all_leaf_nodes_single_branch(self):
        tree = Tree()
        c1 = tree.add_child(tree.root, 1)
        c2 = tree.add_child(c1, 2)
        leaves = tree.get_all_leaf_nodes()
        assert len(leaves) == 1
        assert leaves[0].value == 2

    def test_get_all_leaf_nodes_multiple_branches(self):
        tree = Tree()
        c1 = tree.add_child(tree.root, 1)
        c2 = tree.add_child(tree.root, 2)
        tree.add_child(c1, 3)
        tree.add_child(c2, 4)
        leaves = tree.get_all_leaf_nodes()
        assert len(leaves) == 2

    def test_get_all_nodes(self):
        tree = Tree()
        tree.add_child(tree.root, 1)
        tree.add_child(tree.root, 2)
        all_nodes = tree.get_all_nodes()
        assert len(all_nodes) == 3


class TestTreeTraversal:
    def test_traverse_pre_order_single_node(self):
        tree = Tree(root_value=1)
        values = [n.value for n in tree.traverse(TraversalMode.PRE_ORDER)]
        assert values == [1]

    def test_traverse_pre_order_simple(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        values = [n.value for n in tree.traverse(TraversalMode.PRE_ORDER)]
        assert values == [1, 2, 3]

    def test_traverse_pre_order_deep(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(tree.root, 3)
        tree.add_child(c1, 4)
        tree.add_child(c2, 5)
        values = [n.value for n in tree.traverse(TraversalMode.PRE_ORDER)]
        assert values == [1, 2, 4, 3, 5]

    def test_traverse_post_order_simple(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        values = [n.value for n in tree.traverse(TraversalMode.POST_ORDER)]
        assert values == [2, 3, 1]

    def test_traverse_post_order_deep(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(tree.root, 3)
        tree.add_child(c1, 4)
        tree.add_child(c2, 5)
        values = [n.value for n in tree.traverse(TraversalMode.POST_ORDER)]
        assert values == [4, 2, 5, 3, 1]

    def test_traverse_level_order_simple(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        values = [n.value for n in tree.traverse(TraversalMode.LEVEL_ORDER)]
        assert values == [1, 2, 3]

    def test_traverse_level_order_deep(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(tree.root, 3)
        tree.add_child(c1, 4)
        tree.add_child(c2, 5)
        values = [n.value for n in tree.traverse(TraversalMode.LEVEL_ORDER)]
        assert values == [1, 2, 3, 4, 5]

    def test_traverse_default_pre_order(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        values = [n.value for n in tree.traverse()]
        assert values[0] == 1


class TestTreeHeight:
    def test_height_single_node(self):
        tree = Tree()
        assert tree.get_height() == 0

    def test_height_one_level(self):
        tree = Tree()
        tree.add_child(tree.root, 1)
        assert tree.get_height() == 1

    def test_height_two_levels(self):
        tree = Tree()
        c1 = tree.add_child(tree.root, 1)
        tree.add_child(c1, 2)
        assert tree.get_height() == 2

    def test_height_unbalanced(self):
        tree = Tree()
        c1 = tree.add_child(tree.root, 1)
        tree.add_child(tree.root, 2)
        c2 = tree.add_child(c1, 3)
        tree.add_child(c2, 4)
        assert tree.get_height() == 3

    def test_height_wide_tree(self):
        tree = Tree()
        for i in range(10):
            tree.add_child(tree.root, i)
        assert tree.get_height() == 1


class TestTreeSerialization:
    def test_to_dict_single_node(self):
        tree = Tree(root_value=1)
        data = tree.to_dict()
        assert data['value'] == 1
        assert data['children'] == []

    def test_to_dict_with_children(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        data = tree.to_dict()
        assert len(data['children']) == 2

    def test_to_dict_nested(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        tree.add_child(c1, 3)
        data = tree.to_dict()
        assert data['children'][0]['children'][0]['value'] == 3

    def test_to_json_valid(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        json_str = tree.to_json()
        parsed = json.loads(json_str)
        assert parsed['value'] == 1

    def test_to_json_formatted(self):
        tree = Tree(root_value=1)
        json_str = tree.to_json(indent=2)
        assert '\n' in json_str

    def test_from_dict_simple(self):
        data = {'value': 1, 'children': []}
        tree = Tree.from_dict(data)
        assert tree.root.value == 1

    def test_from_dict_nested(self):
        data = {
            'value': 1,
            'children': [
                {'value': 2, 'children': [
                    {'value': 3, 'children': []}
                ]}
            ]
        }
        tree = Tree.from_dict(data)
        assert tree.root.value == 1
        assert tree.root.children[0].value == 2
        assert tree.root.children[0].children[0].value == 3

    def test_from_json_simple(self):
        json_str = '{"value": 1, "children": []}'
        tree = Tree.from_json(json_str)
        assert tree.root.value == 1

    def test_from_json_nested(self):
        json_str = '{"value": 1, "children": [{"value": 2, "children": []}]}'
        tree = Tree.from_json(json_str)
        assert tree.root.children[0].value == 2

    def test_roundtrip_json(self):
        tree1 = Tree(root_value="root")
        tree1.add_child(tree1.root, "child1")
        tree1.add_child(tree1.root, "child2")
        
        json_str = tree1.to_json()
        tree2 = Tree.from_json(json_str)
        
        assert tree2.root.value == "root"
        assert len(tree2.root.children) == 2

    def test_save_to_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "tree.json")
            tree = Tree(root_value=1)
            tree.add_child(tree.root, 2)
            tree.save_to_file(filepath)
            assert os.path.exists(filepath)

    def test_load_from_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "tree.json")
            tree1 = Tree(root_value=1)
            tree1.add_child(tree1.root, 2)
            tree1.save_to_file(filepath)
            
            tree2 = Tree.load_from_file(filepath)
            assert tree2.root.value == 1


class TestTreeFunctionalOperations:
    def test_map_identity(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        mapped = tree.map(lambda x: x)
        assert mapped.root.value == 1

    def test_map_transform_integers(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        mapped = tree.map(lambda x: x * 2 if isinstance(x, int) else x)
        values = [n.value for n in mapped.traverse()]
        assert values == [2, 4, 6]

    def test_map_preserves_structure(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        tree.add_child(c1, 3)
        mapped = tree.map(lambda x: x)
        assert len(mapped.root.children[0].children) == 1

    def test_filter_all_pass(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        filtered = tree.filter(lambda x: True)
        assert filtered.get_node_count() >= 3

    def test_filter_none_pass(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        filtered = tree.filter(lambda x: False)
        assert filtered.root.value != 1 or filtered.root.value is None

    def test_filter_partial(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        filtered = tree.filter(lambda x: x != 2)
        nodes = filtered.get_all_nodes()
        values = [n.value for n in nodes if n.value is not None]
        assert 2 not in values

    def test_find_path_root(self):
        tree = Tree(root_value=1)
        path = tree.find_path(1)
        assert path == [1]

    def test_find_path_child(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        path = tree.find_path(2)
        assert path == [1, 2]

    def test_find_path_deep(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(c1, 3)
        tree.add_child(c2, 4)
        path = tree.find_path(4)
        assert path == [1, 2, 3, 4]

    def test_find_path_not_found(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        path = tree.find_path(99)
        assert path is None

    def test_get_common_ancestor_same_node(self):
        tree = Tree(root_value=1)
        node = tree.add_child(tree.root, 2)
        ancestor = tree.get_common_ancestor(node, node)
        assert ancestor is node

    def test_get_common_ancestor_siblings(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(tree.root, 3)
        ancestor = tree.get_common_ancestor(c1, c2)
        assert ancestor is tree.root

    def test_get_common_ancestor_parent_child(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(c1, 3)
        ancestor = tree.get_common_ancestor(c1, c2)
        assert ancestor is c1

    def test_get_common_ancestor_cousins(self):
        tree = Tree(root_value=1)
        b1 = tree.add_child(tree.root, 2)
        b2 = tree.add_child(tree.root, 3)
        c1 = tree.add_child(b1, 4)
        c2 = tree.add_child(b2, 5)
        ancestor = tree.get_common_ancestor(c1, c2)
        assert ancestor is tree.root


class TestTreeAdvancedOperations:
    def test_clear_removes_children(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        tree.clear()
        assert len(tree.root.children) == 0

    def test_reverse_children_simple(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        tree.reverse_children()
        values = [c.value for c in tree.root.children]
        assert values == [3, 2]

    def test_reverse_children_deep(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(tree.root, 3)
        tree.add_child(c1, 4)
        tree.add_child(c1, 5)
        tree.reverse_children()
        assert tree.root.children[0].value == 3

    def test_sort_children_ascending(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 3)
        tree.add_child(tree.root, 1)
        tree.add_child(tree.root, 2)
        tree.sort_children()
        values = [c.value for c in tree.root.children]
        assert values == [1, 2, 3]

    def test_sort_children_descending(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 1)
        tree.add_child(tree.root, 3)
        tree.add_child(tree.root, 2)
        tree.sort_children(reverse=True)
        values = [c.value for c in tree.root.children]
        assert values == [3, 2, 1]

    def test_sort_children_custom_key(self):
        tree = Tree(root_value=0)
        tree.add_child(tree.root, "banana")
        tree.add_child(tree.root, "apple")
        tree.add_child(tree.root, "cherry")
        tree.sort_children(key=lambda x: len(x) if isinstance(x, str) else x)
        values = [c.value for c in tree.root.children]
        assert values[0] == "apple"

    def test_depth_first_search_found(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        tree.add_child(c1, 3)
        node = tree.depth_first_search(3)
        assert node is not None
        assert node.value == 3

    def test_depth_first_search_not_found(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        node = tree.depth_first_search(99)
        assert node is None

    def test_breadth_first_search_found(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        node = tree.breadth_first_search(2)
        assert node is not None
        assert node.value == 2

    def test_breadth_first_search_not_found(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        node = tree.breadth_first_search(99)
        assert node is None

    def test_apply_to_all_nodes(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        
        collected = []
        tree.apply(lambda node: collected.append(node.value))
        assert len(collected) == 3

    def test_reduce_sum(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        total = tree.reduce(lambda acc, val: acc + val if isinstance(val, int) else acc)
        assert total == 6

    def test_reduce_count(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        count = tree.reduce(lambda acc, val: acc + 1, initial=0)
        assert count == 3

    def test_reduce_concatenate(self):
        tree = Tree(root_value="a")
        tree.add_child(tree.root, "b")
        tree.add_child(tree.root, "c")
        result = tree.reduce(lambda acc, val: acc + val if isinstance(val, str) else acc)
        assert result == "abc"

    def test_get_siblings_no_parent(self):
        tree = Tree(root_value=1)
        siblings = tree.get_siblings(tree.root)
        assert len(siblings) == 0

    def test_get_siblings_with_parent(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(tree.root, 3)
        c3 = tree.add_child(tree.root, 4)
        siblings = tree.get_siblings(c1)
        assert len(siblings) == 2
        assert c2 in siblings
        assert c3 in siblings

    def test_get_subtree_height_leaf(self):
        tree = Tree(root_value=1)
        child = tree.add_child(tree.root, 2)
        height = tree.get_subtree_height(child)
        assert height == 0

    def test_get_subtree_height_with_children(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        tree.add_child(c1, 3)
        height = tree.get_subtree_height(tree.root)
        assert height == 2

    def test_is_balanced_single_node(self):
        tree = Tree(root_value=1)
        assert tree.is_balanced() is True

    def test_is_balanced_simple(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(tree.root, 3)
        tree.add_child(c1, 4)
        tree.add_child(c2, 5)
        assert tree.is_balanced() is True

    def test_is_not_balanced(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        tree.add_child(tree.root, 3)
        gc1 = tree.add_child(c1, 4)
        tree.add_child(c1, 5)
        tree.add_child(gc1, 6)
        tree.add_child(gc1, 7)
        assert tree.is_balanced() is False


class TestTreeEdgeCases:
    def test_tree_with_none_values(self):
        tree = Tree(root_value=None)
        tree.add_child(tree.root, None)
        assert tree.get_node_count() == 2

    def test_tree_with_mixed_types(self):
        tree = Tree(root_value=1)
        tree.add_child(tree.root, "string")
        tree.add_child(tree.root, 3.14)
        tree.add_child(tree.root, [1, 2, 3])
        tree.add_child(tree.root, {"key": "value"})
        assert tree.get_node_count() == 5

    def test_tree_with_large_number_of_children(self):
        tree = Tree(root_value=0)
        for i in range(1000):
            tree.add_child(tree.root, i)
        assert tree.get_node_count() == 1001

    def test_tree_with_deep_nesting(self):
        tree = Tree(root_value=0)
        current = tree.root
        for i in range(100):
            current = tree.add_child(current, i)
        assert tree.get_height() == 100

    def test_tree_with_complex_structures(self):
        tree = Tree(root_value={"type": "root"})
        tree.add_child(tree.root, {"type": "child1", "data": [1, 2, 3]})
        tree.add_child(tree.root, {"type": "child2", "nested": {"a": 1}})
        assert tree.get_node_count() == 3

    def test_tree_operations_on_empty_tree_like_structure(self):
        tree = Tree(root_value=None)
        leaves = tree.get_all_leaf_nodes()
        assert len(leaves) == 1

    def test_tree_roundtrip_with_metadata(self):
        tree = Tree(root_value=1)
        tree.root.set_metadata("type", "root")
        c1 = tree.add_child(tree.root, 2)
        c1.set_metadata("type", "child")
        
        json_str = tree.to_json(include_metadata=True)
        tree2 = Tree.from_json(json_str)
        
        assert tree2.root.get_metadata("type") == "root"

    def test_multiple_operations_sequence(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        c2 = tree.add_child(tree.root, 3)
        tree.add_child(c1, 4)
        tree.add_child(c2, 5)
        
        tree.sort_children()
        tree.reverse_children()
        height = tree.get_height()
        count = tree.get_node_count()
        
        assert height == 2
        assert count == 5


class TestTreeSearchVariations:
    def test_search_by_type_string(self):
        tree = Tree(root_value="root")
        tree.add_child(tree.root, "child1")
        tree.add_child(tree.root, 42)
        tree.add_child(tree.root, "child2")
        
        strings = tree.get_nodes_by_predicate(lambda x: isinstance(x, str))
        assert len(strings) == 3

    def test_search_by_type_integer(self):
        tree = Tree(root_value=0)
        tree.add_child(tree.root, 1)
        tree.add_child(tree.root, "not int")
        tree.add_child(tree.root, 2)
        
        ints = tree.get_nodes_by_predicate(lambda x: isinstance(x, int))
        assert len(ints) == 3

    def test_search_complex_predicate(self):
        tree = Tree(root_value=10)
        for i in range(1, 10):
            tree.add_child(tree.root, i * 10)
        
        result = tree.get_nodes_by_predicate(lambda x: isinstance(x, int) and x > 50 and x < 80)
        assert len(result) == 2


class TestTreeTraversalVariations:
    def test_traverse_large_tree_breadth_first(self):
        tree = Tree(root_value=0)
        for i in range(1, 100):
            tree.add_child(tree.root, i)
        
        first_level = [n.value for n in tree.traverse(TraversalMode.LEVEL_ORDER)]
        assert first_level[0] == 0

    def test_traverse_with_start_parameter(self):
        tree = Tree(root_value=1)
        c1 = tree.add_child(tree.root, 2)
        tree.add_child(c1, 3)
        
        values = [n.value for n in tree.traverse(TraversalMode.PRE_ORDER, c1)]
        assert values[0] == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
