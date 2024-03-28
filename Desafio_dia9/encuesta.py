from pregunta import Pregunta

class Encuesta():
    def __init__(self, nombre:str, pregunta:list):
        self.nombre = nombre
        self.__pregunta = [
            Pregunta(
                p["enunciado"],
                p["ayuda"],
                p["alternativas"],
                p["requerido"],
                )for p in pregunta
        ]

        self.__listados_respuestas = []
        
        
    def mostrar_encuesta(self):
        print(self.nombre)

        for p in self.__preguntas:
            p.mostrar_pregunta()

    def agregar_listado_respuesta(self, listado_respuestas):
        self.__listados_respuestas.append(listado_respuestas)

        
class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre:str, preguntas: list, edad_min: int, edad_max:int):
        super().__init(nombre, preguntas)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    @property
    def edad_min(self):
        return self.__edad_min
    
    @edad_min.setter
    def edad_min(self, nueva_min):
        self.__edad_min = nueva_min

    @property
    def edad_max(self):
        return self.__edad_max

    @edad_max.setter
    def edad_max(self, nueva_max):
        self.__edad_max = nueva_max


    def agregar_respuesta(self, respuestas:list):
        if self.__edad_min <= respuestas.usuario.edad <= self.__edad_max:#clase usuario
            super().agregar_listado_respuestas(respuestas)
    

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre:str, pregunta:list, region:list):
        super().__init__(nombre, pregunta)
        self.__region = region

    @property
    def regiones(self):
        return self.region
    
    @regiones.setter
    def regiones(self, nueva_region):
        self.__region = nueva_region


    def agregar_respuesta(self, respuestas:list):
        if self.__region in respuestas.usuario.region:
            super().agregar_listado_respuestas(respuestas)