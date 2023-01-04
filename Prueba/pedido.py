from clase_metodos import Persona

class Pedido (Persona):
    nombre       = str 
    apellido     = str
    ciudad       = str
    correo       = str
    telefono     = str
    direccion    = str
    sector       = str
    numerocasa  = str
    
    def __init__(self, nombre, apellido, ciudad, correo, telefono, direccion, sector, numerocasa):
        super().__init__(nombre, apellido, ciudad, correo, telefono)
        
        self.direccion  = direccion
        self.telefono   = telefono
        self.numerocasa = numerocasa