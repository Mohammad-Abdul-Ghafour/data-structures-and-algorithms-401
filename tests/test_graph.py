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

@pytest.fixture
def graph():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    graph.add_edge(node1,node2)
    return [graph , node1 , node2]