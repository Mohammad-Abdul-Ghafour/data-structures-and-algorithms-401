# Hashtables

**`Hashtable`** is a data structure that implements an associative array abstract data type, a structure that can map keys to values.

A hashtable uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.

## Challenge

Implement a hashtable that has **`hash`** method, **`add`** method, **`get`** method and **`contains`** method.

## Approach & Efficiency

I used **`Linkedlist`** as base structure inside the map array in the hashtable to avoid collision I found it the best way.

1. **`hash`** method:
    * Time : O(n)
        * Because we loop through the key to get each letter ascii code.
    * Space : O(1)
        * We only use specific varaible and we store in the memory once.
2. **`add`** method:
    * Time : O(n)
        * We used the hash method inside of it and we also used the insert method from the linkedlist class.
    * Space : O(1)
        * We only adding one item to the linkedlist.
3. **`get`** method:
    * Time : O(n)
        * We used the hash method inside of it and also we have while loop that loop through the linkedlist.
    * Space : O(1)
        * We only use specific varaible and we store in the memory once.
4. **`contains`** method:
    * Time : O(n)
        * We used the hash method inside of it and also we have while loop that loop through the linkedlist.
    * Space : O(1)
        * We only use specific varaible and we store in the memory once.

## API
* **`hash`** method that takes a string and hash it to integer.
* **`add`** method to add to the hashtabe.
* **`get`** method to get stored data using keys.
* **`contains`** method that check if the key is already stored or not.