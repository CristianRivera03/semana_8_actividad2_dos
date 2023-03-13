from juego import Juego
from jugador import Jugador

jugador1 = Jugador("Daniel", "Scorpion", 100)
jugador2 = Jugador("Eduardo", "Link", 100)

juego = Juego(jugador1, jugador2)
juego.jugar()
