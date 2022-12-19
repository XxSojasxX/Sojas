from clase_metodos_str import pizza

class Promocion():

    Pizza           = pizza ("", "", "", "")
   
    def __init__(self, nombre, pizza):
        self.pizza = pizza
    
    def orden(self, Promocion):
        return f"Su orden es una promocion que contiene dos {self.pizza}"  

print(Promocion.orden)
    