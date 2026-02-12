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
            cadena += cadena + str(i)
        return cadena
    

class Stock:
    def __init__(self, comida: dict):
        self.comida = comida
    
    def sacar(self, comida, cantidad):
        self.comida[comida] -= cantidad

    def reponer(self, comida, cantidad):
        self.comida[comida] -= cantidad





class Animal:
    def __init__(self, id:int, dieta: Edieta, cuidador_act: Cuidador, especie: str)
        self.id = id
        self.dieta = dieta
        self.cuidador = cuidador_act
        self.especie = especie

    def get_id(self):
        return str(self.id)

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

