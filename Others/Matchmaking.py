from Others.Partida import Partida1vs1, PartidaOne4All

class MatchmakingClass1vs1():
    def __init__(self):
        self.waitingQueue = []
        self.matchedPlayers = {} #{PartidaID : [Player1, Player2]}
        self.activeGames = {} #{PartidaID : ClassPartida}
        self.activePlayers = {} #{Player : PartidaID}
        self.currentGame = 0;
    
    def queuePlayer(self, username):
        #Create room
        if(username not in self.waitingQueue):
            self.waitingQueue.append(username)
            self.activePlayers[username] = -1;
        #Join Room
        if(len(self.waitingQueue) >= 2):
            #Se remueven del Queue ambos jugadores
            player1 = self.waitingQueue.pop(0);
            player2 = self.waitingQueue.pop(0);
            #Se crea una referencia del juego contra los jugadores
            self.matchedPlayers[self.currentGame] = [player1, player2]
            #Se crea una referencia de los jugaodres contra el id del room
            self.activePlayers[player1] = self.currentGame;
            self.activePlayers[player2] = self.currentGame;
            #Se crea la partida
            self.activeGames[self.currentGame] = Partida1vs1(player1, player2, self.currentGame);
            #Se mueve el id de partida en 1
            self.currentGame += 1;
            
    #Funcion para verificar si el jugador ya encontro partida
    def isMatched(self, username):
        if(username in self.activePlayers.keys()):
            if(self.activePlayers[username] != -1):
                #Regresar que esta actualmente en partida
                return True
        
        return False
    
    #Funcion para obtener la partida actual de los jugadores
    def getMatch(self, username):
        return self.activePlayers[username]
    
    def getClassMatch(self, ID_Network):
        return self.activeGames[self.activePlayers[ID_Network]]
    
    #Funcion para cancelar el match del jugador
    def cancel_queue(self, username):
        if(self.isMatched(username)):
            return False
        if(username in self.waitingQueue):
            self.waitingQueue.remove(username)
            return True;
    
    
    
class MatchmakingClassOne4All():
    def __init__(self):
        self.waitingQueue = []
        self.matchedPlayers = {} #{PartidaID : [Player1, Player2]}
        self.activeGames = {} #{PartidaID : ClassPartida}
        self.activePlayers = {} #{Player : PartidaID}
        self.currentGame = 0;
    
    def queuePlayer(self, username):
        #Create room
        if(username not in self.waitingQueue):
            self.waitingQueue.append(username)
            self.activePlayers[username] = -1;
        #Join Room
        if(len(self.waitingQueue) >= 4):
            #Se remueven del Queue ambos jugadores
            print"pop"
            player1 = self.waitingQueue.pop(0);
            player2 = self.waitingQueue.pop(0);
            player3 = self.waitingQueue.pop(0);
            player4 = self.waitingQueue.pop(0);
            #Se crea una referencia del juego contra los jugadores
            print "match"
            self.matchedPlayers[self.currentGame] = [player1, player2, player3, player4]
            #Se crea una referencia de los jugaodres contra el id del room
            print "currentGame"
            self.activePlayers[player1] = self.currentGame;
            self.activePlayers[player2] = self.currentGame;
            self.activePlayers[player3] = self.currentGame;
            self.activePlayers[player4] = self.currentGame;
            print "partida"
            #Se crea la partida
            self.activeGames[self.currentGame] = PartidaOne4All(player1, player2, player3, player4, self.currentGame);
            #Se mueve el id de partida en 1
            self.currentGame += 1;
            
    #Funcion para verificar si el jugador ya encontro partida
    def isMatched(self, username):
        if(username in self.activePlayers.keys()):
            if(self.activePlayers[username] != -1):
                #Regresar que esta actualmente en partida
                return True
        
        return False
    
    #Funcion para obtener la partida actual de los jugadores
    def getMatch(self, username):
        return self.activePlayers[username]
    
    def getClassMatch(self, ID_Network):
        return self.activeGames[self.activePlayers[ID_Network]]
    
    #Funcion para cancelar el match del jugador
    def cancel_queue(self, username):
        if(self.isMatched(username)):
            return False
        if(username in self.waitingQueue):
            self.waitingQueue.remove(username)
            return True;
    
ActualMatchmaking1vs1 = MatchmakingClass1vs1()
ActualMatchmakingOne4All = MatchmakingClassOne4All()