from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo ):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"El subtipo '{sub_tipo}' no es válido para este tipo de anuncio.")
        self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos():
        for info in Video, Display, Social:
            print(f"\nFORMATO: {info.FORMATO}")
            print("==================")
            for subtipo in info.SUB_TIPOS:
                print(f"> {subtipo} \n")
           

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass


class Video(Anuncio):
        FORMATO = "Video"
        SUB_TIPOS = ("instream","outstream")

        def __init__(self, ancho:int, alto:int, url_archivo: str, url_clic: str, sub_tipo: str, duracion:int):
            super().__init__(1,1, url_archivo, url_clic, sub_tipo)
            self.__duracion = duracion if duracion > 0 else 5

        @property
        def ancho(self):
            return self.__ancho
    
        @ancho.setter
        def ancho(self):
            pass

        @property
        def duracion(self):
             return self.__duracion
        
        @duracion.setter
        def duracion(self, duracion):
             self.__duracion = duracion if duracion > 0 else 5

        def comprimir_anuncio():
            print ("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

        def redimensionar_anuncio():
            print ("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")



class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional","native")

    def __init__(self, ancho: int, alto:int, url_archivo: str, url_clic: str, sub_tipo: str):
            super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
            
    
    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook","linkedin")

    def __init__(self, ancho: int, alto:int, url_archivo: str, url_clic: str, sub_tipo: str):
            super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")




#anuncio_valido = Video(1, 1, "abc.cl", "def.cl", "instream", 30)
#anuncio_valido.sub_tipo = "linkedin"


# Anuncio.mostrar_formatos()


