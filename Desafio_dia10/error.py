class Error(Exception):
    pass

class DimensionError(Error):
    def __init__(self, mensaje:str, dimension:int = None, maximo:int = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self. maximo = maximo

    def __str__(self) -> str:
        
        if self.mensaje and self.dimension and self.maximo:
            return f"DimensionError {self.mensaje}, {self.dimension}, {self.maximo}"
        else:
            return super().__str__()
            
        


