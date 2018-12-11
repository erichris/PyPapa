'''
Created on 27/08/2014

@author: HP
'''
import psycopg2
import os
from psycopg2._psycopg import TIME
import datetime


class Database():
    def crear_conexion(self, puerto, nombredb, usuario, password):
        #Ej.- database.crear_conexion("8000", "Proyecto", "postgres", "tkieromuxho1")
        entrada = "port= "+puerto+" dbname= "+nombredb+" user= "+usuario+" password= "+password
        self.connection = psycopg2.connect(entrada)
        self.cursor = self.connection.cursor()
        self.command = ""
        
    def crear_tabla(self, nombre_tabla, lista_tupla):
        #nombre_tabla = "Nombre de la tabla"
        #lista_columnas = ["Id", "Nombre", "Edad", "Direccion", "Salario"]
        #lista_valor = ["INT PRIMARY KEY", "TEXT", "INT", "CHAR(50)", "REAL"]
        #lista_NULL = [1, 1, 1, 0, 0]
        #lista_tupla = [["Id", "INT PRIMARY KEY", true]]
        comando = "DROP TABLE IF EXISTS " + nombre_tabla
        self.cursor.execute (comando)
        self.command = "CREATE TABLE %s" % nombre_tabla
        table = "("
        for time in range(0, len(lista_tupla)):
            table += lista_tupla[time][0] + " "
            table += lista_tupla[time][1] + " "
            if time == len(lista_tupla) - 1:
                pass
            elif lista_tupla[time][2] == 1:
                table += "NOT NULL, "
            else:
                table += ", "
        table += ")"
        self.command += table
        print self.command
        self.cursor.execute(self.command)
        self.connection.commit()


    def insertar_datos(self, nombre_tabla, lista_columnas):
        #nombre_tabla = "Nombre de la tabla"
        #lista_columnas = ["Id", "Nombre", "Edad", "Direccion", "Salario"]
        #lista_valor = ["INT PRIMARY KEY", "TEXT", "INT", "CHAR(50)", "REAL"]
        self.command = "INSERT INTO "
        table = nombre_tabla
        table += "("
        for time in range(0, len(lista_columnas)):
            table += lista_columnas[time][0]
            if time != len(lista_columnas) - 1:
                table += ", "
            else:
                table += ") VALUES ("
        for time in range(0, len(lista_columnas)):
            table += str(lista_columnas[time][1])
            if time != len(lista_columnas) - 1:
                table += ", "
            else:
                table += ")"
        self.command += table
        #print command
        print self.command
        self.cursor.execute(self.command)
        self.connection.commit()
        
    def obtener_registros(self, nombre_tabla, lista_columnas):
        self.command = "SELECT "
        table = ""
        for time in range(0, len(lista_columnas)):
            table += lista_columnas[time]
            if time != len(lista_columnas) - 1:
                table += ", "
            else:
                table += " from "
        table += nombre_tabla
        self.command += table
        print self.command
        self.cursor.execute(self.command)
        registros = []
        time = 0
        for registro in self.cursor:
            registros.append([])
            for element in registro:
                registros[time].append(element)
            time += 1
        return registros
    
    def actualizar_registro(self, nombre_tabla, colum_value, ID_value):
        #nombre_tabla = "Nombre de tabla"
        #colum_value = "nombre = 'Christian'"
        #ID_value = "ID = 001"
        self.command = "UPDATE "
        table = nombre_tabla + " set "
        table += colum_value
        table += " where "
        table += ID_value
        self.command += table
        print self.command
        self.cursor.execute(self.command)
        self.connection.commit()
        
    def eliminar_registro(self, nombre_tabla, ID_value):
        self.command = "DELETE from "
        table = nombre_tabla
        table += " where "
        table += ID_value
        self.command += table
        print self.command
        self.cursor.execute(self.command)
        self.connection.commit()
        
    def obtener_registro(self, nombre_tabla, lista_columnas, ID_value):
        self.command = "SELECT "
        table = ""
        for time in range(0, len(lista_columnas)):
            table += lista_columnas[time]
            if time != len(lista_columnas) - 1:
                table += ", "
            else:
                table += " from "
        table += nombre_tabla
        table += " where "
        table += ID_value
        self.command += table
        #print command
        print self.command
        self.cursor.execute(self.command)
        registros = []
        time = 0
        for registro in self.cursor:
            registros.append([])
            for element in registro:
                registros[time].append(element)
            time += 1
        return registros
        
