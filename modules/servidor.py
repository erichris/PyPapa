#Servidor para manejar diferentes eventos
import SocketServer
import threading
#import time
#from cPickle import dumps, loads
from setup import Setup
from json import dumps, loads
from eventHandlers.ProtocolManager import protocolHandler

#from auxiliar import MapaPartidas

#class MiTCPHandler(SocketServer.BaseRequestHandler):
class MiTCPHandler(SocketServer.StreamRequestHandler):	
	Config = Setup()
	
	def handle(self):
		package = ""	
		while package != "salir":
			try:
				package = self.rfile.readline().strip()
				#package = self.request.recv(4000)
				print package
				if(package != ""):
					package = loads(package)
					print package
					mensaje = protocolHandler(self.Config, package)
					print mensaje
					mensaje = dumps(mensaje)
					self.request.sendall(mensaje)
			except:
				print "Error on package:"
				print package
				
			
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
	pass
	
def servidor(host, port):
	conexion = (host,port)
	server =  ThreadServer(conexion, MiTCPHandler)
	server_thread = threading.Thread(target = server.serve_forever)
	server_thread.start()
	

