class Te():
    duracion = 365 
   
    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor:int):
        if sabor == 1:
            return 3, 'Al desayunar'
        elif sabor == 2:
            return 5, 'Al medio dia'
        elif sabor == 3:
            return 6, 'Al atardecer'
        
        
    @staticmethod
    def retornar_precio(formato:int):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        
  
     

