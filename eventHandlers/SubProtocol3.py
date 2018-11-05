import datetime
from dateutil import parser

def subProtocolHandler3(Config, package):
    if(package['SubProtocol'] == '0'): #ChecarDesayuno
        return checkMenu(Config, package)
    elif(package['SubProtocol'] == '1'): #UpdateDesayuno
        return updateMenu(Config, package)
    
def checkMenu(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    Platillos = Config.Database.obtener_registro("Desayunos", ["Platillos"], "DB_ID = " + str(DB_ID))[0][0]
    PlatillosPrecio = Config.Database.obtener_registro("Desayunos", ["PlatillosPrecio"], "DB_ID = " + str(DB_ID))[0][0]
    Extras = Config.Database.obtener_registro("Desayunos", ["Extras"], "DB_ID = " + str(DB_ID))[0][0]
    ExtrasPrecio = Config.Database.obtener_registro("Desayunos", ["ExtrasPrecio"], "DB_ID = " + str(DB_ID))[0][0]
    Inlcuye = Config.Database.obtener_registro("Desayunos", ["Incluye"], "DB_ID = " + str(DB_ID))[0][0]
    IncluyeBool = Config.Database.obtener_registro("Desayunos", ["IncluyeBool"], "DB_ID = " + str(DB_ID))[0][0]
    HoraApertura = Config.Database.obtener_registro("Desayunos", ["HoraApertura"], "DB_ID = " + str(DB_ID))[0][0]
    HoraCierre = Config.Database.obtener_registro("Desayunos", ["HoraCierre"], "DB_ID = " + str(DB_ID))[0][0]
    packageReturn = {"Status": "0",
            "Platillos" : Platillos,
            "PlatillosPrecio" : PlatillosPrecio,
            "Extras" : Extras,
            "ExtrasPrecio" : ExtrasPrecio,
            "Inlcuye" : Inlcuye,
            "IncluyeBool" : IncluyeBool,
            "HoraApertura" : str(HoraApertura.hour) + ":" + str(HoraApertura.minute),
            "HoraCierre" : str(HoraCierre.hour) + ":" + str(HoraCierre.minute)
            }
    return packageReturn

def updateMenu(Config, package):
    print 0
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    print 1
    Platillos = package['Platillos'][:-1]
    PlatillosPrecio = package['PlatillosPrice'][:-1]
    Extras = package['Extras'][:-1]
    ExtrasPrecio = package['ExtrasPrice'][:-1]
    Inlcuye = package['Incluye'][:-1]
    IncluyeBool = package['IncluyeBool'][:-1]
    HoraApertura = package['HoraApertura']
    HoraCierre = package['HoraCierre']
    Config.Database.actualizar_registro("Desayunos", "Platillos = '" + Platillos + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Desayunos", "PlatillosPrecio = '" + PlatillosPrecio + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Desayunos", "Extras = '" + Extras + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Desayunos", "ExtrasPrecio = '" + ExtrasPrecio + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Desayunos", "Incluye = '" + Inlcuye + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Desayunos", "IncluyeBool = '" + IncluyeBool + "'", "DB_ID = %s" % str(DB_ID))

    Config.Database.actualizar_registro("Desayunos", "HoraApertura = '%s'" % parser.parse(HoraApertura), "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("Desayunos", "HoraCierre = '%s'" % parser.parse(HoraCierre), "DB_ID = %s" % str(DB_ID))

    
    packageReturn = {"Status": "0"}
    return packageReturn











