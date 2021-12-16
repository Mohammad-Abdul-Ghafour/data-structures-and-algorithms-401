# Graphs

A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge

Implementing a Graph represented as an adjacency list.

## Approach & Efficiency

* Time: O(1)
  * AddNode(): O(1)
  * AddEdge(): O(1)
  * GetNodes(): O(1)
  * Size(): O(1)
* Space: O(n+m)
  * AddNode(): O(n)
  * AddEdge(): O(m)
  * GetNodes(): O(1)
  * Size(): O(1)

## API

* **`AddNode`** method :
  * Adds a new node to the graph.
  * Input : Takes in the value of that node.
  * Returns : The added node.
* **`AddEdge`** method :
  * Adds a new edge between two nodes in the graph include the ability to have a “weight”.
  * Input : Two nodes to be connected by the edge.
  * Returns : Nothing.
* **`GetNodes`** method :
  * Get all of the nodes in the graph as a set or list.
  * Input : Nothing.
  * Returns : A list or set of all nodes in the graph.
* **`GetNeighbors`** method :
  * Get a collection of edges connected to the given node.
  * Input : A node.
  * Returns : List of edges connected to the given node.
* Size():
  * Get the total number of nodes in the graph.
  * Input : Nothing.
  * Returns : Number of the nodes in the graph.


[Code Link](graph.py)

[Test Link](../../tests/test_graph.py)