if __name__ == "__main__":
    db = Database()
    
    db.crear_conexion("5432", "LaPapa", "postgres", "Nomorelove12")
    #db.crear_conexion("5432", "lapapa", "hakapapa", "Lapapa2019")
    
    #db.cursor.execute("UPDATE Comidas set Guarnicion = 'Arroz|Frijoles|Spagethi|Dummy' where DB_ID = 2");
    
    #DB_ID = db.obtener_registro("Users", ["DB_ID"], "ClientID = " + 34673)
    #print DB_ID
    lista_tupla = [["DB_ID", "SERIAL PRIMARY KEY", True], 
                   ["PID", "INT", True],
                   ["ClientID", "TEXT", True]
                   ]
    db.crear_tabla("Users", lista_tupla)
    
    
    lista_tupla = [["DB_ID", "INT", True],
                   ["PROFILEPIC", "TEXT", True],
                   ["BACKGROUNDPIC", "TEXT", True],
                   ["HASPROFILE", "BOOL", True],
                   ["HASBACKGROUND", "BOOL", True]
                   ]
    db.crear_tabla("Images", lista_tupla);
        
        
    lista_tupla = [["DB_ID", "INT", True], 
                   ["NombreEmpresa", "TEXT", True], 
                   ["NombreUsuario", "TEXT", True],
                   ["Direccion", "TEXT", True],
                   ["Latitud", "DOUBLE PRECISION", True],
                   ["Longitud", "DOUBLE PRECISION", True],
                   ["Correo", "TEXT", True],
                   ["CalifServicio", "INT", True],
                   ["CalifServicioVotos", "INT", True],
                   ["CalifLimpieza", "INT", True],
                   ["CalifLimpiezaVotos", "INT", True],
                   ["CalifComida", "INT", True],
                   ["CalifComidaVotos", "INT", True],
                   ["AceptaEfectivo", "BOOL", True],
                   ["AceptaTarjeta", "BOOL", True],
                   ["OfreceDesayuno", "BOOL", True],
                   ["OfreceComida", "BOOL", True],
                   ]
    db.crear_tabla("DatosPersonales", lista_tupla)
        
    lista_tupla = [["DB_ID", "INT", True], 
                   ["Platillos", "TEXT", True],
                   ["PlatillosPrecio", "TEXT", True],
                   ["Extras", "TEXT", True],
                   ["ExtrasPrecio", "TEXT", True],
                   ["Incluye", "TEXT", True],
                   ["IncluyeBool", "TEXT", True],
                   ["HoraApertura", "TIME", True],
                   ["HoraCierre", "TIME", True]
                   ]
    db.crear_tabla("Desayunos", lista_tupla)
        
    lista_tupla = [["DB_ID", "INT", True], 
                   ["Entrada", "TEXT", True],
                   ["PlatoFuerte", "TEXT", True],
                   ["PlatoFuertePrecio", "TEXT", True],
                   ["Guarnicion", "TEXT", True],
                   ["CantidadGuarniciones", "INT", True],
                   ["Incluye", "TEXT", True],
                   ["IncluyeBool", "TEXT", True],
                   ["HoraApertura", "TIME", True],
                   ["HoraCierre", "TIME", True]
                   ]
    db.crear_tabla("Comidas", lista_tupla)
        
    lista_tupla = [["PEDIDO_ID", "SERIAL PRIMARY KEY", True],
                   ["COMENSAL_ID", "INT", True],
                   ["NEGOCIO_ID", "INT", True],
                   ["Plato1", "TEXT", True],
                   ["Plato2", "TEXT", True],
                   ["Plato3", "TEXT", True],
                   ["EsDesayuno", "BOOL", True],
                   ["Entregado", "BOOL", True],
                   ["Cancelado", "BOOL", True],
                   ["Hora", "TIME", True],
                   ["Fecha", "DATE", True],
                   ]
    db.crear_tabla("Pedido", lista_tupla)
    
    
    #Comensales
    lista_tupla = [["DB_ID", "SERIAL PRIMARY KEY", True], 
                   ["PID", "INT", True],
                   ["ClientID", "TEXT", True]
                   ]
    db.crear_tabla("Comensales", lista_tupla)
    
    lista_tupla = [["DB_ID", "INT", True], 
                   ["Nombre", "TEXT", True],
                   ["Correo", "TEXT", True]
                   ]
    db.crear_tabla("DatosComensal", lista_tupla)
    
    lista_tupla = [["DB_ID", "INT", True], 
                   ["COCINA_ID", "INT", True]
                   ]
    db.crear_tabla("Favoritos", lista_tupla)

    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    
