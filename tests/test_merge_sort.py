from python.MergeSort.merge_sort import mergeSort
import pytest

def test_merge_sort(array):  
    expected = [-2,5,8,12,18,20]
    actual = mergeSort(array[0])
    assert expected == actual
    expected2 = [5,5,5,7,7,12]
    actual2 = mergeSort(array[1])
    assert expected2 == actual2
    expected3 = [2,3,5,7,11,13]
    actual3 = mergeSort(array[2])
    assert expected3 == actual3

def test_merge_sort_empty_array(array):  
    with pytest.raises(ValueError):
        mergeSort(array[3])

def test_merge_sort_array_of_one_value(array):  
    expected = [1]
    actual = mergeSort(array[4])
    assert expected == actual

@pytest.fixture
def array():
    arr = [20,18,12,8,5,-2]
    arr1 = [5,12,7,5,5,7]
    arr2 = [2,3,5,7,13,11]
    arr3 = []
    arr4 = [1]
    return arr , arr1 , arr2 , arr3 , arr4