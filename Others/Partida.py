from json import dumps, loads;

class Partida1vs1():
    def __init__(self, Player1, Player2, partidaNo):
        self.partidaNo = partidaNo;
        self.namePlayer1 = Player1;
        self.namePlayer2 = Player2;
        self.readyPlayer1 = False;
        self.readyPlayer2 = False;
        self.alturaPlayer1 = 0;
        self.alturaPlayer2 = 0;
        self.isAlivePlayer1 = True;
        self.isAlivePlayer2 = True;
        self.partidaReady = False;
    
    def updateScore(self, idNetwork, score):
        if(idNetwork == self.namePlayer1):
            self.alturaPlayer1 = int(score);
        else:
            self.alturaPlayer2 = int(score);
    
    def updateAlive(self, idNetwork):
        if(idNetwork == self.namePlayer1):
            self.isAlivePlayer1 = False;
        else:
            self.isAlivePlayer2 = False;
        if(not self.isAlivePlayer1 and not self.isAlivePlayer2):
            print "Debio terminar la partida"
            pass
        
    def isReady(self):
        if(self.readyPlayer1 and self.readyPlayer2):
            self.partidaReady = True;
            return True;
        return False;
    
    def setReadyPlayer(self, Network_ID):
        if(self.namePlayer1 == Network_ID):
            self.readyPlayer1 = True
        elif(self.namePlayer2 == Network_ID):
            self.readyPlayer2 = True
        else:
            print "No es la partida de dicho jugador"
            print self.namePlayer1
            print self.namePlayer2
            print Network_ID;
            
    def checkDeathPartida(self):
        if(not self.isAlivePlayer1 and not self.isAlivePlayer2):
            return True
        return False

class PartidaOne4All():
    def __init__(self, Player1, Player2, Player3, Player4, partidaNo):
        self.partidaNo = partidaNo;
        self.namePlayer1 = Player1;
        self.namePlayer2 = Player2;
        self.namePlayer3 = Player3;
        self.namePlayer4 = Player4;
        self.readyPlayer1 = False;
        self.readyPlayer2 = False;
        self.readyPlayer3 = False;
        self.readyPlayer4 = False;
        self.alturaPlayer1 = 0;
        self.alturaPlayer2 = 0;
        self.alturaPlayer3 = 0;
        self.alturaPlayer4 = 0;
        self.isAlivePlayer1 = True;
        self.isAlivePlayer2 = True;
        self.isAlivePlayer3 = True;
        self.isAlivePlayer4 = True;
        self.partidaReady = False;
    
    def updateScore(self, idNetwork, score):
        if(idNetwork == self.namePlayer1):
            self.alturaPlayer1 = int(score);
        elif(idNetwork == self.namePlayer2):
            self.alturaPlayer2 = int(score);
        elif(idNetwork == self.namePlayer3):
            self.alturaPlayer3 = int(score);
        elif(idNetwork == self.namePlayer4):
            self.alturaPlayer4 = int(score);
    
    def updateAlive(self, idNetwork):
        if(idNetwork == self.namePlayer1):
            self.isAlivePlayer1 = False;
        elif(idNetwork == self.namePlayer2):
            self.isAlivePlayer2 = False;
        elif(idNetwork == self.namePlayer3):
            self.isAlivePlayer3 = False;
        elif(idNetwork == self.namePlayer4):
            self.isAlivePlayer4 = False;
        if(not self.isAlivePlayer1 and not self.isAlivePlayer2 and not self.isAlivePlayer3 and not self.isAlivePlayer4):
            print "Debio terminar la partida"
            pass
        
    def isReady(self):
        if(self.readyPlayer1 and self.readyPlayer2 and self.readyPlayer3 and self.readyPlayer4):
            self.partidaReady = True;
            return True;
        return False;
    
    def setReadyPlayer(self, Network_ID):
        if(self.namePlayer1 == Network_ID):
            self.readyPlayer1 = True
        elif(self.namePlayer2 == Network_ID):
            self.readyPlayer2 = True
        elif(self.namePlayer3 == Network_ID):
            self.readyPlayer3 = True
        elif(self.namePlayer4 == Network_ID):
            self.readyPlayer4 = True
        else:
            print "No es la partida de dicho jugador"
            print self.namePlayer1
            print self.namePlayer2
            print self.namePlayer3
            print self.namePlayer4
            print Network_ID;
            
    def checkDeathPartida(self):
        if(not self.isAlivePlayer1 and not self.isAlivePlayer2 and not self.isAlivePlayer3 and not self.isAlivePlayer4):
            return True
        return False
    
