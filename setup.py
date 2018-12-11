#!/usr/bin/python2
# -*- coding: utf-8 -*-

#from modules.postresql import Database as PSQL   
from modules.sqlite import Database as PSQL
from modules.fichero import Fichero
#from Others.Matchmaking import ActualMatchmaking1vs1, ActualMatchmakingOne4All;
#from Others.LogIn import Login;

class Setup():
    def __init__(self):
        print ("Se inicio Setup")
        
        self.configuracionFile = "configuracion.txt"
        
        self.iniciar_ficheros()
        self.iniciar_database()
        self.conf_servidor()
        self.server_version_control()
        
        
        
        #self.match_making();
        #self.loger = Login();
        
    def iniciar_ficheros(self):
        self.Fichero = Fichero()
        
    def iniciar_database(self):
        database = int(self.Fichero.buscar_valor(self.configuracionFile, "DATABASE"))
        if database == 0:
            puerto = self.Fichero.buscar_valor(self.configuracionFile, "DBPORT")
            nombredb = self.Fichero.buscar_valor(self.configuracionFile, "DBNAME")
            usuario = self.Fichero.buscar_valor(self.configuracionFile, "DBUSER")
            password = self.Fichero.buscar_valor(self.configuracionFile, "DBPASS")
            self.Database = PSQL()
            self.Database.crear_conexion(puerto, nombredb, usuario, password)
        elif database == 1:
            puerto = self.Fichero.buscar_valor(self.configuracionFile, "DBPORT")
            nombredb = self.Fichero.buscar_valor(self.configuracionFile, "DBNAME")
            usuario = self.Fichero.buscar_valor(self.configuracionFile, "DBUSER")
            password = self.Fichero.buscar_valor(self.configuracionFile, "DBPASS")
            self.Database = PSQL()
            self.Database.crear_conexion(puerto, nombredb, usuario, password)
            
        
    def conf_servidor(self):
        host = self.Fichero.buscar_valor(self.configuracionFile, "HOST_SERVER")
        port = self.Fichero.buscar_valor(self.configuracionFile, "PORT_SERVER")
        self.host = host
        self.port = int(port)
        
    def server_version_control(self):
        self.version = self.Fichero.buscar_valor(self.configuracionFile, "CURRENT_VERSION")
    
    #def match_making(self):
        #self.Matchmaker1vs1 = ActualMatchmaking1vs1;
        #self.MatchmakerOne4All = ActualMatchmakingOne4All;
        
if __name__ == "__main__":
    config = Setup()
    



