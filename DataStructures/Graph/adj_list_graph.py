from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt

def new_graph(initial_capacity=10, directed=False):
    graph = {
        "vertices": mp.new_map(initial_capacity, 0.5), 
        "information": mp.new_map(initial_capacity, 0.5),  
        "edges": 0,  
        "directed": directed  
    }
    graph["in_degree"] = None

    return graph

def insert_vertex(graph, vertex_id, vertex_info):
    if mp.get(graph["vertices"], vertex_id) is None:
        edges = lt.new_list()
        mp.put(graph["vertices"], vertex_id, edges)
        mp.put(graph["information"], vertex_id, vertex_info)
    
def edges(graph):
    edges_list = lt.new_list()
    for vertex in mp.keys(graph["vertices"]):
        edges = mp.get(graph["vertices"], vertex)
        for edge in lt.iterator(edges):
            lt.add_last(edges_list, edge)
    return edges_list

def num_vertices(graph):
    return graph["vertices"]["size"]

def num_edges(graph):
    return graph["edges"]

def vertices(graph):
    vertex_list = lt.new_list()     
    if graph["vertices"]["size"] == 0:
        return vertex_list      
    for vertex_id in mp.keys(graph["vertices"]):
        lt.add_last(vertex_list, vertex_id) 
    
    return vertex_list

def edges(graph):
    edges_list = lt.new_list()
    vertex_map = graph["vertices"]
    vertex_keys = mp.key_set(vertex_map)
    for vertex in vertex_keys:
        vertex_edges = mp.get(vertex_map, vertex)
        if vertex_edges is not None:
            for edge in vertex_edges["elements"]:
                lt.add_last(edges_list, edge)

    return edges_list


def degree(graph, vertex_id):
    vertex_map = graph["vertices"]
    vertex_data = mp.get(vertex_map, vertex_id)
    
    if vertex_data is None:
        return None 
    return vertex_data["size"]


def in_degree(graph, vertex_id):
    if not graph["directed"]:
        return None 

    vertex_map = graph["vertices"]
    vertex_data = mp.get(vertex_map, vertex_id)

    if vertex_data is None:
        return None
    
    in_degree_count = 0
    vertex_keys = mp.key_set(vertex_map)
    
    for vertex_key in vertex_keys:
        vertex_info = mp.get(vertex_map, vertex_key)
        if vertex_info is not None and "elements" in vertex_info:
            for edge in vertex_info["elements"]:
                if edge["vertex_b"] == vertex_id: 
                    in_degree_count += 1

    return in_degree_count


def add_edge(graph, vertex_a, vertex_b, weight):
    vertex_map = graph["vertices"]
    vertex_data_a = mp.get(vertex_map, vertex_a)
    vertex_data_b = mp.get(vertex_map, vertex_b)

    if vertex_data_a is None or vertex_data_b is None:
        return 
    edge = {"vertex_a": vertex_a, "vertex_b": vertex_b, "weight": weight}
    edges_a = vertex_data_a["elements"]
    if edges_a is None:
        edges_a = []
    edges_a.append(edge) 
    vertex_data_a["elements"] = edges_a
    vertex_data_a["size"] += 1
    graph["edges"] += 1

