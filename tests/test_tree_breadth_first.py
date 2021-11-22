from python.treeBreadthFirst.tree_breadth_first import breadthFirst
from python.trees.tree import Trees , Node
import pytest

def test_breadth_first(tree):
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual = breadthFirst(tree)
    assert expected == actual

def test_breadth_first_empty_tree():
    tree = Trees()
    with pytest.raises(ValueError):
        breadthFirst(tree)

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