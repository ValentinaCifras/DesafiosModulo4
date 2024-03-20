from te import Te

sabor = int(input(f"""Indique que sabor de Te desea: 
                  1. Te negro
                  2. Te verde
                  3. Infusion de hierbas: """
                  ))

formato = int(input("Que formato desea? 300 o 500gr?: "))

tiempo,recomendacion = Te.obtener_tiempo_y_recomendacion(sabor)
precio = Te.retornar_precio(formato)

if sabor == 1:
    sabor_texto = 'Te negro'
elif sabor == 2:
    sabor_texto = 'Te verde'
elif sabor == 3:
    sabor_texto = 'Infusion de hierbas'

print(f"Ya hemos ingresado su pedido de {sabor_texto} en formato de {formato}gr. El valor es de ${precio}.\n"
      f"El tiempo de preparacion es de {tiempo} minutos y recomendamos consumirlo {recomendacion}")
