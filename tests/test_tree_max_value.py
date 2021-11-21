from python.treesMax.tree_max import Node, Trees
import pytest

def test_max_value(tree):
    expected = 11
    actual = tree.maxValue()
    assert expected == actual

def test_max_value_empty_tree():
    tree = Trees()
    with pytest.raises(ValueError):
        tree.maxValue()

@pytest.fixture
def tree():
    tree = Trees()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    return tree