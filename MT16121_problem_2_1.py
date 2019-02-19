# Ankit Sharma
# MT16121
# Python 2.7


class Graph:
    def __init__(self, list_of_nodes, list_of_edges):
        self.list_of_nodes = list_of_nodes
        self.list_of_edges = list_of_edges


class Edge:
    def __init__(self, source, sink):
        self.source = source
        self.sink = sink


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def fleurys_algorithm(my_g):
    list_to_be_returned = []
    number_of_odd_degree_nodes, n_list = check_odd_vertices(my_graph)
    if number_of_odd_degree_nodes == 2:
        current_node = n_list[0]
        list_of_selected_edges = get_edges(current_node, my_g)
        bridge_flag = 0
        for my_e in list_of_selected_edges:
            if check_bridge(my_e, my_g) == 0:
                current_edge = my_e
                bridge_flag = 1
                break
        if bridge_flag == 0:
            current_edge = list_of_selected_edges[0]
        while len(my_g.list_of_edges) != 0:
            node1 = current_edge.source
            node2 = current_edge.sink
            if node1 == current_node:
                current_node = node2
            else:
                current_node = node1
            list_to_be_returned.append(current_edge)
            my_g.list_of_edges = burn_edge(current_edge, my_g)
            if len(my_g.list_of_edges) != 0:
                list_of_selected_edges = get_edges(current_node, my_g)
                bridge_flag = 0
                for my_e in list_of_selected_edges:
                    if check_bridge(my_e, my_g) == 0:
                        current_edge = e
                        bridge_flag = 1
                        break
                if bridge_flag == 0:
                    current_edge = list_of_selected_edges[0]
    elif number_of_odd_degree_nodes == 0:
        current_node = my_g.list_of_nodes[0]
        list_of_selected_edges = get_edges(current_node, my_g)
        bridge_flag = 0
        for my_e in list_of_selected_edges:
            if check_bridge(my_e, my_g) == 0:
                current_edge = my_e
                bridge_flag = 1
                break
        if bridge_flag == 0:
            current_edge = list_of_selected_edges[0]
        while len(my_g.list_of_edges) != 0:
            node1 = current_edge.source
            node2 = current_edge.sink
            if node1 == current_node:
                current_node = node2
            else:
                current_node = node1
            list_to_be_returned.append(current_edge)
            my_g.list_of_edges = burn_edge(current_edge, my_g)
            if len(my_g.list_of_edges) != 0:
                list_of_selected_edges = get_edges(current_node, my_g)
                bridge_flag = 0
                for my_e in list_of_selected_edges:
                    if check_bridge(my_e, my_g) == 0:
                        current_edge = e
                        bridge_flag = 1
                        break
                if bridge_flag == 0:
                    current_edge = list_of_selected_edges[0]
    else:
        print 'Eulerian path not possible'
    return list_to_be_returned


def burn_edge(my_edge, my_graph):
    my_graph.list_of_edges.remove(my_edge)
    return my_graph.list_of_edges


def get_dfs(my_graph):
    traversal = []
    s = Stack()
    s.push(my_graph.list_of_nodes[0])
    while len(s.items)!= 0:
        top = s.pop()
        traversal.append(top)
        node_list = get_nodes(top, my_graph)
        for nd in node_list:
            flag = 0
            for tr in traversal:
                if nd == tr:
                    flag = 1
            if flag == 0:
                s.push(nd)
    return traversal


def check_bridge(my_edge, my_graph):
    val_to_be_returned = -1
    my_graph.list_of_edges.remove(my_edge)
    dfs_traversal = get_dfs(my_graph)
    if cmp(my_graph.list_of_nodes, dfs_traversal) == 0:
        val_to_be_returned = 0
    else:
        val_to_be_returned = 1
    my_graph.list_of_edges.append(my_edge)
    return val_to_be_returned

def get_nodes(my_node, my_graph):
    list_of_nodes = []
    for e in my_graph.list_of_edges:
        n1 = e.source
        n2 = e.sink
        if n1 == my_node:
            list_of_nodes.append(n2)
        elif n2 == my_node:
            list_of_nodes.append(n1)
    return list_of_nodes

def get_edges(my_node, my_graph):
    list_to_be_returned = []
    for e in my_graph.list_of_edges:
        if e.source == my_node or e.sink == my_node:
            list_to_be_returned.append(e)
    return list_to_be_returned

def check_odd_vertices(my_g):
    node_list = []
    number_of_vertices_with_odd_degree = 0
    for node in my_g.list_of_nodes:
        degree_contribution = 0
        for edge in my_g.list_of_edges:
            if edge.source == node or edge.sink == node:
                degree_contribution += 1
        if degree_contribution%2 == 1:
            number_of_vertices_with_odd_degree += 1
            node_list.append(node)
    return number_of_vertices_with_odd_degree, node_list


number_of_vertices = int(input())
number_of_edges = int(input())
list_of_e = []
list_of_n = []
for i in range(0, number_of_edges):
    line = raw_input()
    source_sink_list = line.split(' ')

    # Maintain edge list
    edge = Edge(source_sink_list[0], source_sink_list[1])
    list_of_e.append(edge)

    # Maintain node list
    list_of_n.append(source_sink_list[0])
    list_of_n.append(source_sink_list[1])
    my_set = set(list_of_n)
    list_of_n = list(my_set)

my_graph = Graph(list_of_n, list_of_e)

eulerian_path = fleurys_algorithm(my_graph)

for e in eulerian_path:
    print e.source + '-' + e.sink,

