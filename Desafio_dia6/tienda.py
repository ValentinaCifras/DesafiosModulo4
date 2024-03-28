from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    @abstractmethod
    def ingresar_productos(self, nombre, precio, stock):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    tipo = 'restaurante'

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_productos(self, nombre, precio, stock):
            p = Producto(nombre, precio, stock)

            encontrado = p in self.__productos
            if not encontrado:
                 self.__productos.append(p)

    def listar_productos(self):
         if len(self.__productos) > 0:
              retorno = ''
              for producto in self.__productos:
                   retorno += f"""
                NOMBRE : {producto.nombre}
                PRECIO : ${producto.precio}
                """
              return retorno
         else:
              return " No hay productos para esta tienda "
         

    def realizar_venta(self, nombre_producto, cantidad):
         pass
    
class Farmacia(Tienda):
     tipo = 'Farmacia'

     def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

     def ingresar_productos(self, nombre, precio, stock):
         p = Producto(nombre, precio, stock)

         encontrado = p in self.__productos

         if not encontrado:
                 self.__productos.append(p)

         elif encontrado:
            indice = self.__productos.index()
            self.__productos [indice].stock = p + self.__productos

     def listar_productos(self):
          if len(self.__productos) > 0:
             retorno = ''
             for __producto in self.__productos:
                m = ''
                if __producto.precio > 15000:
                    m = ("Envío gratis al solicitar este producto")
                retorno += f"""
            NOMBRE : {__producto.nombre}
            PRECIO : ${__producto.precio}
            {m}
            """
             return retorno
          else:
            return " No hay productos para esta tienda "
          

     def realizar_venta(self, nombre_producto, cantidad):
            if cantidad <= 3:
                 p = Producto(nombre_producto,0,cantidad)
                 if p in self.__productos:
                      indice = self.__productos.index(p)
                      if self.__productos[indice].stock > 0:
                           print(f"El stock disponible es {self.__productos[indice].stock}")
                           temporal = self.__productos[indice] - p
                           nuevo_stock = temporal if temporal > 0 else 0
                           self.__productos[indice].stock = nuevo_stock

class Supermercado(Tienda):
     tipo = 'Supermercado'

     def __init__(self, nombre, costo_delivery):
            self.__nombre = nombre
            self.__costo_delivery = costo_delivery
            self.__productos = []

     def ingresar_productos(self, nombre, precio, stock):
         p = Producto(nombre, precio, stock)

         encontrado = p in self.__productos

         if not encontrado:
                 self.__productos.append(p)

         elif encontrado:
            indice = self.__productos.index()
            self.__productos [indice].stock = p + self.__productos

     def listar_productos(self):
          if len(self.__productos) < 10:
             print(f"Pocos productos disponibles. Stock actual: {self.__productos} ")
             retorno = ''
             for producto in self.__productos:
                retorno += f"""
            NOMBRE : {producto.nombre}
            PRECIO : ${producto.precio}
            """
             return retorno
          else:
            return " No hay productos para esta tienda "
          
     def realizar_venta(self, nombre_producto, cantidad):
                 p = Producto(nombre_producto,0,cantidad)
                 if p in self.__productos:
                      indice = self.__productos.index(p)
                      if self.__productos[indice].stock > 0:
                           print(f"El stock disponible es {self.__productos[indice].stock}")
                           temporal = self.__productos[indice] - p
                           nuevo_stock = temporal if temporal > 0 else 0
                           self.__productos[indice].stock = nuevo_stock
          
    
     


    
          
     
        
