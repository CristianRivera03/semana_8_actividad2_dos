class Servicio:
    def __init__(self, servicio, precio) -> None:
        self.servicio = servicio
        self.precio = precio
        
    def obtener_servicio(self):
        return f'Servicio de la empresa {self.servicio} con un precio de {self.precio}'
    
servicio_spa = Servicio("Masaje Corporal" , 15.00)
print(servicio_spa.obtener_servicio())