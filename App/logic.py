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
    usuarios = 0
    relationships = "Data/relationships_"+filename+".csv"
    userinfo = "Data/users_info_"+filename+".csv" 
    # Se crea un diccionario para almacenar toda la informacion de seguidores.
    relationshipsdict = {}
    # Carga los datos de relationships
    with open(relationships, mode='r') as csv_file:    
        relationships_csv_reader = csv.DictReader(csv_file, delimiter=';') 
        # Loopea el archivo cargado, guardando el seguidor y el seguido en variables individuales. Verifica si ya existe, y crea una lista para guardar todos los vertices.
        # Id1 : [Id2, Id3] == Id1 Sigue a Id2 e Id3
        for r_row in relationships_csv_reader:
            Seguidor = float(r_row['FOLLOWER_ID'])
            SigueA = float(r_row['FOLLOWED_ID'])
            if Seguidor not in relationshipsdict:
                relationshipsdict[Seguidor] = []
            relationshipsdict[Seguidor].append(SigueA)
                
       
    with open(userinfo, mode='r') as csv_file:    
        csv_reader = csv.DictReader(csv_file, delimiter=';')  
        # Se crea diccionario vacio, donde se guardara el ID en una llave, y los datos en otra. 
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
        # Loop para los rows, agrega el ID a la llave ID, y verifica si el id existe. (Obvio tiene que existir pero por si las moscas ;)  )
        userdict = {}
        for row in csv_reader:
            if row["USER_ID"] == '' or row["USER_ID"] == ' ':
                user["ID"] == 'Unknown'
            else:
                user["ID"] = float(row["USER_ID"])
            # Loop que agrega los datos a UserData, y verifica si hay datos vacios.
            for dato in user["UserData"]:
                if row[dato] == '' or row[dato] == ' ':
                    user["UserData"][dato] = ' Unknown'
                else:
                    user["UserData"][dato] = row[dato]
                # Ahora agrega los datos de user en information
            userdict[user['ID']] = user['UserData']                
            usuarios += 1

        # Contador para verificar la existencia de ids de relationship en user_data :)
        # Tambien se encarga de eliminar duplicados en el dict de relaciones
        notfound = 0
        print ('Total usuarios en user_data = ',str(len(userdict)),', Total usuarios en relationship = ',str(len(relationshipsdict)))        
        for value in list(relationshipsdict.keys()):
            if value not in userdict:
                notfound += 1
                del relationshipsdict[value]                
        print ('Hay', str(notfound), 'IDs de', relationships, 'que no se encuentran en', userinfo ,'!!!!')
        print ('Los IDs faltantes han sido eliminados.')
        # Ahora si agrega todo al graph
        catalog['information']['table']['elements'] = userdict
        catalog['information']['table']['size'] = len(userdict) # Actualiza Size
        catalog['vertices']['table']['elements'] = relationshipsdict
        catalog['vertices']['table']['size'] = len(relationshipsdict) # Actualiza Size
        edges = sum(len(followed_list) for followed_list in relationshipsdict.values())
        catalog["edges"] = edges
        # Agregar arcos al grafo usando relationshipsdict

        
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
