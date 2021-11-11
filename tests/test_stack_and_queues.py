import pytest
from python.stacksAndQueues.stack_and_queues import Stack , Node , Queue

# Can successfully push onto a stack
def test_stack_push_one():
    stack = Stack()
    stack.push(1)
    expected = 1
    actual = stack.top.value
    assert expected == actual

# Can successfully push multiple values onto a stack   
def test_stack_push_multi(stack):
    expected = 3
    actual = stack.top.value
    assert expected == actual

# Can successfully pop off the stack
def test_stack_pop_one(stack):
    expected = 3
    actual = stack.pop()
    assert expected == actual

# Can successfully empty a stack after multiple pops
def test_empty_stack_with_pop(stack):
    while stack.top != None:
        stack.pop()
    expected = None
    actual = stack.top
    assert expected == actual

# Can successfully peek the next item on the stack
def test_stack_peek(stack):
    current = stack.peek()
    expected = 3
    actual = current
    assert expected == actual

# Can successfully instantiate an empty stack
def test_stack_is_empty_true():
    stack = Stack()
    expected = True
    actual = stack.is_empty()
    assert expected == actual

def test_stack_is_empty_false(stack):
    expected = False
    actual = stack.is_empty()
    assert expected == actual

# Calling pop or peek on empty stack raises exception
def test_pop_or_peek_rais_error():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.pop()
    with pytest.raises(ValueError):
        stack.peek()

# Can successfully enqueue into a queue
def test_queue_enqueue_one():
    que = Queue()
    que.enqueue(1)
    expected = 1
    actual = que.rear.value
    assert expected == actual

# Can successfully enqueue multiple values into a queue
def test_queue_enqueue_multi(que):
    expected = 3
    actual = que.rear.value
    expected2 = 1
    actual2 = que.front.value
    assert expected == actual
    assert expected2 == actual2

# Can successfully dequeue out of a queue the expected value
def test_queue_dequeue_one(que):
    expected = 1
    actual = que.dequeue()
    assert expected == actual

# Can successfully empty a queue after multiple dequeues
def test_empty_queue_with_dequeue(que):
    while que.front !=None:
        que.dequeue()
    expected = None
    actual = que.front
    assert expected == actual

# Can successfully peek into a queue, seeing the expected value
def test_queue_peek(que):
    expected = 1
    actual = que.peek()
    assert expected == actual

# Can successfully instantiate an empty queue
def test_instantiate_empty_queue():
    que = Queue()
    expected = None
    actual = que.front
    assert expected == actual

# Calling dequeue or peek on empty queue raises exception
def test_dequeue_or_peek_raises_error():
    que = Queue()
    with pytest.raises(ValueError):
        que.dequeue()
    with pytest.raises(ValueError):
        que.peek()

# Check if the queue is empty
def test_queue_is_empty_true():
    que = Queue()
    expected = True
    actual = que.is_empty()
    assert expected == actual

def test_queue_is_empty_false(que):
    expected = False
    actual = que.is_empty()
    assert expected == actual

@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

@pytest.fixture
def que():
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    return que