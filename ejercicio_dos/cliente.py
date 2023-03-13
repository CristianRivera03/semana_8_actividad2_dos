from categoria import Categoria
from pelicula import Pelicula


class Cliente:
    def __init__(self, categoria_elegida):
        self.categoria_elegida = categoria_elegida

    def mostrar_peliculas(self):
        if self.categoria_elegida == 'Acción':
            pelicula = Pelicula('Terminator', 'Acción')
            pelicula.mostrar_pelicula()
        elif self.categoria_elegida == 'Comedia':
            pelicula = Pelicula('¿Qué pasó ayer?', 'Comedia')
            pelicula.mostrar_pelicula()
        elif self.categoria_elegida == 'Terror':
            pelicula = Pelicula('El conjuro', 'Terror')
            pelicula.mostrar_pelicula()
        else:
            print("La categoría seleccionada no existe.")
