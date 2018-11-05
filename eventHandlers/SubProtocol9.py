import datetime
from dateutil import parser

def subProtocolHandler9(Config, package):
    if(package['SubProtocol'] == '0'): #RecibirPedidoComida
        return setPedidoComida(Config, package)
    elif(package['SubProtocol'] == '1'): #RecibirPedidoComida
        return setPedidoDesayuno(Config, package)
    elif(package['SubProtocol'] == '2'): #RecibirPedidoComida
        return getPedidosComida(Config, package)
    elif(package['SubProtocol'] == '3'): #RecibirPedidoComida
        return getPedidosDesayuno(Config, package)

def setPedidoComida(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    User = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    isDesayuno = True;
    if package['ES_DESAYUNO'] == "0":
        isDesayuno = False;
        
    lista_tupla = [["COMENSAL_ID", User],
                   ["NEGOCIO_ID", package['FONDA_ID']],
                   ["Plato1", "'%s'" % package['PLATO1']],
                   ["Plato2", "'%s'" % package['PLATO2']],
                   ["Plato3", "'%s'" % package['PLATO3']],
                   ["EsDesayuno", isDesayuno],
                   ["Entregado", False],
                   ["Cancelado", False],
                   ["Hora", "'%s'" % parser.parse(package['HORA'])],
                   ["Fecha", "'%s'" % datetime.date.today()]
                   ]
    Config.Database.insertar_datos("Pedido", lista_tupla)
    return {"Status": "0"
            }
    
def setPedidoDesayuno(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    User = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    isDesayuno = True;
    if package['ES_DESAYUNO'] == "0":
        isDesayuno = False;
        
    lista_tupla = [["COMENSAL_ID", User],
                   ["NEGOCIO_ID", package['FONDA_ID']],
                   ["Plato1", "'%s'" % package['PLATO1']],
                   ["Plato2", "'%s'" % package['PLATO2']],
                   ["Plato3", "'%s'" % package['PLATO3']],
                   ["EsDesayuno", isDesayuno],
                   ["Entregado", False],
                   ["Cancelado", False],
                   ["Hora", "'%s'" % parser.parse(package['HORA'])],
                   ["Fecha", "'%s'" % datetime.date.today()]
                   ]
    Config.Database.insertar_datos("Pedido", lista_tupla)
    return {"Status": "0"
            }

def getPedidosComida(Config, package):
    print 1
    PID = package['PID']
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    print 3
    lista_columnas = ["Plato1", "Plato2", "Plato3", "Entregado", "Cancelado", "Hora", "COMENSAL_ID"]
    Pedidos = Config.Database.obtener_registro("Pedido", lista_columnas, "NEGOCIO_ID = " + str(DB_ID) + " AND EsDesayuno = "  + str(False) + " AND Fecha = '"  + str(datetime.date.today()) + "'")
    print 2
    platos1 = ""
    platos2 = ""
    platos3 = ""
    Entregados = ""
    Cancelados = ""
    Horas = ""
    NombresComensales = ""
    CorreosComensales = ""
    print 4
    for pedido in Pedidos:
        print 5
        platos1 += str(pedido[0]) + "|"
        platos2 += str(pedido[1]) + "|"
        platos3 += str(pedido[2]) + "|"
        if pedido[3] == True:
            Entregados += str("1") + "|"
        else:
            Entregados += str("0") + "|"
        if pedido[4] == True:
            Cancelados += str("1") + "|"
        else:
            Cancelados += str("0") + "|"
        Horas += str(pedido[5]) + "|"
        comensal = Config.Database.obtener_registro("DatosComensal", ["Nombre", "Correo"], "DB_ID = " + str(pedido[6]))[0]
        NombresComensales += str(comensal[0]) + "|"
        CorreosComensales += str(comensal[1]) + "|"
    print 6
    if(len(Pedidos) > 0):
        platos1 = platos1[:-1]
        platos2 = platos2[:-1]
        platos3 = platos3[:-1]
        Entregados = Entregados[:-1]
        Cancelados = Cancelados[:-1]
        Horas = Horas[:-1]
        NombresComensales = NombresComensales[:-1]
        CorreosComensales = CorreosComensales[:-1]
    print 7
    return {"Status": "0",
            "Plato1": platos1,
            "Plato2": platos2,
            "Plato3": platos3,
            "Entregado": Entregados,
            "Cancelado": Cancelados,
            "Hora": Horas,
            "NombreComensal": NombresComensales,
            "CorreoComensal": CorreosComensales
            }

def getPedidosDesayuno(Config, package):
    PID = package['PID']
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    lista_columnas = ["Plato1", "Plato2", "Plato3", "Entregado", "Cancelado", "Hora", "COMENSAL_ID"]
    Pedidos = Config.Database.obtener_registro("Pedido", lista_columnas, "NEGOCIO_ID = " + str(DB_ID) + " AND EsDesayuno = "  + str(True) + " AND Fecha = '"  + str(datetime.date.today()) + "'")
    platos1 = ""
    platos2 = ""
    platos3 = ""
    Entregados = ""
    Cancelados = ""
    Horas = ""
    NombresComensales = ""
    CorreosComensales = ""
    for pedido in Pedidos:
        print pedido
        print 0
        platos1 += str(pedido[0]) + "|"
        platos2 += str(pedido[1]) + "|"
        platos3 += str(pedido[2]) + "|"
        print 1
        if pedido[3] == True:
            Entregados += str("1") + "|"
        else:
            Entregados += str("0") + "|"
        print 2
        if pedido[4] == True:
            Cancelados += str("1") + "|"
        else:
            Cancelados += str("0") + "|"
        print 3
        Horas += str(pedido[5]) + "|"
        print 4
        comensal = Config.Database.obtener_registro("DatosComensal", ["Nombre", "Correo"], "DB_ID = " + str(pedido[6]))[0]
        print 5
        NombresComensales += str(comensal[0]) + "|"
        print 6
        CorreosComensales += str(comensal[1]) + "|"
    if(len(Pedidos) > 0):
        platos1 = platos1[:-1]
        platos2 = platos2[:-1]
        platos3 = platos3[:-1]
        Entregados = Entregados[:-1]
        Cancelados = Cancelados[:-1]
        Horas = Horas[:-1]
        NombresComensales = NombresComensales[:-1]
        CorreosComensales = CorreosComensales[:-1]
    return {"Status": "0",
            "Plato1": platos1,
            "Plato2": platos2,
            "Plato3": platos3,
            "Entregado": Entregados,
            "Cancelado": Cancelados,
            "Hora": Horas,
            "NombreComensal": NombresComensales,
            "CorreoComensal": CorreosComensales
            }

def updateData(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    Config.Database.actualizar_registro("DatosComensal", "Nombre = '" + str(package['Nombre']) + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("DatosComensal", "Correo = '" + str(package['Correo'])+ "'", "DB_ID = %s" % str(DB_ID))
    return {"Status": "0"}












