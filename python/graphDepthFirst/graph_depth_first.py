from python.graphDepthFirst.graph import Graph
# from tests.test_graph import graph
def dfs(graph, start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start.value)
    neighbors = graph.get_neighbors(start)

    for edge in neighbors :
        if edge.vertex.value not in visited:
            dfs(graph, edge.vertex, visited)
    return visited

if __name__=="__main__":

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
    print(dfs(graph1,node1))