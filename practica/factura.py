from practica import Servicio
from practica import servicio_spa
from practica import Cliente

class Factura(Servicio,Cliente):
    pass 

    def ticket():
        return f'Cliente {Cliente.nombre} cantidad: {servicio_spa.servicio} Precio: {servicio_spa.precio}'

factura_uno = Factura
print(factura_uno.ticket())