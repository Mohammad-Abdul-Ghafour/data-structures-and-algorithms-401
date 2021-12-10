from python.hashtable.hash_table import HashTable
import pytest

def test_hash_table_add_and_get(hashtable):
    expected = 10
    actual = hashtable.get("mohammad")
    assert expected == actual

def test_hash_table_get_None(hashtable):  
    expected = None
    actual = hashtable.get("Yahya")
    assert expected == actual

def test_hash_table_contain_True(hashtable):  
    expected = True
    actual = hashtable.contains("mohammad")
    assert expected == actual

def test_hash_table_contain_False(hashtable):  
    expected = False
    actual = hashtable.contains("yahya")
    assert expected == actual

@pytest.fixture
def hashtable():
    table = HashTable()
    table.add("ahmad",5)
    table.add("hamad",6)
    table.add("mohammad",10)
    return table