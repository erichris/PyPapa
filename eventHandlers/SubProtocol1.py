import datetime


def subProtocolHandler1(Config, package):
    if(package['SubProtocol'] == '0'): #CargarDatos
        print "Cargar Datos"
        return getData(Config, package)
    elif(package['SubProtocol'] == '1'): #UpdateDatos
        return updateData(Config, package)
    
def getData(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    NombreEmpresa = Config.Database.obtener_registro("DatosPersonales", ["NombreEmpresa"], "DB_ID = " + str(DB_ID))[0][0]
    NombreUser = Config.Database.obtener_registro("DatosPersonales", ["NombreUsuario"], "DB_ID = " + str(DB_ID))[0][0]
    Direccion = Config.Database.obtener_registro("DatosPersonales", ["Direccion"], "DB_ID = " + str(DB_ID))[0][0]
    Correo = Config.Database.obtener_registro("DatosPersonales", ["Correo"], "DB_ID = " + str(DB_ID))[0][0]
    AceptarEfectivo = Config.Database.obtener_registro("DatosPersonales", ["AceptaEfectivo"], "DB_ID = " + str(DB_ID))[0][0]
    AceptarTarjeta = Config.Database.obtener_registro("DatosPersonales", ["AceptaTarjeta"], "DB_ID = " + str(DB_ID))[0][0]
    OfreceDesayuno = Config.Database.obtener_registro("DatosPersonales", ["OfreceDesayuno"], "DB_ID = " + str(DB_ID))[0][0]
    OfreceComida = Config.Database.obtener_registro("DatosPersonales", ["OfreceComida"], "DB_ID = " + str(DB_ID))[0][0]
    CalifServicio = Config.Database.obtener_registro("DatosPersonales", ["CalifServicio"], "DB_ID = " + str(DB_ID))[0][0]
    CalifLimpieza = Config.Database.obtener_registro("DatosPersonales", ["CalifLimpieza"], "DB_ID = " + str(DB_ID))[0][0]
    CalifComida = Config.Database.obtener_registro("DatosPersonales", ["CalifComida"], "DB_ID = " + str(DB_ID))[0][0]
    if(int(CalifServicio) > 0):
        CalifServicio = int(CalifServicio) / int(Config.Database.obtener_registro("DatosPersonales", ["CalifServicioVotos"], "DB_ID = " + str(DB_ID))[0][0])
    if(int(CalifLimpieza) > 0):
        CalifLimpieza = int(CalifLimpieza) / int(Config.Database.obtener_registro("DatosPersonales", ["CalifLimpiezaVotos"], "DB_ID = " + str(DB_ID))[0][0])
    if(int(CalifComida) > 0):
        CalifComida = int(CalifComida) / int(Config.Database.obtener_registro("DatosPersonales", ["CalifComidaVotos"], "DB_ID = " + str(DB_ID))[0][0])
    return {"Status": "0", 
            "NombreEmpresa": str(NombreEmpresa),
            "NombreUser": str(NombreUser),
            "Direccion": str(Direccion),
            "Correo": str(Correo),
            "CalifServicio": str(CalifServicio),
            "CalifLimpieza": str(CalifLimpieza),
            "CalifComida": str(CalifComida),
            "AceptarEfectivo": str(AceptarEfectivo),
            "AceptarTarjeta": str(AceptarTarjeta),
            "OfreceDesayuno": str(OfreceDesayuno),
            "OfreceComida": str(OfreceComida)
            }
    
def updateData(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    Config.Database.actualizar_registro("DatosPersonales", "NombreEmpresa = '" + str(package['nombreEmpresa']) + "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("DatosPersonales", "NombreUsuario = '" + str(package['nombreUser'])+ "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("DatosPersonales", "Direccion = '" + str(package['Direccion'])+ "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("DatosPersonales", "Correo = '" + str(package['Correo'])+ "'", "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("DatosPersonales", "Latitud = " + str(package['Latitud']), "DB_ID = %s" % str(DB_ID))
    Config.Database.actualizar_registro("DatosPersonales", "Longitud = " + str(package['Longitud']), "DB_ID = %s" % str(DB_ID))
    if(package["aceptaEfectivo"] == "True"):
        Config.Database.actualizar_registro("DatosPersonales", "AceptaEfectivo = " + str(True), "DB_ID = %s" % str(DB_ID))
    else:
        Config.Database.actualizar_registro("DatosPersonales", "AceptaEfectivo = " + str(False), "DB_ID = %s" % str(DB_ID))
    
    if(package["aceptaTarjeta"] == "True"):
        Config.Database.actualizar_registro("DatosPersonales", "AceptaTarjeta = " + str(True), "DB_ID = %s" % str(DB_ID))
    else:
        Config.Database.actualizar_registro("DatosPersonales", "AceptaTarjeta = " + str(False), "DB_ID = %s" % str(DB_ID))
    if(package["ofreceDesayuno"] == "True"):
        Config.Database.actualizar_registro("DatosPersonales", "OfreceDesayuno = " + str(True), "DB_ID = %s" % str(DB_ID))
    else:
        Config.Database.actualizar_registro("DatosPersonales", "OfreceDesayuno = " + str(False), "DB_ID = %s" % str(DB_ID))
    if(package["ofreceComida"] == "True"):
        Config.Database.actualizar_registro("DatosPersonales", "OfreceComida = " + str(True), "DB_ID = %s" % str(DB_ID))
    else:
        Config.Database.actualizar_registro("DatosPersonales", "OfreceComida = " + str(False), "DB_ID = %s" % str(DB_ID))
    
    
    return {"Status": "0"}












