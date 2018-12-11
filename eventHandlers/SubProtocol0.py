import datetime
import random
from dateutil import parser
import hashlib
import binascii

def subProtocolHandler0(Config, package):
    if(package['SubProtocol'] == '0'): #Login/Register Fonda
        return login(Config, package)
    elif(package['SubProtocol'] == '1'): #Login/Register Comensal
        return loginComensal(Config, package)
    elif(package['SubProtocol'] == '2'): #Login/Register NewFonda
        return newLogin(Config, package)
    
def login(Config, package):
    #Verificar si existe
    ClientID = package['ClientID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", lista_columnas, "ClientID = '" + str(ClientID) + "'")
    #Logear
    if(len(DB_ID) > 0):
        PID = 0;
        while(True):
            PID = random.randint(0,1000000);
            lista_columnas = ["DB_ID"]
            if(len(Config.Database.obtener_registro("Users", lista_columnas, "PID = " + str(PID))) == 0):
                break;
        Config.Database.actualizar_registro("Users", "PID = " + str(PID), "DB_ID = %s" % str(DB_ID[0][0]))
        print PID
        return {"Status": "0", "PID": str(PID)}
    #Registrar
    if(len(DB_ID) == 0):
        PID = 0;
        while(True):
            PID = random.randint(0,1000000);
            lista_columnas = ["DB_ID"]
            if(len(Config.Database.obtener_registro("Users", lista_columnas, "PID = " + str(PID))) == 0):
                break;
        lista_tupla = [["PID", str(PID)], ["ClientID", "'" + ClientID + "'"]]
        Config.Database.insertar_datos("Users", lista_tupla)
        DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = %i" % PID)[0][0]
        lista_tupla = [["DB_ID", DB_ID], 
                       ["NombreEmpresa", "'SIN NOMBRE'"], 
                       ["NombreUsuario", "'SIN NOMBRE'"],
                       ["Direccion", "'SIN DIRECCION'"],
                       ["Correo", "'SIN CORREO'"],
                       ["CalifServicio", "'0'"],
                       ["CalifLimpieza", "'0'"],
                       ["CalifComida", "'0'"],
                       ["Longitud", 0],
                       ["Latitud", 0],
                       ["CalifServicioVotos", "'0'"],
                       ["CalifLimpiezaVotos", "'0'"],
                       ["CalifComidaVotos", "'0'"],
                       ["AceptaEfectivo", False],
                       ["AceptaTarjeta", False],
                       ["OfreceDesayuno", False],
                       ["OfreceComida", False],
                       ]
        Config.Database.insertar_datos("DatosPersonales", lista_tupla)
        lista_tupla = [["DB_ID", DB_ID],
                   ["PROFILEPIC", "'N'"],
                   ["BACKGROUNDPIC", "'N'"],
                   ["HASPROFILE", False],
                   ["HASBACKGROUND", False]
                   ]
        Config.Database.insertar_datos("Images", lista_tupla)
        lista_tupla = [["DB_ID", DB_ID], 
                       ["Platillos", "'Chilaquiles|Enchiladas'"],
                       ["PlatillosPrecio", "'35|40'"],
                       ["Extras", "'Extra1|Extra2'"],
                       ["ExtrasPrecio", "'5|10'"],
                       ["Incluye", "'Fruta|Cafe de olla|Te o jugo'"],
                       ["IncluyeBool", "'0|0|0'"],
                       ["HoraApertura", "'%s'" % datetime.time(8,0,0)],
                       ["HoraCierre", "'%s'" % datetime.time(12,0,0)]
                       ]
        Config.Database.insertar_datos("Desayunos", lista_tupla)
        lista_tupla = [["DB_ID", DB_ID], 
                       ["Entrada", "'Consome|Crema de zanahoria'"],
                       ["PlatoFuerte", "'Pechuga de pollo|Enfrijoladas'"],
                       ["PlatoFuertePrecio", "'50|45'"],
                       ["Guarnicion", "'Arroz|Frijoles|Spagethi'"],
                       ["CantidadGuarniciones", 2],
                       ["Incluye", "'Agua|Tortillas|Postre'"],
                       ["IncluyeBool", "'0|0|0'"],
                       ["HoraApertura", "'%s'" % datetime.time(13,0,0)],
                       ["HoraCierre", "'%s'" % datetime.time(18,0,0)]
                       ]
        Config.Database.insertar_datos("Comidas", lista_tupla)
        return {"Status": "0", "PID": str(PID)}



def loginComensal(Config, package):
    #Verificar si existe
    ClientID = package['ClientID']
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Comensales", lista_columnas, "ClientID = '" + str(ClientID) + "'")
    #Logear
    if(len(DB_ID) > 0):
        PID = 0;
        while(True):
            PID = random.randint(0,1000000);
            lista_columnas = ["DB_ID"]
            if(len(Config.Database.obtener_registro("Comensales", lista_columnas, "PID = " + str(PID))) == 0):
                break;
        Config.Database.actualizar_registro("Comensales", "PID = " + str(PID), "DB_ID = %s" % str(DB_ID[0][0]))
        return {"Status": "0", "PID": str(PID)}
    #Registrar
    if(len(DB_ID) == 0):
        PID = 0;
        while(True):
            PID = random.randint(0,1000000);
            lista_columnas = ["DB_ID"]
            if(len(Config.Database.obtener_registro("Comensales", lista_columnas, "PID = " + str(PID))) == 0):
                break;
        lista_tupla = [["PID", str(PID)], ["ClientID", "'" + str(ClientID) + "'"]]
        Config.Database.insertar_datos("Comensales", lista_tupla)
        DB_ID = Config.Database.obtener_registro("Comensales", ["DB_ID"], "PID = %i" % PID)[0][0]
        lista_tupla = [["DB_ID", DB_ID], 
                   ["Nombre", "'Sin nombre'"],
                   ["Correo", "'Sin correo'"]
                   ]
        Config.Database.insertar_datos("DatosComensal", lista_tupla)
        
        return {"Status": "0", "PID": str(PID)}
    
    


def newLogin(Config, package):
    #Verificar si existe
    User = package['Username']
    Pass = package['Pass']
    Pass = force_bytes(Pass)
    lista_columnas = ["password"]
    print 1
    stored_pass = Config.Database.obtener_registro("auth_user", lista_columnas, "username = '" + str(User) + "'")
    print 2
    if(len(stored_pass) == 0):
        return {"Status": "1"}
    print 3
    b = stored_pass[0][0].split('$')
    print 4
    salt = str(b[2])
    print 5
    iterations = str(b[1])
    encrypt = str(b[0])
    salt = force_bytes(salt)
    #iterations = 100000
    enconde = 'SHA256'
    print 6
    Pass = hashlib.pbkdf2_hmac(enconde, Pass, salt, int(iterations))
    Pass = binascii.b2a_base64(Pass)
    print 7
    Pass = encrypt + "$" + iterations + "$" + salt + "$" + Pass
    Pass = Pass.replace('\n', '')
    print 8
    lista_columnas = ["id"]
    id_username = Config.Database.obtener_registro("auth_user", lista_columnas, "username = '" + str(User) + "'" + " AND " + "password = '" + str(Pass) + "'")
    if(len(id_username) == 0):
        return {"Status": "1"}
    
    
    ClientID = User
    lista_columnas = ["DB_ID"]
    DB_ID = Config.Database.obtener_registro("Users", lista_columnas, "ClientID = '" + str(ClientID) + "'")
    #Logear
    if(len(DB_ID) > 0):
        PID = 0;
        while(True):
            PID = random.randint(0,1000000);
            lista_columnas = ["DB_ID"]
            if(len(Config.Database.obtener_registro("Users", lista_columnas, "PID = " + str(PID))) == 0):
                break;
        Config.Database.actualizar_registro("Users", "PID = " + str(PID), "DB_ID = %s" % str(DB_ID[0][0]))
        return {"Status": "0", "PID": str(PID)}
    #Registrar
    if(len(DB_ID) == 0):
        PID = 0;
        while(True):
            PID = random.randint(0,1000000);
            lista_columnas = ["DB_ID"]
            if(len(Config.Database.obtener_registro("Users", lista_columnas, "PID = " + str(PID))) == 0):
                break;
        lista_tupla = [["PID", str(PID)], ["ClientID", "'" + User + "'"]]
        print "1"
        Config.Database.insertar_datos("Users", lista_tupla)
        DB_ID = Config.Database.obtener_registro("Users", ["DB_ID"], "PID = %i" % PID)[0][0]
        print "2"
        lista_tupla = [["DB_ID", DB_ID], 
                       ["NombreEmpresa", "'SIN NOMBRE'"], 
                       ["NombreUsuario", "'SIN NOMBRE'"],
                       ["Direccion", "'SIN DIRECCION'"],
                       ["Correo", "'SIN CORREO'"],
                       ["CalifServicio", "'0'"],
                       ["CalifLimpieza", "'0'"],
                       ["CalifComida", "'0'"],
                       ["Longitud", 0],
                       ["Latitud", 0],
                       ["CalifServicioVotos", "'0'"],
                       ["CalifLimpiezaVotos", "'0'"],
                       ["CalifComidaVotos", "'0'"],
                       ["AceptaEfectivo", False],
                       ["AceptaTarjeta", False],
                       ["OfreceDesayuno", False],
                       ["OfreceComida", False],
                       ]
        Config.Database.insertar_datos("DatosPersonales", lista_tupla)
        print "3"
        lista_tupla = [["DB_ID", DB_ID],
                   ["PROFILEPIC", "'N'"],
                   ["BACKGROUNDPIC", "'N'"],
                   ["HASPROFILE", False],
                   ["HASBACKGROUND", False]
                   ]
        Config.Database.insertar_datos("Images", lista_tupla)
        print "4"
        lista_tupla = [["DB_ID", DB_ID], 
                       ["Platillos", "'Chilaquiles|Enchiladas'"],
                       ["PlatillosPrecio", "'35|40'"],
                       ["Extras", "'Extra1|Extra2'"],
                       ["ExtrasPrecio", "'5|10'"],
                       ["Incluye", "'Fruta|Cafe de olla|Te o jugo'"],
                       ["IncluyeBool", "'0|0|0'"],
                       ["HoraApertura", "'%s'" % datetime.time(8,0,0)],
                       ["HoraCierre", "'%s'" % datetime.time(12,0,0)]
                       ]
        Config.Database.insertar_datos("Desayunos", lista_tupla)
        print "5"
        lista_tupla = [["DB_ID", DB_ID], 
                       ["Entrada", "'Consome|Crema de zanahoria'"],
                       ["PlatoFuerte", "'Pechuga de pollo|Enfrijoladas'"],
                       ["PlatoFuertePrecio", "'50|45'"],
                       ["Guarnicion", "'Arroz|Frijoles|Spagethi'"],
                       ["CantidadGuarniciones", 2],
                       ["Incluye", "'Agua|Tortillas|Postre'"],
                       ["IncluyeBool", "'0|0|0'"],
                       ["HoraApertura", "'%s'" % datetime.time(13,0,0)],
                       ["HoraCierre", "'%s'" % datetime.time(18,0,0)]
                       ]
        Config.Database.insertar_datos("Comidas", lista_tupla)
        print "6"
        return {"Status": "0", "PID": str(PID)}



def force_bytes(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Similar to smart_bytes, except that lazy instances are resolved to
    strings, rather than kept as lazy objects.

    If strings_only is True, don't convert (some) non-string-like objects.
    """
    # Handle the common case first for performance reasons.
    if isinstance(s, bytes):
        if encoding == 'utf-8':
            return s
        else:
            return s.decode('utf-8', errors).encode(encoding, errors)
    if strings_only and is_protected_type(s):
        return s
    if isinstance(s, memoryview):
        return bytes(s)
    #print isinstance(s, Promise)
    if not isinstance(s, str):
        return str(s).encode(encoding, errors)
    else:
        return s.encode(encoding, errors)
    
#pbkdf2_sha256$100000$E2yGwFq0zGjM$5fN+ssKKZm+JgerA/s9fvX2LyqJb/0dgN5nUVFXy4no=
#pbkdf2_sha256$100000$E2yGwFq0zGjM$5fN+ssKKZm+JgerA/s9fvX2LyqJb/0dgN5nUVFXy4no=