import datetime


def subProtocolHandler7(Config, package):
    if(package['SubProtocol'] == '0'): #GetApartados
        return checkMenuDesayuno(Config, package)
    elif(package['SubProtocol'] == '1'): #GetApartados
        return checkMenuComida(Config, package)


def checkMenuDesayuno(Config, package):
    DB_ID = package['ID_NEGOCIO']
    lista_columnas = ["DB_ID"]
    #DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
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

def checkMenuComida(Config, package):
    DB_ID = package['ID_NEGOCIO']
    lista_columnas = ["DB_ID"]
    #DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
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











