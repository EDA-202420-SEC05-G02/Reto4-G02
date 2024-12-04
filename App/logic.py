import time
from DataStructures.Graph import adj_list_graph as adj
import csv


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    UserGraph = adj.new_graph()
    return UserGraph
    
# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    relationships = "relationships_"+filename+".csv"
    userinfo = "users_info_"+filename+".csv"    
    with open(filename, mode='r') as csv_file:    
        csv_reader = csv.DictReader(csv_file)   
        #Un poco demorado pero parece servir? Con tal que la carga sea rapida y los REQ's se manejen rapido esta bien (:    
        #Accidents-large toma 12 segundos para cargar en mi PC ><
        #Small esta listo en 2.5 entonces bien C:
        for row in csv_reader:
            for tipo_info in catalog:
                if row[tipo_info] == "" or row[tipo_info] == " ":                    
                    rbt.put(catalog[tipo_info], row["ID"], "Unknown")                
                else:                
                    rbt.put(catalog[tipo_info], row["ID"], row[tipo_info])                   
        return catalog

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
