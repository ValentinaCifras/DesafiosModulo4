from listado_respuestas import Listado_respuestas

class Usuario():
    def __init__(self, correo:str, edad:int, region:int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region


    @property
    def correo(self):
        return self.__correo
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def region(self):
        return self.__region
    
    @correo.setter
    def correo(self, nuevo_correo:str):
        self.__correo = nuevo_correo

    @correo.edad
    def edad(self, nueva_edad:int):
        self.__edad = nueva_edad

    @correo.region
    def region(self, nueva_region:str):
        self.__region = nueva_region

    def contestar_encuesta(self, respuestas:list):
       pass
       
   
    
    
