import pytest
from python.stackQueueAnimalShelter.stack_queue_animal_shelter import AnimalShelter

def test_enqueue_dog():
    que = AnimalShelter()
    que.enqueue({'dog':'alex'})
    expexted = {'dog':'alex'}
    actual = que.dogQueue.rear.value
    assert expexted == actual

def test_dequeue_dog(que):
    expexted = 'dog'
    actual = que.dequeue("dog")
    assert expexted == actual

def test_enqueue_cat():
    que = AnimalShelter()
    que.enqueue({'cat':'lolo'})
    expexted = {'cat':'lolo'}
    actual = que.catQueue.rear.value
    assert expexted == actual

def test_dequeue_cat(que):
    expexted = 'cat'
    actual = que.dequeue("cat")
    assert expexted == actual

@pytest.fixture
def que():
    que = AnimalShelter()
    que.enqueue({'dog':'alex'})
    que.enqueue({'cat':'lolo'})
    que.enqueue({'cat':'shy'})
    que.enqueue({'dog':'fox'})
    return que
