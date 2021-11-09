from python.linkedListInsertions.linked_list_insertions import Node , LinkedList , zip_lists
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

def test_kth_from_end_last(ll):
    ll.append(2)
    expected = 2
    actual = ll.kthFromEnd(0)
    assert expected == actual

def test_kth_from_end_with_index_out_of_range(ll):
    ll.append(2)
    expected = "index out of range"
    actual = ll.kthFromEnd(6)
    assert expected == actual

def test_kth_from_end_with_index_negative(ll):
    ll.append(2)
    expected = "index out of range"
    actual = ll.kthFromEnd(-1)
    assert expected == actual

def test_kth_from_end_one_node():
    ll2 = LinkedList()
    ll2.append(1)
    expected = 1
    actual = ll2.kthFromEnd(0)
    assert expected == actual

def test_kth_from_end_middle(ll):
    ll.append(2)
    ll.append(1)
    expected = 3
    actual = ll.kthFromEnd(2)
    assert expected == actual

def test_zip_linked_lists(ll,ll2):
    expected = "head -> [5] -> [2] -> [4] -> [4] -> [3] -> [6] -> X"
    actual = zip_lists(ll,ll2)
    assert expected == actual

def test_zip_linked_lists_one_is_not_ll(ll2):
    ll3 = "hello"
    expected = "One or two of the inputs is not a linked list"
    actual = zip_lists(ll3,ll2)
    assert expected == actual

def test_zip_linked_lists_one_is_none(ll2):
    ll3 = LinkedList()
    expected = "head -> [2] -> [4] -> [6] -> X"
    actual = zip_lists(ll3,ll2)
    assert expected == actual

def test_zip_linked_lists_first_is_longer(ll4,ll2):
    expected = "head -> [2] -> [2] -> [4] -> [4] -> [6] -> [6] -> [6] -> [6] -> [6] -> X"
    actual = zip_lists(ll4,ll2)
    assert expected == actual

def test_zip_linked_lists_second_is_longer(ll2,ll4):
    expected = "head -> [2] -> [2] -> [4] -> [4] -> [6] -> [6] -> [6] -> [6] -> [6] -> X"
    actual = zip_lists(ll4,ll2)
    assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(5)
    ll.append(4)
    ll.append(3)
    return ll

@pytest.fixture
def ll2():
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    return ll2

@pytest.fixture
def ll4():
    ll4 = LinkedList()
    ll4.append(2)
    ll4.append(4)
    ll4.append(6)
    ll4.append(6)
    ll4.append(6)
    ll4.append(6)
    return ll4