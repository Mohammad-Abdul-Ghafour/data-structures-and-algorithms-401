from _pytest.python_api import raises
from python.stacksAndQueues.stack_and_queues import Stack

class PseudoQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.front = None
        self.rear = None

    def enqueue(self,value):
        if self.stack1.is_empty():
            self.stack1.push(value)
            self.front = self.stack1.top
        else:
            self.stack1.push(value)
        self.rear = self.stack1.top

    def dequeue(self):
        if self.stack1.is_empty():
            raise ValueError("The Queue Is Empty")

        while not self.stack1.is_empty():
            temp = self.stack1.pop()
            self.stack2.push(temp)
        dequeue = self.stack2.pop()

        while not self.stack2.is_empty():
            temp = self.stack2.pop()
            if self.stack1.is_empty():
                self.stack1.push(temp)
                self.front = self.stack1.top
            else:
                self.stack1.push(temp)

        self.rear = self.stack1.top
        if self.stack1.is_empty() and self.stack2.is_empty():
            self.rear = None
            self.front = None
        return dequeue

    def peek(self):
        if self.front == None:
            raise ValueError("This Queue Is Empty")
        return self.front.value

    def __str__(self):
        outPut = "rear -> "
        if self.rear is None:
            outPut += "None -> front"
        else:
            current = self.rear
            while current != None:
                outPut += "["+f"{current.value}"+"] -> "
                current = current.next
            outPut += "front"
            return outPut


if __name__ == "__main__":
    que = PseudoQueue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    print(que.rear.next)
    print(que.__str__())
    # print(que.dequeue())
    que.dequeue()
    # print(que.stack1.top.next.value)
    # print(que.front.next)
    print(que.rear.next)
    print(que.__str__())
    # print(que.rear.value,que.front.value,que.peek())

