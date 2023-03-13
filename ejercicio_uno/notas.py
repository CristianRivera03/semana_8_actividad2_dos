from estudiante import Estudiante, alumno
from materia import Materia, asignatura


class Notas(Estudiante,Materia):
    def __init__(self, nombre, apellido, codigo, materia, nota_parcial, nota_laboratorio):
        Estudiante.__init__(self, nombre, apellido, codigo)
        Materia.__init__(self, materia)
        self.nota_parcial = nota_parcial
        self.nota_laboratorio = nota_laboratorio
        
    def notas(self, computo):
        computo = (self.nota_parcial * 0.4)+(self.nota_laboratorio *0.6)
        return f'''
    El estudiante {self.nombre} {self.apellido} con codigo {self.codigo}
    Cursando la materia {self.materia}
    Obtuvo 
    Laboratorio: {self.nota_laboratorio}
    Parcial: {self.nota_parcial}
    Dado como nota de computo: {computo}'''
    

resultado = Notas(alumno.nombre, alumno.apellido, alumno.codigo, asignatura.materia, 10, 10)

print(resultado.notas(computo=0))
