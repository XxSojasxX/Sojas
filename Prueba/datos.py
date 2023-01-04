from clase_metodos import Persona
from clase_metodos_str import Pizza
from pedido import Pedido

class Datos (Persona, Pizza):
     id = int
     Persona = Persona ("", "", "", "", "")
     Pizza = Pizza ("", "", "", "")
     Pedido = Pedido ("", "", "", "", "", "", "", "")
     
     def __init__(self, id, Persona, Pizza):
         
         self.id = id
         self.Persona = Persona
         self.Pizza = Pizza
        