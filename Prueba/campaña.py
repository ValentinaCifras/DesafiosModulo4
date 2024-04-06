from error import LargoExcedidoError
from datetime import date
from anuncio import Video,Display,Social

class Campaña():
    def __init__(self, nombre: str, fecha_inicio:date, fecha_termino:date, anuncios: list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios

    def __str__(self):
        cantidad_video = 0
        cantidad_display = 0
        cantidad_social = 0

        for elemento in self.__anuncios:
            if isinstance(elemento,Video):
                cantidad_video +=1
            elif isinstance(elemento,Display):
                cantidad_display +=1
            elif isinstance(elemento,Social):
                cantidad_social +=1
            
        return f"""
            Nombre de la campaña:{self.__nombre} 
            Anuncios: {cantidad_video} Video, {cantidad_display} Display, {cantidad_social}Social
            """

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre): 
        if len(nombre) > 250:
            raise LargoExcedidoError("Ha excedido la cantidad de caracteres permitidos") 
        else:
            self.__nombre = nombre 

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

    @property
    def anuncios(self):
        return self.__anuncios

