class Node:

    def __init__(self,value=None):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise ValueError("This stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.top == None:
            raise ValueError("This stack is empty")
        return self.top.value
    
    def is_empty(self):
        return not self.top
    
class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        node = Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node    

    def dequeue(self):
        if self.rear == None:
            raise ValueError("This stack is empty")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.front == None:
            raise ValueError("This stack is empty")
        return self.front.value

    def is_empty(self):
        return not self.front
