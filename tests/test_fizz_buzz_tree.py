from python.treeFizzbBuzz.tree_fizz_buzz import getKTreeChild , fizzBuzzTree , Node
from python.trees.tree import Trees
import pytest

def test_fizz_buzz_tree():
    tree = Trees()
    tree.root = Node(3)
    tree.root.childs = [Node(10),Node(15),Node(8)]
    tree2 = fizzBuzzTree(tree)
    expected = "FizzBuzz"
    actual = tree2.root.childs[1].value
    assert expected == actual

def test_fizz_buzz_tree_empty():
    tree = Trees()
    with pytest.raises(ValueError):
        tree2 = fizzBuzzTree(tree)