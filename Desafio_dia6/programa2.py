from tienda import Restaurante, Farmacia, Supermercado
from producto import Producto

print("""
¡Bienvenido a nuestra tienda!""")

tipo = int(input(
    """Por favor, indique el numero de la tienda a la cual desea ingresar: \n

    1. Restaurante
    2. Farmacia
    3. Supermercado \n
    
    """))

nombre = input("\nIndique el nombre de la tienda: \n")
costo_delivery = int(input("\nIngrese el costo de delivery: \n"))

if tipo == 1:
    tienda = Restaurante(nombre,costo_delivery)
    print("\nAhora te encuentras en el Restaurante\n")
elif tipo == 2:
    tienda = Farmacia(nombre,costo_delivery)
    print("\nAhora te encuentras en la Farmacia\n")
elif tipo == 3:
    tienda = Supermercado(nombre,costo_delivery)
    print("\nAhora te encuentras en el supermercado\n")



