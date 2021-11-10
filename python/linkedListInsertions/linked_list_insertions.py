from typing import Counter


class Node:
    def __init__(self,value = None):
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

    def kthFromEnd(self,index):
        current = self.head
        arr = []
        arr.append(current)
        while current.next != None:
            arr.append(current.next)
            current = current.next
        end_index = len(arr) - (index + 1)
        try:
            if end_index > len(arr) or end_index < 0:
                raise IndexError("index out of range")
            return arr[end_index].value
        except IndexError:
            return "index out of range"


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

# def zip_lists(linkedList1 , linkedList2):
#     try:
#         a = linkedList1.head
#         b = linkedList2.head
#         if a is None and b is None:
#             raise ValueError("The two linked list are empty")
#         elif a is None:
#             return linkedList2.__str__()
#         elif b is None:
#             return linkedList1.__str__()
#         else:
#             while b != None:
#                 linkedList1.insertAfter(a.value,b.value)
#                 print(linkedList1)
#                 if a.next != None:    
#                     a = a.next
#                 if a.next != None:    
#                     a = a.next
#                 b = b.next
#         return linkedList1.__str__()
#     except AttributeError:
#         return "One or two of the inputs is not a linked list"

def zip_lists(linkedList1 , linkedList2):
    try:

        dummy = Node()
        tail = dummy
        a = linkedList1.head
        b = linkedList2.head
        if a is None and b is None:
            raise ValueError("The two linked list are empty")
        elif a is None:
            return linkedList2.__str__()
        elif b is None:
            return linkedList1.__str__()
        else:
            while True:
                if a is None:
                    tail.next = b
                    break
                elif b is None:
                    tail.next = a
                    break
                tail.next = a
                tail = a
                a = a.next
    
                tail.next = b
                tail = b
                b = b.next
        return linkedList1.__str__()
    except AttributeError:
        return "One or two of the inputs is not a linked list"
 


def palindrome_linked_list(ll):
    a = ll.__str__()
    if ll.head == None:
        return "The linked list is empty"
    current = ll.head
    while current.next != None:
        temp_node = current.next
        current.next = current.next.next
        temp_node.next = ll.head
        ll.head = temp_node
    if a == ll.__str__():
        return True
    return False

        
if __name__ == '__main__':
    ll = LinkedList()
    ll2 = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    ll.append(7)
    ll2.append(3)
    ll2.append(4)
    ll2.append(5)
    a = print(ll)
    # a = ll
    print(ll2)
    # a = 1
    # b = 2
    print(zip_lists(ll,ll2)) 
    # l = palindrome_linked_list(ll)
    # print(l)
    # l = palindrome_linked_list(ll)
    # print(l)
    # b = str(print(ll))




