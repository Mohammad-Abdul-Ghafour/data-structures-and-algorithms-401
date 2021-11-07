class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def insertAfter(self,value,newValue):
        node = Node(newValue)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.value != value and current.next != None:
                current = current.next
            if current.next == None and current.value == value:
                current.next = node
            elif current.value == value:
                node.next = current.next
                current.next = node
    
    def insertBefore(self,value,newValue):
        node = Node(newValue)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            if current.value == value:
                node.next = current
                self.head = node
            else:
                prev = {}
                while current.value != value and current.next != None:
                    prev = current
                    current = current.next
                if current.value == value:
                    node.next = current
                    prev.next = node

    def __str__(self):
        outPut = "head -> "
        if self.head is None:
            outPut += "X"
        else:
            current = self.head
            while(current):
                outPut += "["+f"{current.value}"+"] -> "
                current = current.next
            outPut += "X"
            return outPut

