from python.trees.tree import Node, Trees , SearchTree
import pytest

def test_instantiate_empty_tree():
    tree = Trees()
    expected = None
    actual = tree.root
    assert expected == actual

def test_one_root_node():
    tree = Trees()
    tree.root = Node(5)
    expected = 5
    actual = tree.root.value
    assert expected == actual

def test_add_left_and_right_node():
    tree = Trees()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.right = Node(7)
    expectedLeft = 4
    actualLeft = tree.root.left.value
    expectedRight = 7
    actualRight = tree.root.right.value
    assert expectedLeft == actualLeft
    assert expectedRight == actualRight
    
def test_preorder():
    tree = Trees()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.right = Node(7)
    expected = [5,4,7]
    travers = tree.preOrder()
    actual = travers(tree.root)
    assert expected == actual

def test_inorder():
    tree = Trees()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.right = Node(7)
    expected = [4,5,7]
    travers = tree.inOrder()
    actual = travers(tree.root)
    assert expected == actual

def test_postorder():
    tree = Trees()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.right = Node(7)
    expected = [4,7,5]
    travers = tree.postOrder()
    actual = travers(tree.root)
    assert expected == actual

def test_add_search_tree():
    tree = SearchTree()
    tree.add(5)
    tree.add(4)
    tree.add(7)
    expected = [5,4,7]
    travers = tree.preOrder()
    actual = travers(tree.root)
    assert expected == actual

def test_contains_search_tree_true():
    tree = SearchTree()
    tree.add(5)
    tree.add(4)
    tree.add(7)
    tree.add(3)
    tree.add(10)
    expected = True
    actual = tree.contains(10)
    assert expected == actual

def test_contains_search_tree_false():
    tree = SearchTree()
    tree.add(5)
    tree.add(4)
    tree.add(7)
    tree.add(3)
    tree.add(10)
    expected = False
    actual = tree.contains(15)
    assert expected == actual

def test_contains_search_tree_empty():
    tree = SearchTree()
    with pytest.raises(ValueError):
        tree.contains(5)