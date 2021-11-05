class Node:
    def __init__(self,value):
        try:
            if value is None:
                raise ValueError
            self.value = value
            self.next = None # head
        except ValueError:
            return None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def includes(self,val):
        current = self.head
        if current.value == val:
            return True
        else:
            while current.next != None:
                current = current.next
                if current.value == val:
                    return True
        return False
        
    def __str__(self):
        outPut = "head -> "
        if self.head is None:
            outPut += "Null"
        else:
            current = self.head
            while(current):
                outPut += "{"+f"{current.value}"+"} -> "
                current = current.next
            outPut += "Null"
            return outPut

    
if __name__ == "__main__":
    ll = None
    print("""
            ***************************************************
                To exit the program type "exit" at any time     
              To search for a value type "search" at any time
            ***************************************************
    """)

    def searchForValue(li):
        try:
            value = input("please enter the value you want to search : >> ")
            if value != "exit":
                print(li.includes(value))
                print(li)
        except ValueError:
            print ("you should enter a valid value")

    def nodesValue(len,li):
        while len > 0 :
            node = input("please enter the value : >> ")
            if node != "exit" or node != "search":
                while node == None:
                    node = input("please enter valid value : >> ")
                li.insert(node)
            elif node == "search":
                searchForValue()
            len -= 1
        # print(li)
        searchForValue(li)

    def linkedListLength(li):
        try:
            newList = input("please  enter the list length >> ")
            if newList != "exit" or newList !="search":
                int(newList)
                li = LinkedList()
                nodesValue(int(newList),li)
            elif newList == "search" and li != None:
                searchForValue(li)
        except :
            print("""

            *********************************************
                      Please enter valid number         
                 or type "exit" to exit the program  
               or type "search" to search for a value     
            *********************************************

            """)
            linkedListLength()
    linkedListLength(ll)
    
    
    
    # ll.insert("4")
    # ll.insert("3")

    
