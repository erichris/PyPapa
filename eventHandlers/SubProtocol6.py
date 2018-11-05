import datetime


def subProtocolHandler6(Config, package):
    if(package['SubProtocol'] == '0'): #GetApartados
        return getApartados(Config, package)
    elif(package['SubProtocol'] == '1'): #NewApartado
        return updateNewFavoritos(Config, package)
    elif(package['SubProtocol'] == '2'): #CancelarApartado
        return cancelarApartado(Config, package)
    elif(package['SubProtocol'] == '3'): #ObtenerInformacionApartado
        return getInfoApartado(Config, package)
    elif(package['SubProtocol'] == '4'): #ObtenerInformacionApartado
        return getInfoApartado(Config, package)

def getInfoApartado(Config, package):
    PEDIDO_ID = package['PEDIDO_ID']
    DB_ID = Config.Database.obtener_registro("Pedido", ["COMENSAL_ID"], "PEDIDO_ID = " + str(PEDIDO_ID))[0][0]
    Nombre = Config.Database.obtener_registro("DatosPersonales", ["NombreEmpresa"], "DB_ID = " + str(DB_ID))[0][0]
    Direccion = Config.Database.obtener_registro("DatosPersonales", ["Direccion"], "DB_ID = " + str(DB_ID))[0][0]
    Cancelado = Config.Database.obtener_registro("Pedido", ["Cancelado"], "PEDIDO_ID = " + str(PEDIDO_ID))[0][0]
    return {"Status": "0", 
            "Pic": "",
            "Direccion": Direccion,
            "Nombre": Nombre,
            "Cancelado": str(Cancelado)
            }
    

def cancelarApartado(Config, package):
    PID = package['PID']
    Fonda_ID = package['FONDA_ID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    Config.Database.eliminar_registro("Favoritos", "DB_ID = %s AND COCINA_ID = %s" % (DB_ID, Fonda_ID))

    return {"Status": "0"
            }

def getApartados(Config, package):
    print 0
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = " + str(PID))[0][0]
    Apartados = Config.Database.obtener_registro("Pedido", ["PEDIDO_ID", "NEGOCIO_ID", "HORA", "FECHA"], "COMENSAL_ID = " + str(DB_ID))
    print 1
    pedidoID = ""
    NegocioID = ""
    Hora = ""
    Dia = ""
    for x in range(0, len(Apartados)):
        pedidoID += str(Apartados[x][0]) + "|"
        NegocioID += str(Apartados[x][1]) + "|"
        Hora += str(Apartados[x][2].hour) + ":" + str(Apartados[x][2].minute) + "|"
        Dia += str(Apartados[x][3].day) + "/" + str(Apartados[x][3].month) + "/" + str(Apartados[x][3].year) + "|"
    print 2
    if(pedidoID != ""):
        pedidoID = pedidoID[:-1]
        NegocioID = NegocioID[:-1]
        Hora = Hora[:-1]
        Dia = Dia[:-1]
    print 3
    
    return {"Status": "0", 
            "Pedido_ID": pedidoID,
            "Negocio_ID": NegocioID,
            "Hora": Hora,
            "Dia": Dia
            }
    














