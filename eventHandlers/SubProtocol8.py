import datetime


def subProtocolHandler8(Config, package):
    if(package['SubProtocol'] == '0'): #GEtFondasMap
        return GetFondasMap(Config, package)


def GetFondasMap(Config, package):
    print 1
    Lat = float(package['Latitud'])
    Lon = float(package['Longitud'])
    
    print 2
    lista_columnas = ["DB_ID"]
    ratio = 5
    cuestion = "Latitud < " + str(Lat + ratio) + " AND Latitud > " + str(Lat - ratio) + " AND Longitud < " + str(Lon + ratio) + " AND Longitud > " + str(Lon - ratio)
    
    print 3
    fondas = Config.Database.obtener_registro("DatosPersonales", ["DB_ID"], cuestion)
    
    packageReturn = {"Status": "0",
            "IDs" : "",
            "Nombres" : "",
            "Direcciones" : "",
            "Efectivos" : "",
            "Tarjetas" : "",
            "Puntuaciones" : "",
            "Coordenadas" : ""
            }
    
    print fondas
    
    for fonda in fondas:
        print "z"
        id_fonda = fonda[0]
        print "t"
        dataFonda = Config.Database.obtener_registro("DatosPersonales", ["NombreEmpresa", "Direccion", "Latitud", "Longitud", "CalifComida", "CalifComidaVotos", "AceptaEfectivo", "AceptaTarjeta"], "DB_ID = " + str(id_fonda))[0]
        print id_fonda
        packageReturn["IDs"] += str(id_fonda) + "|";
        packageReturn["Nombres"] += str(dataFonda[0]) + "|"
        packageReturn["Direcciones"] += str(dataFonda[1]) + "|"
        print "e"
        if(dataFonda[6]):
            packageReturn["Efectivos"] += "1" + "|"
        else:
            packageReturn["Efectivos"] += "0" + "|"
            
        if(dataFonda[7]):
            packageReturn["Tarjetas"] += "1" + "|"
        else:
            packageReturn["Tarjetas"] += "0" + "|"
        print "w"
        if(dataFonda[5] == 0):
            packageReturn["Puntuaciones"] += "0" + "|"
        else:
            packageReturn["Puntuaciones"] += str(int(dataFonda[4] / dataFonda[5])) + "|"
        print "q"
        packageReturn["Coordenadas"] += str(str(dataFonda[2]) + "^ " + str(dataFonda[3])) + "|"
    
    print 5
    if len(fondas) > 0:
        print 5.5
        packageReturn["IDs"] = packageReturn["IDs"][:-1]
        packageReturn["Nombres"] = packageReturn["Nombres"][:-1]
        packageReturn["Direcciones"] = packageReturn["Direcciones"][:-1]
        packageReturn["Efectivos"] = packageReturn["Efectivos"][:-1]
        packageReturn["Tarjetas"] = packageReturn["Tarjetas"][:-1]
        packageReturn["Puntuaciones"] = packageReturn["Puntuaciones"][:-1]
        packageReturn["Coordenadas"] = packageReturn["Coordenadas"][:-1]
    print 6
    
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











