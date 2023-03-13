class Jugador:
    def __init__(self, nombre, luchador, vida=100):
        self.nombre = nombre
        self.luchador = luchador
        self.vida = vida

    def recibir_golpe(self):
        self.vida -= 30
        print(f"{self.nombre} recibió un golpe y ahora tiene {self.vida}% de vida.")
