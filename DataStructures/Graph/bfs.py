from DataStructures.Graph import graph_search as gs
from DataStructures.Graph import queue as qu
from DataStructures.Graph import stack as st

def breadth_first_search(my_graph, source):
    """
    Inicia un recorrido Breadth First Search (BFS) sobre el grafo a partir de un vertice inicial.
    Crea una estructura de busqueda graph_search y posteriormente llama a la funcion bfs_vertex.

    :param my_graph: El grafo a recorrer
    :type my_graph: dict
    :param source: Llave del vertice de inicio del recorrido.
    :type source: any

    :returns: Estructura de busqueda
    :rtype: graph_search
    """
    search = gs.new_graph_search(source)
    bfs_vertex(search, my_graph, source)
    return search

def bfs_vertex(search, my_graph, source):
    """
    Función auxiliar para calcular un recorrido BFS usada por la función breadth_first_search.

    :param search: Estructura para almacenar el recorrido
    :type search: graph_search
    :param my_graph: El grafo a recorrer
    :type my_graph: dict
    :param source: Vertice de inicio del recorrido.
    :type source: any

    :returns: Estructura de busqueda
    :rtype: graph_search
    """
    queue = ()
    qu.enqueue(queue, source)
    search["visited"][source] = True

    while not qu.is_empty(queue):
        current_vertex = qu.dequeue(queue)
        neighbors = my_graph.get(current_vertex, [])
        for neighbor in neighbors:
            if neighbor not in search["visited"]:
                search["visited"][neighbor] = True
                qu.enqueue(queue, neighbor)

    return search

def has_path_to(search, vertex):
    """
    Indica si existe un camino entre el vertice source y el vertice vertex a partir de una estructura search.

    :param search: Estructura de recorrido BFS
    :type search: graph_search
    :param vertex: Vertice destino
    :type vertex: any

    :returns: True si existe un camino entre source y vertex, False en caso contrario
    :rtype: bool
    """
    return vertex in search["visited"]

def path_to(search, vertex):
    """
    Retorna el camino entre el vertices source y el vertice vertex a partir de una estructura de busqueda search.

    :param search: Estructura de recorrido BFS
    :type search: graph_search
    :param vertex: Vertice destino
    :type vertex: any

    :returns: Una pila con el camino entre source y vertex. Si no existe camino retorna None.
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
