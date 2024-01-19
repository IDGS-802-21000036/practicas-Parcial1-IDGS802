import os

class Triangulo:
    #declaracion de propiedades
    cantidad = 0
    
#declaracion de constructor
    def __init__(self, cantidad):
        self.cantidad = cantidad

#declaracion de metodos de clase
    def imprimir(self):
        asteriscos = "*"
        i = 1
        j = 1
        while i < (self.cantidad+1):
            while j <= i:
                print("*"*(j))
                j += 1
            i += 1
                
    

def main():
    #Linea para limpoar la terminal
    os.system("cls")
    cantidad = int(input("Tamaño del triangulo: "))
    obj = Triangulo(cantidad)
    obj.imprimir()

if __name__ == "__main__":
    main()