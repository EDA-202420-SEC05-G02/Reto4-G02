from DataStructures.Graph import graph_search as gs
from DataStructures.Graph import stack as st

def depth_first_search(my_graph, source):
    """
    Inicia un recorrido Depth First Search (DFS) sobre el grafo a partir de un vertice inicial.
    Crea una estructura de busqueda graph_search y posteriormente llama a la funcion dfs_vertex.

    :param my_graph: El grafo a recorrer
    :type my_graph: dict
    :param source: Llave del vertice de inicio del recorrido.
    :type source: any

    :returns: Estructura de busqueda
    :rtype: graph_search
    """
    search = gs.new_graph_search(source)
    dfs_vertex(search, my_graph, source)
    return search

def dfs_vertex(search, my_graph, vertex):
    """
    Funcion auxiliar para calcular un recorrido DFS usada por la funcion depth_first_search.

    :param search: Estructura para almacenar el recorrido
    :type search: graph_search
    :param my_graph: El grafo a recorrer
    :type my_graph: dict
    :param vertex: Vertice de inicio del recorrido.
    :type vertex: any

    :returns: Una estructura para determinar los vertices conectados a source
    :rtype: graph_search
    """
    stack = st.new_stack()
    st.push(stack, vertex)

    while not st.is_empty(stack):
        current_vertex = st.pop(stack)
        if current_vertex not in search["visited"]:
            search["visited"][current_vertex] = True
            neighbors = my_graph.get(current_vertex, [])
            for neighbor in reversed(neighbors):
                if neighbor not in search["visited"]:
                    st.push(stack, neighbor)

    return search

def has_path_to(search, vertex):
    """
    Indica si existe un camino entre el vertice source y el vertice vertex a partir de una estructura search.

    :param search: Estructura de recorrido DFS
    :type search: graph_search
    :param vertex: Vertice destino
    :type vertex: any

    :returns: True si existe un camino entre source y vertex, False en caso contrario
    :rtype: bool
    """
    return vertex in search["visited"]

def path_to(search, vertex):
    """
    Retorna el camino entre el vertices source y el vertice vertex a partir de una estructura search.

    :param search: La estructura con el recorrido
    :type search: graph_search
    :param vertex: Vertice destino
    :type vertex: any

    :returns: Una pila con el camino entre el vertices source y el vertice vertex
    :rtype: stack
    """
    if not has_path_to(search, vertex):
        return None

    path = st.new_stack()
    current = vertex

    while current is not None and current in search["visited"]:
        st.push(path, current)
        current = search["visited"].get(current)

    return path