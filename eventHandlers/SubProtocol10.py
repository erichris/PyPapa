import datetime
from dateutil import parser

def subProtocolHandler10(Config, package):
    if(package['SubProtocol'] == '0'): #Calif
        return calificar(Config, package)
    elif(package['SubProtocol'] == '1'): #Calif
        return favoritear(Config, package)
    
def calificar(Config, package):
    FONDA_ID = package['FONDA_ID']
    lista_columnas = ["CalifServicio", "CalifServicioVotos", "CalifLimpieza", "CalifLimpiezaVotos", "CalifComida", "CalifComidaVotos"]
    Califs = Config.Database.obtener_registro("DatosPersonales", lista_columnas, "DB_ID = " + str(FONDA_ID))[0]
    Config.Database.actualizar_registro("DatosPersonales", "CalifServicio = " + str(int(Califs[0]) + int(package['CALIF_SERVICIO'])), "DB_ID = %s" % str(FONDA_ID))
    Config.Database.actualizar_registro("DatosPersonales", "CalifServicioVotos = " + str(Califs[1] + 1), "DB_ID = %s" % str(FONDA_ID))
    Config.Database.actualizar_registro("DatosPersonales", "CalifLimpieza = " + str(int(Califs[2]) + int(package['CALIF_LIMPIEZA'])), "DB_ID = %s" % str(FONDA_ID))
    Config.Database.actualizar_registro("DatosPersonales", "CalifLimpiezaVotos = " + str(Califs[3] + 1), "DB_ID = %s" % str(FONDA_ID))
    Config.Database.actualizar_registro("DatosPersonales", "CalifComida = " + str(int(Califs[4]) + int(package['CALIF_COMIDA'])), "DB_ID = %s" % str(FONDA_ID))
    Config.Database.actualizar_registro("DatosPersonales", "CalifComidaVotos = " + str(Califs[5] + 1), "DB_ID = %s" % str(FONDA_ID))
    
    return {"Status": "0"
            }
    
def favoritear(Config, package):
    FONDA_ID = package['FONDA_ID']
    lista_columnas = ["CalifServicio", "CalifServicioVotos", "CalifLimpieza", "CalifLimpiezaVotos", "CalifComida", "CalifComidaVotos"]
    PID = package['PID']
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    
    lista_tupla = [["DB_ID", DB_ID], 
                   ["COCINA_ID", FONDA_ID]
                   ]
    Config.Database.insertar_datos("Favoritos", lista_tupla)
    
    return {"Status": "0"
            }











