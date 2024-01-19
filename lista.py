import os

class Lista:
    #declaracion de propiedades
    lista = []
    lista_limpia = []
    listaPares = []
    listaImpares = []
    
#declaracion de constructor
    def __init__(self, lista):
        self.lista = lista

#declaracion de metodos de clase
    def ordenar(self):
        self.lista.sort()
        print("La lista ordenada es {}".format(self.lista))
        
    def quitar_repeticiones(self):
        self.lista.sort()
        for num in self.lista:
            if num not in self.lista_limpia:
                self.lista_limpia.append(num)
    
    def verificar_repeticiones(self):
        self.lista.sort()
        for num in self.lista:
            if self.lista.count(num) > 1:
                print(num, "->", self.lista.count(num))
        
    def pares(self):
        self.quitar_repeticiones()
        for num in self.lista_limpia:
            if (num%2) == 0:
                if(num not in self.listaPares):
                    self.listaPares.append(num)
        print(self.listaPares)
    
    def impares(self):
        for num in self.lista_limpia:
            if (num%2) != 0:
                if(num not in self.listaImpares):
                    self.listaImpares.append(num)
        print(self.listaImpares)
    

def main():
    #Linea para limpoar la terminal
    os.system("cls")
    cantidad = int(input("Cantidad de numeros a insertar: "))
    lista = []
    for num in range(cantidad):
        numero = int(input("Inserta el numero {}: ".format(num+1)))
        lista.append(numero)
    obj = Lista(lista)
    obj.ordenar()
    obj.verificar_repeticiones()
    obj.pares()
    obj.impares()

if __name__ == "__main__":
    main()