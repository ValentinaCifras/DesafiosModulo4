from ingredientes import lista_ingredientes

class Pizza(): #Requerimiento 1
    precio = 10000
    tamano = 'Familiar'

    @staticmethod # Requerimiento 2
    def validar_elemento(ingrediente:str, lista_ingredientes):
            if ingrediente.lower() in lista_ingredientes:
                return True   
            else:
                return False
            

    def realizar_pedido(self): #Requerimiento 3
        self.prot = str(input("Ingrese su ingrediente proteico (pollo, vacuno o carne vegetal): "))
        self.veg1 = str(input("Ingrese su primer ingrediente vegetal (tomate, aceitunas, champiñones): "))
        self.veg2 = str(input("Ingrese su segundo ingrediente vegetal (tomate, aceitunas, champiñones): "))
        self.masa = str(input("Indique el tipo de masa (tradicional o delgada): "))
        
        #Requerimiento 4
        validar_prot = self.validar_elemento(self.prot, lista_ingredientes)
        validar_veg1 = self.validar_elemento(self.veg1, lista_ingredientes)
        validar_veg2 = self.validar_elemento(self.veg2, lista_ingredientes)
        validar_masa = self.validar_elemento(self.masa, lista_ingredientes)
        self.esvalido = validar_prot and validar_veg1 and validar_veg2 and validar_masa
       


   











