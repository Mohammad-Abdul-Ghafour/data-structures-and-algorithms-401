from python.treeIntersection.tree_intersection import tree_intersection
from python.trees.tree import Node , Trees
import pytest

def test_tree_intersection(tree1,tree2):
    expected = "100 , 200 , 350 , 500 , "
    actual = tree_intersection(tree1,tree2)
    assert expected == actual

def test_tree_intersection_second_tree_empty(tree3,tree1):  
    expected = "First tree in the arguments are empty"
    actual = tree_intersection(tree3,tree1)
    assert expected == actual

def test_tree_intersection_second_tree_empty(tree1,tree3):  
    expected = "Second tree in the arguments are empty"
    actual = tree_intersection(tree1,tree3)
    assert expected == actual

def test_tree_intersection_no_common_values(tree1,tree4):
    expected = "There are no common values"
    actual = tree_intersection(tree1,tree4)
    assert expected == actual


@pytest.fixture
def tree1():
    tree1 = Trees()
    tree1.root = Node(150)
    tree1.root.right = Node(250)
    tree1.root.left = Node(100)

    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)

    tree1.root.right.right.right = Node(500)
    tree1.root.right.right.left = Node(300)

    return tree1

@pytest.fixture
def tree2():
    tree2 = Trees()
    tree2.root = Node(42)
    tree2.root.right = Node(600)
    tree2.root.left = Node(100)

    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)

    tree2.root.right.right.right = Node(500)
    tree2.root.right.right.left = Node(4)

    return tree2

@pytest.fixture
def tree3():
    tree3 = Trees()
    return tree3

@pytest.fixture
def tree4():
    tree4 = Trees()
    tree4.root = Node(6786)
    tree4.root.right = Node(2323)

    return tree4