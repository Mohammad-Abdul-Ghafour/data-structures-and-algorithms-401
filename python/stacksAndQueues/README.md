# Stacks and Queues
* **`Stacks`** :

A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

Stacks follow these concepts :

1. **`FILO`** : First In Last Out
2. **`LIFO`** : Last In First Out

* **`Queues`** :

Queues same as Stacks a data structure that consists of Nodes.

But it follows these concepts :

1. **`FIFO`** : First In First Out
2. **`LILO`** : Last In Last Out

## Challenge
1. Build a class that create an empty stack and has its methods
   * *`push`* : (to add new node to the stack).
   * *`pop`* : (to remove a node from the top of the stack).
   * *`peek`* : (to return the value of the top node of the stack).
   * *`is_empty`* : (to check if the stack is empty or not).
2. Build a class that create an empty queue and has its methods :
   * *`enqueue`* : (to add new node to the rear of the queue).
   * *`dequeue`* : (to remove a node from the front of the queue).
   * *`peek`* : (to return the value of the front node of the queue).
   * *`is_empty`* : (to check if the queue is empty or not)

## Approach & Efficiency
1. Time : O(1) (for all methods in stacks and queues)
2. space : O(1) (for all methods in stacks and queues)

## API
1. **`Stacks Methods`** :
   * *`push`* : (to add new node to the stack).
   * *`pop`* : (to remove a node from the top of the stack).
   * *`peek`* : (to return the value of the top node of the stack).
   * *`is_empty`* : (to check if the stack is empty or not).
2. **`Queues Methods`** :
   * *`enqueue`* : (to add new node to the rear of the queue).
   * *`dequeue`* : (to remove a node from the front of the queue).
   * *`peek`* : (to return the value of the front node of the queue).
   * *`is_empty`* : (to check if the queue is empty or not)