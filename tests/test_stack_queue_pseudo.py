from python.stackQueuePseudo.stack_queue_pseudo import PseudoQueue
import pytest

def test_enqueue(pseudoQueue):
    # print(pseudoQueue.rear)
    expected = 3
    actual = pseudoQueue.rear.value
    assert expected == actual

def test_dequeue(pseudoQueue):
    expected = 1
    actual = pseudoQueue.dequeue()
    assert expected == actual

def test_dequeue_empty():
    que=PseudoQueue()
    with pytest.raises(ValueError):
        que.dequeue()

def test_peek(pseudoQueue):
    expected = 1
    actual = pseudoQueue.peek()
    assert expected == actual

def test_peek_empty():
    que=PseudoQueue()
    with pytest.raises(ValueError):
        que.peek()

@pytest.fixture
def pseudoQueue():
    que=PseudoQueue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    return que