#     #Vendedor
#     PID = 1678302
#     lista_tupla = [["PID", PID], ["ClientID", 78690]]
#     db.insertar_datos("Users", lista_tupla)
#      
#     DB_ID = db.obtener_registro("Users", ["DB_ID"], "PID = %i" % PID)[0][0]
#      
#     lista_tupla = [["DB_ID", DB_ID], 
#                    ["NombreEmpresa", "'LA ESTUFA'"], 
#                    ["NombreUsuario", "'Eric Christian Corona'"],
#                    ["Direccion", "'Av Amsterdam 206'"],
#                    ["Longitud", -100.43323],
#                    ["Latitud", 20.602953],
#                    ["Correo", "'erichris2902@gmail.com'"],
#                    ["CalifServicio", "0"],
#                    ["CalifServicioVotos", "0"],
#                    ["CalifLimpieza", "0"],
#                    ["CalifLimpiezaVotos", "0"],
#                    ["CalifComida", "0"],
#                    ["CalifComidaVotos", "0"],
#                    ["AceptaEfectivo", False],
#                    ["AceptaTarjeta", False],
#                    ["OfreceDesayuno", False],
#                    ["OfreceComida", False],
#                    ]
#     db.insertar_datos("DatosPersonales", lista_tupla)
#     
#     lista_tupla = [["DB_ID", DB_ID],
#                    ["PROFILEPIC", "'N'"],
#                    ["BACKGROUNDPIC", "'N'"],
#                    ["HASPROFILE", False],
#                    ["HASBACKGROUND", False]
#                    ]
#     db.insertar_datos("Images", lista_tupla)
#  
#     lista_tupla = [["DB_ID", DB_ID], 
#                    ["Platillos", "'UnPlatillo|DosPlatillos'"],
#                    ["PlatillosPrecio", "'45|67'"],
#                    ["Extras", "'Extra1|Extra2'"],
#                    ["ExtrasPrecio", "'67|90'"],
#                    ["Incluye", "'Agua|Tortilla'"],
#                    ["IncluyeBool", "'0|1'"],
#                    ["HoraApertura", "'%s'" % datetime.time(10,0,0)],
#                    ["HoraCierre", "'%s'" % datetime.time(13,0,0)]
#                    ]
#     db.insertar_datos("Desayunos", lista_tupla)
#      
#      
#     lista_tupla = [["DB_ID", DB_ID], 
#                    ["Entrada", "'Desayuno1|Desayuno2'"],
#                    ["PlatoFuerte", "'COMIDA1|COMIDA2'"],
#                    ["PlatoFuertePrecio", "'22|23'"],
#                    ["Guarnicion", "'Guar1|Guar2'"],
#                    ["CantidadGuarniciones", 2],
#                    ["Incluye", "'Incluye1|Incluye'"],
#                    ["IncluyeBool", "'0|1'"],
#                    ["HoraApertura", "'%s'" % datetime.time(14,0,0)],
#                    ["HoraCierre", "'%s'" % datetime.time(19,0,0)]
#                    ]
#     db.insertar_datos("Comidas", lista_tupla)
#  
#     
#     
#     
#     
#     
#     #Comensal
#     PID = 1678
#     lista_tupla = [["PID", PID], ["ClientID", 78690]]
#     db.insertar_datos("Comensales", lista_tupla)
#     
#     lista_tupla = [["DB_ID", 1], 
#                    ["Nombre", "'Chris Corona'"],
#                    ["Correo", "'erichris2@live.com.mx'"]
#                    ]
#     db.insertar_datos("DatosComensal", lista_tupla)
#     
#     lista_tupla = [["DB_ID", 1], 
#                    ["COCINA_ID", 1]
#                    ]
#     db.insertar_datos("Favoritos", lista_tupla)
#     
#     
#     lista_tupla = [["COMENSAL_ID", 1],
#                    ["NEGOCIO_ID", 1],
#                    ["Plato1", "'Chilaquiles'"],
#                    ["Plato2", "'Pan dulce'"],
#                    ["Plato3", "''"],
#                    ["EsDesayuno", True],
#                    ["Entregado", False],
#                    ["Cancelado", False],
#                    ["Hora", "'%s'" % datetime.time(12,30,0)],
#                    ["Fecha", "'%s'" % datetime.date.today()],
#                    ]
#     db.insertar_datos("Pedido", lista_tupla)
#     
#     lista_tupla = [["COMENSAL_ID", 1],
#                    ["NEGOCIO_ID", 1],
#                    ["Plato1", "'Sopa de chapuline'"],
#                    ["Plato2", "'Bistec en salsa verde'"],
#                    ["Plato3", "'Spagethi|Arroz'"],
#                    ["EsDesayuno", False],
#                    ["Entregado", False],
#                    ["Cancelado", False],
#                    ["Hora", "'%s'" % datetime.time(16,30,0)],
#                    ["Fecha", "'%s'" % datetime.date.today()],
#                    ]
#     db.insertar_datos("Pedido", lista_tupla)
#     
#     lista_tupla = [["COMENSAL_ID", 1],
#                    ["NEGOCIO_ID", 1],
#                    ["Plato1", "'Sopa de chapuline2'"],
#                    ["Plato2", "'Bistec en salsa verde2'"],
#                    ["Plato3", "'Spagethi|Frijoles'"],
#                    ["EsDesayuno", False],
#                    ["Entregado", False],
#                    ["Cancelado", True],
#                    ["Hora", "'%s'" % datetime.time(14,30,0)],
#                    ["Fecha", "'%s'" % datetime.date.today()],
#                    ]
#     db.insertar_datos("Pedido", lista_tupla)
#     
#     
#     