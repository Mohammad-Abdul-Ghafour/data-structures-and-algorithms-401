from python.linkedListInsertions.linked_list_insertions import Node , LinkedList
import pytest

def test_append(ll):
    ll.append(2)
    expected = "head -> [5] -> [4] -> [3] -> [2] -> X"
    actual = ll.__str__()
    assert expected == actual  

def test_append_multi_values():
    ll = LinkedList()
    ll.append(5)
    ll.append(4)
    ll.append(3)
    expected = "head -> [5] -> [4] -> [3] -> X"
    actual = ll.__str__()
    assert expected == actual  

def test_insert_after_middle(ll):
    ll.insertAfter(4,2)
    expected = "head -> [5] -> [4] -> [2] -> [3] -> X"
    actual = ll.__str__()
    assert expected == actual  

def test_insert_after_last_node(ll):
    ll.insertAfter(3,2)
    expected = "head -> [5] -> [4] -> [3] -> [2] -> X"
    actual = ll.__str__()
    assert expected == actual 

def test_insert_before_middle(ll):
    ll.insertBefore(4,2)
    expected = "head -> [5] -> [2] -> [4] -> [3] -> X"
    actual = ll.__str__()
    assert expected == actual  

def test_insert_before_last_node(ll):
    ll.insertBefore(5,2)
    expected = "head -> [2] -> [5] -> [4] -> [3] -> X"
    actual = ll.__str__()
    assert expected == actual 

# def test_insert_before_expected_failure(ll):
#     ll.insertBefore(6,2)
#     expected = "head -> [5] -> [4] -> [3] -> X"
#     actual = ll.__str__()
#     assert expected == actual 

# def test_insert_after_expected_failure(ll):
#     ll.insertBefore(6,2)
#     expected = "head -> [5] -> [4] -> [3] -> X"
#     actual = ll.__str__()
#     assert expected == actual 

# def test_insert_before_edge_case(ll):
#     # ll.insertBefore(None,2)
#     with pytest.raises(TypeError):
#         ll.insertBefore(None,2)
#     # expected = "head -> [5] -> [4] -> [3] -> X"
#     # actual = ll.__str__()
#     # assert expected == actual 

# def test_insert_after_edge_case(ll):
#     ll.insertBefore(None,2)
#     expected = "head -> [5] -> [4] -> [3] -> X"
#     actual = ll.__str__()
#     assert expected == actual 

def test_kth_from_end(ll):
    ll.append(2)
    expected = 3
    actual = ll.kthFromEnd(1)
    assert expected == actual

def test_kth_from_end_with_index_out_of_range(ll):
    ll.append(2)
    expected = "index out of range"
    actual = ll.kthFromEnd(6)
    assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(5)
    ll.append(4)
    ll.append(3)
    return ll