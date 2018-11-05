from setup import Setup
from Others.Partida import Partida

if __name__ == "__main__":
    partida = Partida("erichris", "annieZa", 1)
    setup = Setup();
    DB = setup.Database
    partida.startPartida(DB)
    print partida.Jugador1
    print partida.Jugador2