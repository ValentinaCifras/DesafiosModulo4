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
productos = []

if tipo == 1:
    tienda = Restaurante(nombre,costo_delivery)
    restaurante = tienda
    print("\nAhora te encuentras en el Restaurante!\n")

    while True:
        opcion = input("Deseas ingresar un producto a tu lista? Responde Si o No: \n ")

        if opcion.lower() == 'si':
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            producto = Producto(nombre,precio,stock)
            restaurante.ingresar_productos(nombre, precio, stock)
            productos.append(producto)

        elif opcion.lower() == 'no':
            while True:
                eleccion = int(input("""
                                 Que deseas hacer? \n
                                 1.Listar productos existentes
                                 2.Realizar venta
                                 3.Salir del programa
                                 """))
                
                if eleccion == 1:
                    print(restaurante.listar_productos())
                elif eleccion == 2:
                    nombre_producto = input("Indica el nombre del producto que deseas vender: ")
                    cantidad = int(input(f"Indicanos la cantidad de {nombre_producto} que deseas vender: "))
                    restaurante.realizar_venta(nombre_producto, cantidad)  
                    print("Procesando venta...")
                elif eleccion == 3:
                    print("Saliendo del programa...")
                    break
            break
        else:
            print("Ingrese una respuesta valida ")
    
    
            
elif tipo == 2:
    tienda = Farmacia(nombre,costo_delivery)
    farmacia = tienda
    print("\nAhora te encuentras en la Farmacia!\n")

    while True:
        opcion = input("Deseas ingresar un producto a tu lista? Responde Si o No: \n ")

        if opcion.lower() == 'si':
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            producto = Producto(nombre,precio,stock)
            farmacia.ingresar_productos(nombre, precio, stock)
            productos.append(producto)

        elif opcion.lower() == 'no':
            while True:
                eleccion = int(input("""
                                 Que deseas hacer? \n
                                 1.Listar productos existentes
                                 2.Realizar venta
                                 3.Salir del programa
                                 """))
                
                if eleccion == 1:
                    print(farmacia.listar_productos())
                elif eleccion == 2:
                    nombre_producto = input("Indica el nombre del producto que deseas vender: ")
                    cantidad = int(input(f"Indicanos la cantidad de {nombre_producto} que deseas vender: "))
                    farmacia.realizar_venta(nombre_producto, cantidad)  
                elif eleccion ==3:
                    print("Saliendo del programa...")
                    break
            break
        else:
            print("Ingrese una respuesta valida ")

elif tipo == 3:
    tienda = Supermercado(nombre,costo_delivery)
    supermercado = tienda
    print("\nAhora te encuentras en el Supermercado!\n")

    while True:
        opcion = input("Deseas ingresar un producto a tu lista? Responde Si o No: \n ")

        if opcion.lower() == 'si':
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            producto = Producto(nombre,precio,stock)
            supermercado.ingresar_productos(nombre, precio, stock)
            productos.append(producto)

        elif opcion.lower() == 'no':
            while True:
                eleccion = int(input("""
                                 Que deseas hacer? \n
                                 1.Listar productos existentes
                                 2.Realizar venta
                                 3.Salir del programa
                                 """))
                
                if eleccion == 1:
                    print(supermercado.listar_productos())
                elif eleccion == 2:
                    nombre_producto = input("Indica el nombre del producto que deseas vender: ")
                    cantidad = int(input(f"Indicanos la cantidad de {nombre_producto} que deseas vender: "))
                    supermercado.realizar_venta(nombre_producto, cantidad)  
                elif eleccion ==3:
                    print("Saliendo del programa...")
                    break
            break
        else:
            print("Ingrese una respuesta valida ")





