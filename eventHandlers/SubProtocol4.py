import datetime


def subProtocolHandler4(Config, package):
    if(package['SubProtocol'] == '0'): #GetDatos
        return getData(Config, package)
    elif(package['SubProtocol'] == '1'): #SetDatos
        return updateData(Config, package)
    

def getData(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    Nombre = Config.Database.obtener_registro("DatosComensal", ["Nombre"], "DB_ID = " + str(DB_ID))[0][0]
    Correo = Config.Database.obtener_registro("DatosComensal", ["Correo"], "DB_ID = " + str(DB_ID))[0][0]
    return {"Status": "0", 
            "Nombre": str(Nombre),
            "Correo": str(Correo),
            }
    
def updateData(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    Config.Database.actualizar_registro("DatosComensal", "Nombre = '" + str(package['Nombre']) + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("DatosComensal", "Correo = '" + str(package['Correo'])+ "'", "DB_ID = %s" % str(DB_ID))
    return {"Status": "0"}












