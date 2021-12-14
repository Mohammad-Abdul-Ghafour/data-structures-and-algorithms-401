from python.hashmapLeftJoin.hashmap_left_join import left_join
from python.hashtable.hash_table import HashTable
import pytest

def test_left_join(table1,table2):  
    expected = [['diligent', 'employed', 'idle'], ['outfit', 'garb', 'NULL'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]
    actual = left_join(table1,table2)
    assert expected == actual

def test_left_join_right_table_is_empty(table1,table3):  
    expected = [['diligent', 'employed', 'NULL'], ['outfit', 'garb', 'NULL'], ['fond', 'enamored', 'NULL'], ['guide', 'usher', 'NULL'], ['wrath', 'anger', 'NULL']]
    actual = left_join(table1,table3)
    assert expected == actual

def test_left_join_left_table_is_empty(table3,table1):  
    expected = []
    actual = left_join(table3,table1)
    assert expected == actual

@pytest.fixture
def table1():
    table1 = HashTable()
    table1.add('fond', 'enamored')
    table1.add('wrath', 'anger')
    table1.add('diligent', 'employed')
    table1.add('outfit', 'garb')
    table1.add('guide', 'usher')

    return table1

@pytest.fixture
def table2():
    table2 = HashTable()
    table2.add('fond', 'averse')
    table2.add('wrath', 'delight')
    table2.add('diligent', 'idle')
    table2.add('guide', 'follow')
    table2.add('flow', 'jam')

    return table2

@pytest.fixture
def table3():
    table3 = HashTable()

    return table3
