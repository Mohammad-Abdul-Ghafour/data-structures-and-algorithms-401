from data_structures_and_algorithms_401 import __version__
from python.linkedList.linked_list import Node , LinkedList
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual    

def test_insert_to_ll():
    ll = LinkedList()
    ll.insert(0)
    expected = 'head -> {0} -> Null'
    actual = ll.__str__()
    assert expected == actual

def test_head_first_value(ll):
    expected = 1
    actual = ll.head.value
    assert expected == actual

def test_insert_multiple_node():
    ll = LinkedList()
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    expected = 'head -> {2} -> {1} -> {0} -> Null'
    actual = ll.__str__()
    assert expected == actual

def test_check_value_True(ll):
    expected = True
    actual =ll.includes(3)
    assert expected == actual

def test_check_value_False(ll):
    expected = False
    actual = ll.includes(8)
    assert expected == actual

def test_return_all_values(ll):
    expected = 'head -> {1} -> {2} -> {3} -> {4} -> {5} -> Null'
    actual = ll.__str__()
    assert expected == actual


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    return ll