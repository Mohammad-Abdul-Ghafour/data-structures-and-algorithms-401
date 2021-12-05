from python.InsertionSort.insertion_sort import insertion_sort
import pytest

def test_insertion(array):  
    expected = [-2,5,8,12,18,20]
    actual = insertion_sort(array[0])
    assert expected == actual
    expected2 = [5,5,5,7,7,12]
    actual2 = insertion_sort(array[1])
    assert expected2 == actual2
    expected3 = [2,3,5,7,11,13]
    actual3 = insertion_sort(array[2])
    assert expected3 == actual3

def test_insertion_empty_array(array):  
    with pytest.raises(ValueError):
        insertion_sort(array[3])

def test_insertion_array_of_one_value(array):  
    expected = [1]
    actual = insertion_sort(array[4])
    assert expected == actual

@pytest.fixture
def array():
    arr = [20,18,12,8,5,-2]
    arr1 = [5,12,7,5,5,7]
    arr2 = [2,3,5,7,13,11]
    arr3 = []
    arr4 = [1]
    return arr , arr1 , arr2 , arr3 , arr4