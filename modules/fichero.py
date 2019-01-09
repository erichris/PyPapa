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
import random
import string
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
        
 
lote = 0;
codigo = 0;
id = "PRO"
doc = Fichero();
fichero = doc.abrir_fichero("CodigosP00.txt", doc.escritura)
 
for i in range(0, 1000):
    fichero.write( id + '%02d' % lote + '%03d' % codigo  + " " + "".join( [random.choice(string.hexdigits) for i in xrange(8)] ) + "\n")
    codigo += 1
doc.cerrar_fichero(fichero)
lote = 1
codigo = 0;
fichero = doc.abrir_fichero("CodigosP01.txt", doc.escritura)
for i in range(0, 1000):
    fichero.write( id + '%02d' % lote + '%03d' % codigo  + " " + "".join( [random.choice(string.hexdigits) for i in xrange(8)] ) + "\n")
    codigo += 1
doc.cerrar_fichero(fichero)
lote = 2
codigo = 0;
fichero = doc.abrir_fichero("CodigosP02.txt", doc.escritura)
for i in range(0, 1000):
    fichero.write( id + '%02d' % lote + '%03d' % codigo  + " " + "".join( [random.choice(string.hexdigits) for i in xrange(8)] ) + "\n")
    codigo += 1
doc.cerrar_fichero(fichero)
lote = 3
codigo = 0;
fichero = doc.abrir_fichero("CodigosP03.txt", doc.escritura)
for i in range(0, 1000):
    fichero.write( id + '%02d' % lote + '%03d' % codigo  + " " + "".join( [random.choice(string.hexdigits) for i in xrange(8)] ) + "\n")
    codigo += 1
doc.cerrar_fichero(fichero)
lote = 4
codigo = 0;
fichero = doc.abrir_fichero("CodigosP04.txt", doc.escritura)
for i in range(0, 1000):
    fichero.write( id + '%02d' % lote + '%03d' % codigo  + " " + "".join( [random.choice(string.hexdigits) for i in xrange(8)] ) + "\n")
    codigo += 1
doc.cerrar_fichero(fichero)



