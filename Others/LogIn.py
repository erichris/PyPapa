class Login():
    def __init__(self):
        print "Se inicio"
        self.currentIDPlayer = 1
        self.availableOldIDPlayer = [];
        self.ingameIDs = [];
        
    def logPlayer(self):
        newID = -1;
        if(len(self.availableOldIDPlayer) > 0):
            newID = self.availableOldIDPlayer.pop(0);
        else:
            print "//////////////"
            print self.currentIDPlayer
            newID = self.currentIDPlayer;
            self.currentIDPlayer += 1;
            print self.currentIDPlayer
            print "//////////////"
        if(newID == -1):
            print "Error al intentar logear cliente"
        else:
            self.ingameIDs.append(newID)
        return newID;