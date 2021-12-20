from python.graphbusinesstrip.graph import Graph 

def businessTrip(graph,city_list):

    total = 0
    for index, city in enumerate(city_list):
        if index + 1 < len(city_list):
            print(city)
            city_neighbors = graph.get_neighbors(city)
            print(city_neighbors)
            found = False

            for edge in city_neighbors:
                if edge.vertex == city_list[index+1]:
                    total += edge.weight
                    found = True
                    break
            if found == False:
                return f"False , ${total}"

    return f"True , ${total}"

    # total = 0
    # def travers(graph,city_list,total):
    #     for index, city in enumerate(city_list):
    #         if index + 1 < len(city_list):
    #             found = False
    #             city_neighbors = graph.get_neighbors(city)
    #             print(city_neighbors)


    #             for edge in city_neighbors:

    #                     if edge.vertex == city_list[index+1]:
    #                         print(edge.weight)
    #                         total += edge.weight
    #                         found = True
    #                         break
    #             if found == False:
    #                 for i,val in enumerate(city_neighbors):
    #                     print(val)
    #                     total += travers(graph,[val,city_list[index+1]],total)
    #     return total
    # total = travers(graph,city_list,total)
    # return f"${total}"

if __name__=="__main__":
    # graph = Graph()
    # node1 = graph.add_node(1)
    # node2 = graph.add_node(2)
    # graph.add_edge(node1,node2)
    # print(graph.get_neighbors(node1))
    # print(graph.get_nodes())
    # print(graph.size())
    # print(graph.bfs(node1))

    graph1 = Graph()
    node1 = graph1.add_node("a")
    node2 = graph1.add_node("b")
    node3 = graph1.add_node("c")
    node4 = graph1.add_node("d")
    graph1.add_edge(node1,node2,20)
    graph1.add_edge(node2,node1,20)
    graph1.add_edge(node2,node3,30)
    graph1.add_edge(node3,node2,30)
    graph1.add_edge(node1,node4,15)
    graph1.add_edge(node4,node1,15)
    # print(graph1.bfs(node1))
    total = businessTrip(graph1,[node1,node2,node3])
    # total = businessTrip(graph1,["a","b","c"])
    print(node1)
    print(total)