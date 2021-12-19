from python.graphs.graph import Graph
import pytest


def test_graph_add_node():
    graph = Graph()
    node = graph.add_node(1)
    # actual = list(graph.get_nodes())
    # expected = [node]
    # assert expected == actual

def test_graph_add_edge():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    graph.add_edge(node1,node2)

    
def test_graph_get_nodes(graph):
    actual = list(graph[0].get_nodes())
    expected = [graph[1] , graph[2]]
    assert expected == actual

def test_graph_get_neighbors_and_weight(graph):
    actual = list(graph[0].get_neighbors(graph[1]))[0].vertex
    expected = graph[2]
    assert expected == actual
    actual1 = list(graph[0].get_neighbors(graph[1]))[0].weight
    expected1 = 0
    assert expected1 == actual1

def test_graph_size(graph):
    actual = graph[0].size()
    expected = 2
    assert expected == actual

def test_graph_with_one_node():
    graph = Graph()
    node = graph.add_node(1)
    actual = list(graph.get_nodes())
    expected = [node]
    assert expected == actual

def test_empty_graph():
    graph = Graph()
    actual = list(graph.get_nodes())
    expected = []
    assert expected == actual

def test_graph_bfs(graph1):
    actual = graph1[0].bfs(graph1[1])
    expected = [graph1[1].value,graph1[2].value,graph1[4].value,graph1[3].value]
    assert expected == actual

@pytest.fixture
def graph():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    graph.add_edge(node1,node2)
    return [graph , node1 , node2]

@pytest.fixture
def graph1():
    graph1 = Graph()
    node1 = graph1.add_node(1)
    node2 = graph1.add_node(2)
    node3 = graph1.add_node(3)
    node4 = graph1.add_node(4)
    graph1.add_edge(node1,node2)
    graph1.add_edge(node2,node1)
    graph1.add_edge(node2,node3)
    graph1.add_edge(node3,node2)
    graph1.add_edge(node1,node4)
    graph1.add_edge(node4,node1)
    return [graph1 , node1 , node2 , node3 , node4]