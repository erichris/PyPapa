import datetime
from dateutil import parser

def subProtocolHandler2(Config, package):
    if(package['SubProtocol'] == '0'): #ChecarComida
        return checkMenu(Config, package)
    elif(package['SubProtocol'] == '1'): #UpdateComida
        return updateMenu(Config, package)
    
def checkMenu(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    Entradas = Config.Database.obtener_registro("Comidas", ["Entrada"], "DB_ID = " + str(DB_ID))[0][0]
    PlatoFuerte = Config.Database.obtener_registro("Comidas", ["PlatoFuerte"], "DB_ID = " + str(DB_ID))[0][0]
    PlatoFuertePrecio = Config.Database.obtener_registro("Comidas", ["PlatoFuertePrecio"], "DB_ID = " + str(DB_ID))[0][0]
    Guarnicion = Config.Database.obtener_registro("Comidas", ["Guarnicion"], "DB_ID = " + str(DB_ID))[0][0]
    CantidadGuarniciones = Config.Database.obtener_registro("Comidas", ["CantidadGuarniciones"], "DB_ID = " + str(DB_ID))[0][0]
    Inlcuye = Config.Database.obtener_registro("Comidas", ["Incluye"], "DB_ID = " + str(DB_ID))[0][0]
    IncluyeBool = Config.Database.obtener_registro("Comidas", ["IncluyeBool"], "DB_ID = " + str(DB_ID))[0][0]
    HoraApertura = Config.Database.obtener_registro("Comidas", ["HoraApertura"], "DB_ID = " + str(DB_ID))[0][0]
    HoraCierre = Config.Database.obtener_registro("Comidas", ["HoraCierre"], "DB_ID = " + str(DB_ID))[0][0]
    packageReturn = {"Status": "0",
            "Entradas" : Entradas,
            "PlatoFuerte" : PlatoFuerte,
            "PlatoFuertePrecio" : PlatoFuertePrecio,
            "Guarnicion" : Guarnicion,
            "CantidadGuarniciones" : str(CantidadGuarniciones),
            "Inlcuye" : Inlcuye,
            "IncluyeBool" : IncluyeBool,
            "HoraApertura" : str(HoraApertura.hour) + ":" + str(HoraApertura.minute),
            "HoraCierre" : str(HoraCierre.hour) + ":" + str(HoraCierre.minute)
            }
    print packageReturn
    return packageReturn
    
def updateMenu(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    Entrada = package['Entrada'][:-1]
    PlatoFuerte = package['PlatoFuerte'][:-1]
    PlatoFuertePrecio = package['PlatoFuertePrecio'][:-1]
    Guarnicion = package['Guarnicion'][:-1]
    CantidadGuarniciones = package['CantidadGuarniciones']
    Incluye_1 = package['Incluye'][:-1]
    IncluyeBool = package['IncluyeBool'][:-1]
    HoraApertura = package['HoraApertura']
    HoraCierre = package['HoraCierre']
    
    Config.Database.actualizar_registro("Comidas", "Entrada = '" + Entrada + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Comidas", "PlatoFuerte = '" + PlatoFuerte + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Comidas", "PlatoFuertePrecio = '" + PlatoFuertePrecio + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Comidas", "Guarnicion = '" + Guarnicion + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Comidas", "Incluye = '" + Incluye_1 + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Comidas", "IncluyeBool = '" + IncluyeBool + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Comidas", "CantidadGuarniciones = " +CantidadGuarniciones, "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Comidas", "HoraApertura = '%s'" % parser.parse(HoraApertura), "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Comidas", "HoraCierre = '%s'" % parser.parse(HoraCierre), "DB_ID = %s" % str(DB_ID))
    
    packageReturn = {"Status": "0"}
    return packageReturn












