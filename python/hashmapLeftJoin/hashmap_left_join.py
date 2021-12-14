from python.hashtable.hash_table import HashTable

def left_join(table1,table2):
    arr = []

    for i in table1.arr:
        if i != None:
            current = i.head
            while current:
                arr.append([current.value[0], current.value[1]])
                current = current.next

    for i in arr:
        if table2.contains(i[0]) == True:
            temp = table2.get(i[0])
            i.append(temp)
        else:
            i.append("NULL")

    return arr

if __name__ == "__main__":
    table1 = HashTable()
    table1.add('fond', 'enamored')
    table1.add('wrath', 'anger')
    table1.add('diligent', 'employed')
    table1.add('outfit', 'garb')
    table1.add('guide', 'usher')

    table2 = HashTable()
    table2.add('fond', 'averse')
    table2.add('wrath', 'delight')
    table2.add('diligent', 'idle')
    table2.add('guide', 'follow')
    table2.add('flow', 'jam')

    print(left_join(table1,table2))