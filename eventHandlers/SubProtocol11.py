import datetime
from dateutil import parser

def subProtocolHandler11(Config, package):
    print 0
    if(package['SubProtocol'] == '0'): #Calif
        return uploadImage(Config, package)
    elif(package['SubProtocol'] == '1'): #Calif
        return getImageFonda(Config, package)
    elif(package['SubProtocol'] == '2'): #Calif
        return getImageUser(Config, package)
    
def uploadImage(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    
    if package['IMAGEUPLOADED'] == "PROFILE":
        Config.Database.actualizar_registro("Images", "HASPROFILE = " + str(True), "DB_ID = %s" % str(DB_ID))
        Config.Database.actualizar_registro("Images", "PROFILEPIC = '" + str(package['IMAGE']) + "'", "DB_ID = %s" % str(DB_ID))
    elif package['IMAGEUPLOADED'] == "BACKGROUND":
        Config.Database.actualizar_registro("Images", "HASBACKGROUND = " + str(True), "DB_ID = %s" % str(DB_ID))
        Config.Database.actualizar_registro("Images", "BACKGROUNDPIC = '" + str(package['IMAGE']) + "'", "DB_ID = %s" % str(DB_ID))
    
    return {"Status": "0"}
    
def getImageFonda(Config, package):
    PID = package['PID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = " + str(PID))[0][0]
    if package['IMAGEREQUIRED'] == "PROFILE":
        if Config.Database.obtener_registro("Images", ["HASPROFILE"], "DB_ID = " + str(DB_ID))[0][0] == True:
            img = Config.Database.obtener_registro("Images", ["PROFILEPIC"], "DB_ID = " + str(DB_ID))[0][0]
            return {"Status": "0", "Image": img}
        else:
            return {"Status": "1", "Image": ""}
    elif package['IMAGEREQUIRED'] == "BACKGROUND":
        if Config.Database.obtener_registro("Images", ["HASBACKGROUND"], "DB_ID = " + str(DB_ID))[0][0] == True:
            img = Config.Database.obtener_registro("Images", ["BACKGROUNDPIC"], "DB_ID = " + str(DB_ID))[0][0]
            return {"Status": "0", "Image": img}
        else:
            return {"Status": "1", "Image": ""}
    else:
        return {"Status": "1"}


def getImageUser(Config, package):
    FONDA_ID = package['FONDA_ID']
    if package['IMAGEREQUIRED'] == "PROFILE":
        if Config.Database.obtener_registro("Images", ["HASPROFILE"], "DB_ID = " + str(FONDA_ID))[0][0] == True:
            img = Config.Database.obtener_registro("Images", ["PROFILEPIC"], "DB_ID = " + str(FONDA_ID))[0][0]
            return {"Status": "0", "Image": img}
        else:
            return {"Status": "1", "Image": ""}
    elif package['IMAGEREQUIRED'] == "BACKGROUND":
        if Config.Database.obtener_registro("Images", ["HASBACKGROUND"], "DB_ID = " + str(FONDA_ID))[0][0] == True:
            img = Config.Database.obtener_registro("Images", ["BACKGROUNDPIC"], "DB_ID = " + str(FONDA_ID))[0][0]
            return {"Status": "0", "Image": img}
        else:
            return {"Status": "1", "Image": ""}
    else:
        return {"Status": "1"}







