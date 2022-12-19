from clase_metodos import pizza
class Pizza():
    Pizza = pizza
    def __init__(self, nombre, ingrediente1, ingrediente2, tamaño):
        self.nombre = nombre
        self.ingrediente1 = ingrediente1
        self.ingrediente2 = ingrediente2
        self.tamaño = tamaño
    
    def __str__(self):
        return f"Su orden es una {self.nombre} que contiene {self.ingrediente1} y {self.ingrediente2} en tamaño {self.tamaño}"

Pizza1 = pizza("Pizza de Peperoni", "Peperoni", "Queso", "Familiar")
Pizza2 = pizza("Pizza Hawaiana", "Piña", "Jamon", "Mediano")
print(Pizza1)
print(Pizza2)
print(vars(Pizza1))
print(vars(Pizza2))