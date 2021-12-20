from python.graphs.graph import Graph, Vertex, Edge
from python.graphbusinesstrip.graph_business_trip import businessTrip
import pytest



def test_input_metroville_pandora_returns_true(example):
    graph = example[0]
    metroville = example[3]
    pandora = example[1]
    actual = businessTrip(graph, [metroville, pandora])
    expected = "True , $82"
    assert actual == expected


def test_happy_path_multiple_cities_returns_true(example):
    graph = example[0]
    arendelle = example[2]
    monstropolis = example[4]
    naboo = example[6]
    actual = businessTrip(graph, [arendelle, monstropolis, naboo])
    expected = "True , $115"
    assert actual == expected


def test_unhappy_path_returns_fales(example):
    graph = example[0]
    naboo = example[6]
    pandora = example[1]
    actual = businessTrip(graph, [naboo, pandora])
    expected = "False , $0"
    assert actual == expected


def test_unhappy_path_with_multiple_cities_return_false(example):
    graph = example[0]
    narnia = example[5]
    arendelle = example[2]
    naboo = example[6]
    actual = businessTrip(graph, [narnia, arendelle, naboo])
    expected = "False , $0"
    assert actual == expected


@pytest.fixture
def example():
    graph1 = Graph()
    pandora = graph1.add_node("pandora")
    arendelle = graph1.add_node("arendelle")
    metroville = graph1.add_node("metroville")
    monstropolis = graph1.add_node("monstropolis")
    narnia = graph1.add_node("narnia")
    naboo = graph1.add_node("naboo")

    graph1.add_edge(pandora, arendelle, 150)
    graph1.add_edge(pandora, metroville, 82)

    graph1.add_edge(arendelle, pandora, 150)
    graph1.add_edge(arendelle, metroville, 99)
    graph1.add_edge(arendelle, monstropolis, 42)

    graph1.add_edge(metroville, pandora, 82)
    graph1.add_edge(metroville, narnia, 37)
    graph1.add_edge(metroville, naboo, 26)
    graph1.add_edge(metroville, monstropolis, 105)
    graph1.add_edge(metroville, arendelle, 99)

    graph1.add_edge(monstropolis, arendelle, 42)
    graph1.add_edge(monstropolis, metroville, 105)
    graph1.add_edge(monstropolis, naboo, 73)

    graph1.add_edge(narnia, metroville, 37)
    graph1.add_edge(narnia, naboo, 250)

    graph1.add_edge(naboo, narnia, 250)
    graph1.add_edge(naboo, metroville, 26)
    graph1.add_edge(naboo, monstropolis, 73)
    return graph1, pandora, arendelle, metroville, monstropolis, narnia, naboo