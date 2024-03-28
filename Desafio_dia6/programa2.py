from tienda import Restaurante, Farmacia, Supermercado

print("""
¡Bienvenido a nuestra tienda!
Actualmente ofrecemos tres servicios:

- Restaurante
- Farmacia
- Supermercado
""")

# Menú principal

nombre = input("Indique el nombre de la tiendaa a la que desea ingresar: ")
costo_delivery = float(input("Ingrese el costo de delivery: "))
    
if nombre.lower == 'restaurante':
    Restaurante(nombre, costo_delivery)
    print(f"Bienvenido a {nombre.tipo}...")
elif nombre.lower == 'farmacia':
    Farmacia(nombre, costo_delivery)
    print(f"Bienvenido a {nombre.tipo}...")
elif nombre.lower == 'supermercado':
    Supermercado(nombre, costo_delivery)
    print(f"Bienvenido a {nombre.tipo}...")
 
        

        # Ciclo para ingresar productos a la tienda
    while True:
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock inicial del producto: "))
            
            tienda.ingresar_productos(nombre_producto, precio_producto, stock_producto)
            
            continuar = input("¿Desea ingresar otro producto? (S/N): ").upper()
            if continuar != 'S':
                break

        # Menú secundario
    while True:
            opcion = int(input("Selecciona una opción:\n1. Listar productos\n2. Realizar venta\n3. Volver al menú principal\nOpción: "))

            if opcion == 1:
                print(tienda.listar_productos())
            elif opcion == 2:
                tienda.realizar_venta(nombre_producto,cantidad)
        
            elif opcion == 3:
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")