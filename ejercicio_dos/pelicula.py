from categoria import Categoria


class Pelicula(Categoria):
    def __init__(self, titulo, categoria):
        super().__init__(categoria)
        self.titulo = titulo

    def mostrar_pelicula(self):
        print(
            f"La película '{self.titulo}' pertenece a la categoría {self.nombre}")
