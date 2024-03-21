from pizza import Pizza

#Requerimiento 5
#A
print(f"Nuestras pizzas tienen un valor de ${Pizza.precio} y son de tamaño {Pizza.tamano} ")

#B
print(Pizza.validar_elemento('salsa de tomate',["salsa de tomate", "salsa bbq"]))

#C
nueva_pizza = Pizza()
nueva_pizza.realizar_pedido()
print(nueva_pizza.esvalido)

#D
print(f"Ingredientes proteicos: {nueva_pizza.prot}. Ingredientes Vegetales: {nueva_pizza.veg1} y {nueva_pizza.veg2}. Masa: {nueva_pizza.masa}.")

#E
print(Pizza.esvalido)


 