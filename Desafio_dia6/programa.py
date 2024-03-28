from producto import Producto
from tienda import Restaurante, Farmacia, Supermercado


print("""
¡Bienvenido a nuestra tienda!
Actualmente ofrecemos tres servicios:

1. Restaurante
2. Farmacia
3. Supermercado
""")

usuario = int(input("Por favor, ingresa el número correspondiente al servicio donde te gustaría realizar un pedido: "))


if usuario == 1:
    restaurante = Restaurante("nombre", 0)  
    print("Ahora te encuentras en nuestro Restaurante... \n")

    while True:
        nombre = input("Ingrese el nombre del producto que deseas ordenar: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock inicial del producto: "))

        p = Producto(nombre, precio, stock)
        restaurante.ingresar_productos(nombre, precio, stock)

        continuar = input("¿Deseas ingresar otro producto? (si/no): ")
        if continuar.lower() != 'si':
            break

    restaurante.listar_productos()
        
       
    # print("\nLista de productos en el restaurante:")
    # print(p.listar_productos())



elif usuario == 2:
    print("ingresaste a la farmacia")
else:
   print("ingresaste al supermercado")






#   

#     