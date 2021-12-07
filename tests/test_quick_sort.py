from python.QuickSort.quick_sort import quick_sort
import pytest

def test_quick_sort(array):  
    expected = [-2,5,8,12,18,20]
    actual = quick_sort(array[0], 0 , len(array[0])-1)
    print(actual)
    assert expected == actual
    expected2 = [5,5,5,7,7,12]
    actual2 = quick_sort(array[1], 0 , len(array[1])-1)
    assert expected2 == actual2
    expected3 = [2,3,5,7,11,13]
    actual3 = quick_sort(array[2], 0 , len(array[2])-1)
    assert expected3 == actual3

def test_quick_sort_empty_array(array):  
    with pytest.raises(ValueError):
        quick_sort(array[3],0,len(array[3])-1)

def test_quick_sort_array_of_one_value(array):  
    expected = [1]
    actual = quick_sort(array[4],0,len(array[4])-1)
    assert expected == actual

@pytest.fixture
def array():
    arr = [20,18,12,8,5,-2]
    arr1 = [5,12,7,5,5,7]
    arr2 = [2,3,5,7,13,11]
    arr3 = []
    arr4 = [1]
    return arr , arr1 , arr2 , arr3 , arr4