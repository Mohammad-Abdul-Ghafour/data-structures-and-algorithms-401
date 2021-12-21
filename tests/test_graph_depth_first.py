from python.graphDepthFirst.graph import Graph
from python.graphDepthFirst.graph_depth_first import dfs
import pytest


def test_graph_depth_first(graph1):
    expected = {1,2,3,4}
    actual = dfs(graph1[0],graph1[1])
    assert expected == actual
    

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