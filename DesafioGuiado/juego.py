from personaje import Personaje
import random

print("Bienvenido a Gran Fantasia!!!")

nombre = input("Por favor ingrese el nombre de su personaje: \n")

p = Personaje(nombre)

print("¡Oh no!, ¡Ha aparecido un Orco! \n")

o = Personaje('other')
probabilidad_ganar = p.get_prob_ganar(o)

opcion_orco = Personaje.mostrar_dialogo(probabilidad_ganar)

while opcion_orco == 1:
    numero = random.uniform(0,1)
    resultado = ''
    resultado = 'G' if numero < probabilidad_ganar else 'P'
    if resultado == 'G':
        print(f"""
              Le has ganado al Orco, Felicidades!
              Recibiras 50 puntos de experiencia!.""")
        p.estado_personaje = 50
        o.estado_personaje = -30
    elif resultado == 'P':
        print(f"""
              Lo siento! El Orco te ha ganado!
              Has perdido 30 puntos de experiencia!.""")
        p.estado_personaje = -30
        o.estado_personaje = 50

    print(p.estado_personaje)
    print(o.estado_personaje)
    probabilidad_ganar = p.get_prob_ganar(o)
    opcion_orco = Personaje.mostrar_dialogo(probabilidad_ganar)

print("Has huido! El Orco ha quedado atras")

    
