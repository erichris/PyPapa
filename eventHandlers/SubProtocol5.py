import datetime


def subProtocolHandler5(Config, package):
    if(package['SubProtocol'] == '0'): #GetFavoritos
        return getFavoritos(Config, package)
    elif(package['SubProtocol'] == '1'): #NewFavoritos
        return updateNewFavoritos(Config, package)
    elif(package['SubProtocol'] == '2'): #DelateFavoritos
        return delateFavoritos(Config, package)
    elif(package['SubProtocol'] == '3'): #ObtenerInformacionFonda
        return getInfoFonda(Config, package)

def getInfoFonda(Config, package):
    DB_ID = package['FONDA_ID']
    Nombre = Config.Database.obtener_registro("DatosPersonales", ["NombreEmpresa"], "DB_ID = " + str(DB_ID))[0][0]
    Direccion = Config.Database.obtener_registro("DatosPersonales", ["Direccion"], "DB_ID = " + str(DB_ID))[0][0]
    return {"Status": "0", 
            "Pic": "",
            "Direccion": Direccion,
            "Nombre": Nombre
            }
    

def delateFavoritos(Config, package):
    PID = package['PID']
    Fonda_ID = package['FONDA_ID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    Config.Database.eliminar_registro("Favoritos", "DB_ID = %s AND COCINA_ID = %s" % (DB_ID, Fonda_ID))

    return {"Status": "0"
            }
    
    
def addFavorito(Config, package):
    PID = package['PID']
    Fonda_ID = package['FONDA_ID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    lista_tupla = [["DB_ID", DB_ID], 
                   ["COCINA_ID", Fonda_ID]
                   ]
    db.insertar_datos("Favoritos", lista_tupla)
    return {"Status": "0"
            }
    

def getFavoritos(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    Favoritos = Config.Database.obtener_registro("Favoritos", ["COCINA_ID"], "DB_ID = " + str(DB_ID))
    Fav = ""
    for x in range(0, len(Favoritos)):
        Fav += str(Favoritos[x][0]) + "|"
    if(Fav != ""):
        Fav = Fav[:-1]
    
    return {"Status": "0", 
            "Favoritos": Fav
            }
    














