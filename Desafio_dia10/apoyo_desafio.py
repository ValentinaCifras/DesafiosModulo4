from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
            if ancho < 1 or ancho > 2500:
                raise DimensionError(f"Ingrese un valor entre 1 y 2500", ancho, 2500)
            self.__ancho = ancho
            print (f"{self.ancho}: Valor ingresado")
            
    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
       
            if alto < 1 or alto > 2500:
                raise DimensionError(f"Ingrese un valor entre 1 y 2500", alto, 2500)
            self.__alto = alto
            print (f"{self.alto}: Valor ingresado")



#Validar
foto_valida = Foto(-5, 50, "ruta1")
foto_valida.alto =5000


