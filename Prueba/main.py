from clase_metodos import Persona
from clase_metodos_str import Pizza
from pedido import Pedido
from datos import Datos

if __name__ == "__main__":
    
    
    pizza1 = Pizza ("Pizza hawaiana", "Pina", "Queso", "Familiar")
    
    cliente1 = Persona ("Sebastian", "Vaca", "Quito", "sebas@hotmail.com", 987654321)
    Pedido1 = Pedido ("Sebastian", "Vaca", "Quito", "sebas@hotmial.com", 987654321, "Habana y tapi", "San Juan", 722)
    
    dato1 = Datos(1, Persona("Sebastian", "Vaca", "Quito", "sebas@hotmail.com", 987654321), Pizza("Pizza hawaiana", "Pina", "Queso", "Familiar"))
    
#Objetos 
    print("")
    print("Objetos:")
    print(vars(pizza1))
    print(vars(cliente1))
    print(vars(Pedido1))

#objetos en Objetos
    print("")
    print("Objetos en Objetos:")
    print(vars(dato1))
    print("Cliente")
    print(vars(dato1.Persona))
    print("Pizza")
    print(vars(dato1.Pizza))
    print("Pedido")
    print(vars(dato1.Pedido))
    