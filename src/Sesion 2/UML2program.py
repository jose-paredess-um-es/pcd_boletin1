class Vehiculo:
    def __init__(self, vehiculo_id, modelo, año, tarifa_diaria):
        self.vehicle_id  = vehiculo_id
        self.modelo = modelo
        self.año = año
        self.tarifa_diaria = tarifa_diaria
        self.is_avaliable = True

    def alquiler(self):
        self.is_avaliable = False

    def return_vehicle(self):
        self.is_avaliable = True

    def calcular_costo_alquiler(self, dias):
        return self.tarifa_diaria*dias
    

class Bicicleta(Vehiculo):
    def __init__(self, vehiculo_id, modelo, año, tarifa_diaria, numero_cambios):
        super().__init__(vehiculo_id, modelo, año, tarifa_diaria)
        self.num_cambios = numero_cambios

    def getNum_cambios(self):
        return self.num_cambios 
    



class Coche(Vehiculo):
    def __init__(self, vehiculo_id, modelo, año, tarifa_diaria, num_puertas):
        super().__init__(vehiculo_id, modelo, año, tarifa_diaria)
        self.num_puertas = num_puertas

    def getNum_puertas(self):
        return self.num_puertas


class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.vehiculos_alquilados = []
    
    def alquiler_vehiculo(self, vehiculo, dias):
        vehiculo.alquiler()
        self.vehiculos_alquilados.append((vehiculo, dias))
    

    def getVehiculos(self):
        return self.vehiculos_alquilados
    
    def return_vehicle(self, vehiculo):
        vehiculo.return_vehicle()

        temp = []
        for (v,d) in self.vehiculos_alquilados:
            if (v != vehiculo):
                temp.append((v,d))
            else:
                print("encontrado: " + str(v.modelo) + "igual a " + str(vehiculo.modelo))
        
        self.vehiculos_alquilados = temp

    def alquiler(self, vehiculo, dias):
        print("El usuario", self.nombre, "ha alquilado el vehiculo", vehiculo.vehicle_id, "un número de", dias, "dias")

    

class Agencia_Alquiler:
    def __init__(self):
        self.vehiculos = []
        self.clientes = []

    def add_vehicle(self, vehiculo):
        self.vehiculos.append(vehiculo)
       
    def add_customer(self, cliente):
        self.clientes.append(cliente)


agencia_alquiler = Agencia_Alquiler()

coche1 = Coche(1, "Toyota", 2022, 30.0, 4)
coche2 = Coche(2, "Audi", 2024, 35.0, 4)

bicicleta1 = Bicicleta(3, "Montaña", 2020, 15.0, 21)
bicicleta2 = Bicicleta(3, "Carretera", 2021, 18.0, 18)

agencia_alquiler.add_vehicle(coche1)
agencia_alquiler.add_vehicle(coche2)
agencia_alquiler.add_vehicle(bicicleta1)
agencia_alquiler.add_vehicle(bicicleta2)

cliente1 = Cliente(101, "Alicia", "Martinez")
cliente2 = Cliente(102, "Bob", "Marley")

agencia_alquiler.add_customer(cliente1)

agencia_alquiler.add_customer(cliente2)

cliente1.alquiler_vehiculo(coche1, 3)

cliente2.alquiler_vehiculo(bicicleta1, 2)


for (v, d) in cliente1.getVehiculos():
	if (isinstance(v, Bicicleta)):
		print("Cliente " + cliente1.nombre + " ha alquilado bicicleta: " + v.modelo + " durante " + str(d))
	if (isinstance(v, Coche)):
		print("Cliente " + cliente1.nombre + " ha alquilado coche: " + v.modelo + " durante " + str(d))
	else:
		("tipo " + str(type(v)))

cliente1.return_vehicle(coche1)

for v in agencia_alquiler.vehiculos:
	if (isinstance(v, Bicicleta)):
		print("bicicleta " + v.modelo + " num cambios " + str(v.getNum_cambios()))
	if (isinstance(v, Coche)):
		print("coche " + v.modelo + " num puertas " + str(v.getNum_puertas()))