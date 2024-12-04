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
    relationships = "Data/relationships_"+filename+".csv"
    userinfo = "Data/users_info_"+filename+".csv" 
       
    with open(userinfo, mode='r') as csv_file:    
        csv_reader = csv.DictReader(csv_file, delimiter=';')   
        user = {"ID" : "", "UserData" : {"USER_NAME": "", 
                                         "USER_TYPE": "", 
                                         "AGE": 0,
                                         "JOIN_DATE" : "",
                                         "PHOTO" : "",
                                         "HOBBIES" : "",
                                         "CITY" : "",
                                         "LATITUDE": 0,
                                         "LONGITUDE" : 0                                                      
                                         }}   
        for row in csv_reader:
            if row["USER_ID"] == '' or row["USER_ID"] == ' ':
                user["ID"] == 'Unknown'
            else:
                user["ID"] = row["USER_ID"]
                
            for dato in user["UserData"]:
                if row[dato] == '' or row[dato] == ' ':
                    user["UserData"][dato] = ' Unknown'
                else:
                    user["UserData"][dato] = row[dato]
            
    
        
        
        
        
                
            

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
