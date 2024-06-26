class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado_personaje(self):
            return f"""
                       Nombre: {self.nombre} 
                       Nivel: {self.nivel}
                       Experiencia: {self.experiencia}"""
    
    @estado_personaje.setter
    def estado_personaje(self, exp):
        temporal_exp = self.experiencia + exp

        while temporal_exp >= 100:
             self.nivel +=1
             temporal_exp -=100

        while temporal_exp < 0:
             if self.nivel > 1:
                  temporal_exp = exp + 100
                  self.nivel -=1
             else:
                temporal_exp = 0
        
        self.experiencia = temporal_exp

    def get_prob_ganar(self,other):
         if self < other:
              return 0.33
         elif self > other:
              return 0.66
         else:
              return 0.5
         
    @staticmethod
    def mostrar_dialogo(probabilidad_ganar):
         return int(input(
              f"""Con tu nivel actual, tienes {probabilidad_ganar *100}% de probabilidades de ganarle al Orco.

                Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
                Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.

                Que deseas hacer?

                1. Atacar
                2.Huir
                """
                ))

    def __lt__(self,other):
        return self.nivel < other.nivel
    
    def __gt__ (self,other):
         return self.nivel < other.nivel
    
    def __eq__ (self,other):
         return self.nivel == other.nivel
             

         