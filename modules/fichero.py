#!/usr/bin/env python
# -*- coding: utf-8 -*-
                    ##################################################
                    #Proyecto:                                       #
                    #Version: 0.0.1                                  #
                    #Nombre:Py. Gamers Latinos                       #
                    #Fecha de inicio: 24/08/2014                     #
                    #Fase: En desarrollo                             #
                    ##################################################
                    
#Biblioteca creada para el manejo de ficheros

class Fichero():
    def __init__(self):
        self.lectura = "r"
        self.escritura = "w"
        
    def abrir_fichero(self, fichero, modalidad):
        fichero = open(fichero, modalidad)
        return fichero
    
    def cerrar_fichero(self, fichero):
        fichero.close()
        
    def buscar_valor(self, fichero, valor_deseado):
        valor = ""
        fichero = self.abrir_fichero(fichero, self.lectura)
        for linea in fichero:
            if linea.startswith(valor_deseado):
                #obtenemos el valor de la variable
                valor = linea.split("= ")
                valor = valor[1]
                valor.lstrip(" ")
                valor = valor[0: valor.index("\n")]
                break
        self.cerrar_fichero(fichero)
        return valor
    
    def sobrescribir_valor(self, fichero, valor_modificable, nuevo_valor):
        fichero_nuevo = self.abrir_fichero("temp.txt", self.escritura)
        fichero_viejo = self.abrir_fichero(fichero, self.lectura)
        for linea in fichero_viejo:
            if linea.startswith(valor_modificable):
                fichero_nuevo.write(valor_modificable + " = " + nuevo_valor + "\n")
            else:
                fichero_nuevo.write(linea)
        self.cerrar_fichero(fichero_nuevo)
        self.cerrar_fichero(fichero_viejo)
        
        fichero_nuevo = self.abrir_fichero("temp.txt", self.lectura)
        fichero_viejo = self.abrir_fichero(fichero, self.escritura)
        for linea in fichero_nuevo:
            fichero_viejo.write(linea)
        self.cerrar_fichero(fichero_nuevo)
        self.cerrar_fichero(fichero_viejo)
        