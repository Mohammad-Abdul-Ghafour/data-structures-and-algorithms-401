# Trees
A binary tree is a data structure in which every node or vertex has atmost two children.

a binary tree can be represented in different ways with different data structures(dictionary, list) and class representation for a node.

## Challenge
1. Create a Binary Tree class that have the following methods:
   * **`pre order`**
   * **`in order`**
   * **`post order`**
2. Create a Binary Search Tree class, This class should be a sub-class of the Binary Tree Class, with the following additional methods :
   * **`Add`** : adds a new node with that value in the correct location in the binary search tree.
   * **`Contains`** : returns boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
* Time:
   * Binary Tree :
      1. **`preOrder()`** : O(n)
      2. **`inOrder()`** : O(n)
      3. **`postOrder()`** : O(n)
   * Binary Search Tree :
      1. **`add()`** : log(n)
      2. **`contain()`** : log(n)

* Space:
   * Binary Tree :
      1. **`preOrder()`** : O(h) where h is the height of the tree (number of edges)
      2. **`inOrder()`** : O(h) where h is the height of the tree 
      3. **`postOrder()`** : O(h) where h is the height of the tree 
   * Binary Search Tree :
      1. **`add()`** : O(1)
      2. **`contain()`** : O(n)

## API
* Binary Tree:
  1. **`preOrder()`** : traverse through the tree one node by another starting from the root node, the left node and, then the right.
  2. **`inOrder()`** : traverse through the tree one node by another starting from the left node, the root node and, then the right.
  3. **`postOrder()`** : traverse through the tree one node by another starting from the left node, the right node and, then the root.
* Binary Search Tree:
  1. **`add()`** : add a value in the right node in sorted tree where if the value is smaller then the root then it is should be added on its left, while it is added on its right if it is greater then the root.
  2. **`contain()`** : traverse through the tree and check if a value exists. First, check if the value is greater than the root or smaller, then only traverse the half of the tree that matches the comparisons.