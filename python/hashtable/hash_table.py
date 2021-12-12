from python.linkedList.linked_list import LinkedList


class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.arr = [LinkedList() for _ in range(size)]

    def hash(self, key):
        _ascii = 0
        for ch in key:
            ascii_of_ch = ord(ch)
            _ascii+= ascii_of_ch
        temp = _ascii*599
        hashed_key = temp%self.size
        return hashed_key

    def add(self, key, value):
        hashed_key = self.hash(key)
        # print(hashed_key)
        self.arr[hashed_key].insert([key,value])

    def get(self, key):
        hashed_key=self.hash(key)
        current = self.arr[hashed_key].head
        value = None
        while current != None:
            if current.value[0] == key:
                value = current.value[1]
                break
            current = current.next
        return value
    
    def contains(self,key):
        hashed_key = self.hash(key)
        current = self.arr[hashed_key].head
        while current != None:
            if current.value[0] == key:
                return True
                break
            current = current.next
        return False

if __name__ == "__main__":
    hashtable= HashTable()
    hashtable.add("AHMAD",30)
    hashtable.add("YAHYA",30)
    hashtable.add("HAMAD",55)

    for index,item in enumerate(hashtable.arr):
        if item:
            print(index, item.head)
    
    value = hashtable.get('HAeMAD')
    print(value)
    print(hashtable.contains('HAMAD'))