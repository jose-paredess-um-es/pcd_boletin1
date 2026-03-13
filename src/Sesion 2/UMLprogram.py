from enum import Enum

# Manera de crear una enumeracón
class Edieta(Enum):
    HERBIVORO = 1
    CARNIVORO = 2
    INSECTIVORO = 3

class Comida:
    def __init__(self,  dietas:list):
        self.dietas = dietas
    def __str__(self):
        cadena = ""
        for i in self.dietas:
            cadena += str(i)
        return cadena
    

class Stock:
    def __init__(self, comida: dict):
        self.comida = comida
    
    def sacar(self, comida, cantidad):
        disponible = self.comida.get(comida, 0)
        if disponible < cantidad:
            raise ValueError('No hay suficiente comida')
        self.comida[comida] -= cantidad

    def reponer(self, comida, cantidad):
        self.comida[comida] += cantidad

    def __str__(self):
        cadena = ""
        for comida, cantidad in self.comida.items():
            if cadena != "":
                cadena = cadena + ", "
            cadena = cadena + str(comida) + ": " + str(cantidad)
        return cadena
    


class Animal:
    def __init__(self, id:int, dieta: Edieta, especie: str):
        self.id = id
        self.dieta = dieta
        self.cuidador_actual = None # cardinalidad de 0..1 (opcional) en vez de 1..n
        self.especie = especie

    def get_id(self):
        return str(self.id)
    
    def setCuidador(self, cuidador):
        self.cuidador_actual = cuidador

    def operacion1(self):
        print("operacion1")
        return
    
    def operacion2(self): # placeholder. Está propuesta pero no se ejecuta
        print("operacion2")
        pass

    def __str__(self):
        cadena = str(self.id) + " " + str(self.especie) + " " + str(self.cuidador_actual) + " " + str(self.dieta)
        return cadena

class Vacaciones:
    def __init__(self, empleado:Cuidador, inicio, duracion:int):
        self.empleado = empleado
        self.inicio = inicio
        self.duracion = duracion


class Cuidador:
    def __init__(self, nombre: str, apellido:str, animales: list):
        self.nombre = nombre
        self.apellido = apellido
        self.animales = animales

    def alimentar(self, animal: Animal):
        return f"{self.nombre} ha alimentado al animal {animal.get_id()}"
    
    def solicitar_vacaciones(self, inicio, duracion):
        return Vacaciones(self, inicio, duracion)
    
    def cuidar(self, animal:Animal):
        return f"{self.nombre} ha cuidado al animal {animal.get_id()}"
    
    def __str__(self):
        cadena = ""
        for i in self.animales:
            cadena = cadena + str(i)
        return (self.nombre + " " + self.apellido + " " + cadena)
    


class Zoo:
    def __init__(self, cuidadores: list, animales: list, stock: Stock):
        self.cuidadores = cuidadores
        self.animales = animales
        self.stock = stock

    def cuidar(self, cuidador: Cuidador, animal: Animal):
        return cuidador.cuidar(animal)
    

    def coger_vacaciones(self, cuidador: Cuidador, inicio, duracion:int):
        solicitante = cuidador.solicitar_vacaciones(inicio, duracion)
        return solicitante

######

comidaanimal1 = Comida([Edieta.CARNIVORO])

animal1 = Animal(1, comidaanimal1, "Tigre")
animal2 = Animal(2, "Leon", comidaanimal1)

cuidador1 = Cuidador("Juan", "Abellan", [animal1, animal2])

comidaC = Comida([Edieta.CARNIVORO])
comidaMixta = Comida([Edieta.CARNIVORO, Edieta.HERBIVORO])


stock = Stock({comidaC: 3, comidaMixta: 4})

zoo = Zoo([cuidador1], [animal1, animal2], stock)

for i in zoo.animales:
    print("animales: " + str(i) + "\n")


for i in zoo.cuidadores:
    print("cuidadores: " + str(i))

print("stock" + str(stock))