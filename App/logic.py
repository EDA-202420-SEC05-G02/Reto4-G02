import time
from DataStructures.Graph import adj_list_graph as adj
import csv
from collections import deque


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
            usuarios += 1

         # Ahora si agrega todo al graph
        catalog['information']['table']['elements'] = userdict
        catalog['information']['table']['size'] = len(userdict) # Actualiza Size
        catalog['vertices']['table']['elements'] = relationshipsdict
        catalog['vertices']['table']['size'] = len(relationshipsdict) # Actualiza Size
        edges = sum(len(followed_list) for followed_list in relationshipsdict.values())
        catalog["edges"] = edges
        # Agregar arcos al grafo usando relationshipsdict

        
        return catalog
            
#Funcions auxiliares para load_data en view :3
def auxiliaresload(catalog):
    basicos = 0
    premium = 0
    #Crea un nuevo dict para verificar la cantidad de usuarios premium y basic, y para verificar la ciudad mas famosa
    #Usaria un BFS pero no necesito saber nada de conexiones ni vertices     
    userdict = catalog['information']['table']['elements']  
    cities = [user_data['CITY'] for user_data in userdict.values()]  
    for usuario in userdict:
        if userdict[usuario]['USER_TYPE'] == 'basic':
            basicos +=1
        else:
            premium +=1  
    #Se crea otro dict para verificar        
    city_count = {}
    for user_data in userdict.values():
        city = user_data['CITY']
        if city != ' Unknown':
            if city not in city_count:
                city_count[city] = 0
            city_count[city] += 1    
    most_common_city = max(city_count, key=city_count.get)
    
    return basicos,premium,most_common_city, city_count[most_common_city]
        
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass

def req_1(catalog, start_id, end_id):
    """
    Encuentra el camino más corto entre dos usuarios en el grafo.
    """
    start_time = time.time()

    vertices = catalog["vertices"]["table"]["elements"]
    user_data = catalog["information"]["table"]["elements"]
    
    if start_id not in vertices or end_id not in vertices:
        return {
            "time": time.time() - start_time,
            "message": "Uno o ambos usuarios no existen en el grafo.",
            "path_details": None
        }

    visited = set()
    queue = deque([[start_id]])
    path = []

    while queue:
        current_path = queue.popleft()
        current_node = current_path[-1]

        if current_node == end_id:
            path = current_path
            break

        if current_node not in visited:
            visited.add(current_node)
            neighbors = vertices.get(current_node, [])
            for neighbor in neighbors:
                new_path = list(current_path)
                new_path.append(neighbor)
                queue.append(new_path)

    execution_time = time.time() - start_time
    if path:
        path_details = []
        for node in path:
            user_info = user_data.get(node, {})
            path_details.append({
                "id": node,
                "alias": user_info.get("USER_NAME", "Unknown"),
                "user_type": user_info.get("USER_TYPE", "Unknown"),
                "city": user_info.get("CITY", "Unknown"),
                "hobbies": user_info.get("HOBBIES", "Unknown"),
            })

        return {
            "time": execution_time,
            "people_in_path": len(path) - 1,
            "path_details": path_details,
        }
    else:
        return {
            "time": execution_time,
            "message": "No se encontró un camino entre los usuarios.",
            "path_details": None
        }


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog,start_id):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = time.time()
    
    vertices = catalog["vertices"]["table"]["elements"]
    if start_id not in vertices:
        return {
            "time": time.time() - start_time,
            "message": f"El usuario con ID {start_id} no existe en el grafo.",
            "popular_friend": None,
            "followers_count": 0,
        }
    
    friends = vertices.get(start_id, [])
    if not friends:
        return {
            "time": time.time() - start_time,
            "message": f"El usuario con ID {start_id} no tiene amigos (seguidores).",
            "popular_friend": None,
            "followers_count": 0,
        }
    
    max_followers = -1
    popular_friend = None
    for friend_id in friends:
        follower_count = len(vertices.get(friend_id, []))
        if follower_count > max_followers:
            max_followers = follower_count
            popular_friend = friend_id
    
    execution_time = time.time() - start_time
    return {
        "time": execution_time,
        "popular_friend": popular_friend,
        "followers_count": max_followers,
    }



def req_4(catalog,cuentaA, cuentaB):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = time.time()
    relationshipgraph = catalog['vertices']['table']['elements']  
    usergaph = catalog['information']['table']['elements']  
    listado = {}
    Afriends = relationshipgraph[cuentaA] 
    Bfriends = relationshipgraph[cuentaB] 
    for amigo in Afriends:
        #Verificar si son amigos
        if cuentaA in relationshipgraph[amigo]:
            if amigo in Bfriends:
                listado[amigo] = {"Username": usergaph[amigo]['USER_NAME'], "Tipo" : usergaph[amigo]["USER_TYPE"]} 
            
    execution_time = time.time() - start_time    
    execution_time = "Tiempo de ejecucion: " + str(execution_time)+" s"
    if listado == {}:
        listado = 'No hay amigos en comun.'
    return execution_time, listado


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, N):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = time.time()
    
    if N < 2:
        return {
            "time": time.time() - start_time,
            "message": "N debe ser mayor o igual a 2.",
            "popular_users": [],
            "tree": None,
        }
    
    vertices = catalog["vertices"]["table"]["elements"]
    
    user_followers_count = {}
    for user_id, followed_users in vertices.items():
        user_followers_count[user_id] = len(followed_users)
    
    sorted_users = sorted(user_followers_count.items(), key=lambda x: x[1], reverse=True)
    popular_users = sorted_users[:N]
    popular_user_ids = [user[0] for user in popular_users]
    popular_user_info = []

    for user_id in popular_user_ids:
        user_data = catalog['information']['table']['elements'].get(user_id, {})
        user_name = user_data.get('USER_NAME', 'Unknown')
        popular_user_info.append({'ID': user_id, 'Name': user_name, 'Followers': user_followers_count[user_id]})
    
    tree = None
    connected = check_if_tree_exists(catalog, popular_user_ids)
    execution_time = time.time() - start_time
    
    return {
        "time": execution_time,
        "popular_users": popular_user_info,
        "tree": connected,
    }

def check_if_tree_exists(catalog, user_ids):
    visited = set()
    queue = deque([user_ids[0]])
    
    while queue:
        current_user = queue.popleft()
        if current_user in visited:
            continue
        visited.add(current_user)
        friends = catalog["vertices"]["table"]["elements"].get(current_user, [])
        
        for friend in friends:
            if friend in user_ids and friend not in visited:
                queue.append(friend)

    return all(user_id in visited for user_id in user_ids)


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
