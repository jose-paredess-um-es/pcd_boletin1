from enum import Enum
from abc import ABCMeta, abstractmethod
# Manera de crear una enumeracón
class Conservacion(Enum):
    ESTABLE = 0
    FRESCO = 1
    REFRIGERADO = 2
    CONGELADO = 3
    CONSERVA = 4

class Producto:
    def __init__(self, nombre:str, precio:float, conservacion:Conservacion):
        self.nombre = nombre
        self.precio = precio
        self.conservacion = conservacion
    
    def devuelveDatos(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Conservación: {self.conservacion.name}"
    

class Almacen:
    def __init__(self):
        self.productos = {}

    def cambiarStock(self, producto:Producto, cantidad:int):
        for p in self.productos:
            if (p == nombre):
                self.cantidades[nombre] += cantidad
                return
        self.productos = {**self.productos, **{nombre:stock}}


class Entidad(metaclass = ABCMeta):
    def __init__(self, nombre: str, identificacion_fiscal: int):
        self.nombre = nombre
        self.idfiscal = identificacion_fiscal
    
    @abstractmethod

    def devuelveDatos(self):
        pass


class Ubicacion():
    def __init__(self, direccion, codpostal):
        self.direccion = direccion
        self.codpostal = codpostal

    def devuelveUbicacion(self):
        return "Direccion:" + self.direccion + "CodPostal:" + str(self.codpostal)


class Proveedor(Entidad, Ubicacion):
    def __init__(self, nombre, direccion, codpostal, cif):
        Entidad.__init__(self, nombre, cif)
        Ubicacion.__init__(self, direccion, codpostal)
        self.productos = []

    def devuelveDatos(self):
        return "Nombre" + self.nombre + "CIF:" + str(self.cif) + " " + self.devuelveUbicacion()


    def altaProducto(self, nombre, conservacion, precio):
        for p in self.productos:
            if (p.nombre == nombre):
                print("Producto" + nombre + "ya existe")
                return
        self.productos.append(Producto(nombre, conservacion, precio))

    

class Cliente(Entidad, Ubicacion):
    def __init__(self, nombre, direccion, codpostal, nif):
        Entidad.__init__(self, nombre, nif)
        Ubicacion.__init__(self, direccion, codpostal)
        self.fidelizacion = False
        self.cesta = {}

    def devuelveDatos():
        return "Nombre:" + self.nombre +  "NIF : " + str(self.idfiscal) + " " + self.devuelveUbicacion()

    

class Supermercado(Ubicacion):
    def __init__(self, nombre, direccion, codpostal):
        Ubicacion.__init__(self, direccion, codpostal)
        self.nombre = nombre
        self._almacen = Almacen()
        self._clientes = []
        self._proveedores = []
        self._ventas = 0.0

    def altaCliente(self, nombre, direccion, codpostal, nif):
        for c in self._clientes:
            if (c.nombre == nombre):
                print("Cliente <" + nombre+ "> ya existe")
                return
        self._clientes.append(Cliente(nombre,direccion,codpostal,nif))

    
    def listadoClientes(self):
        print("LISTADO CLIENTES")
        for c in self._clientes:
            print("\t", c.devuelveDatos())
        print ()

    def altaProveedor(self, nombre, direccion, codpostal, cif):
        for p in self._proveedores:
            if (p.nombre == nombre):
                print("Proveedor <" + nombre+ ">  ya exite")
                return
        self._proveedores.append(Proveedor(nombre,direccion, codpostal, cif))


    def listadoProveedores(self):
        print("LISTADO PROVEEDORES")
        for p in self._proveedores:
            print("\t", p.devuelveDatos())
            for d in p.productos:
                print("\t\t", d.devuelveDatos())
        print ()

    
    def altaProducto(self, nombre, proveedor, conservacion, precio, stock):
        for p in self._proveedores:
            if (p.nombre == proveedor):
                p.altaProducto(nombre, conservacion, precio)
                self._almacen.cambiarStock(nombre, stock)
                return
        print("proveedor <"+proveedor+"< no existe")


    
    def listadoProductos(self):
        print("LISTADO PRODUCTOS")
        for p in self._proveedores:
            pass

    def buscaProducto(self, producto):
        for p in self._proveedores:
            for d in p.productos:
                if (d.nombre == producto):
                    return d
        print("Producto <" + producto + "> no existe")



    def ponEncesta(self, cliente, producto, cantidad):
        for c in self._clientes:
            if (c.nombre == cliente):
                c.ponEnCesta(producto, cantidad)
                self._almacen.cambiarStock(producto, -cantidad)
                self.muestraCesta(cliente)
                return
        print("Cliente <" + cliente + "> no existe")

    
    def quitaDeCesta(self, cliente, producto, cantidad):
        for c in self._clientes:
            if (c.nombre == cliente):
                c.quitaDeCesta(producto, cantidad)
                self._almacen.cambiarStock(producto, cantidad)
                self.muestraCesta(cliente)
                return
        print("Cliente >" + cliente + "> no existe")

    
    def muestraCesta(self, cliente):
        for c in self._clientes:
            if (c.nombre == cliente):
                print("Estado de la cesta de: ", cliente)
                total = 0.0
                transporte = 0.0
                for p in c.cesta:
                    prod = self.buscaProducto(p)
                    subtotal = c.cesta[p]*prod.precio
                    total += subtotal
                    if (prod.conservacion == Conservacion.CONGELADO):
                        transporte = 30.0
                    print(" \t Producto: ", p, " Cantidad: ", c.cesta[p], " Suubtotal:", subtotal)
                    print("\t Total: ", total, " Transporte", transporte)
                    print()
                    return
        print("Clientre <" + cliente + "> no existe")


    def finalizaCompra(self, cliente):
        for c in self._clientes:
            if (c.nombre == cliente)
            print("Finalaziada la cocmpra de: ", cliente)
            total = 0.0
            transporte = 0.0
            for p in c.cesta:
                prod = self.buscaProducto(p)
                total += c.cesta[p] * prod.precio
                if (prod.conservacion == Conservacion.CONGELADO):
                    transporte = 30.0
                c.cesta = {}
                self._ventas += total
                print("\t Coste de la cesta: ", total)
                print("\t Coste del transporte: ", transporte)
                print("\t Cantidad total pagada: ", total + transporte)
                print("\t Ingresos totales acumulados: ", self._ventas)
                print ()
                return
        print("Cliente <" + cliente + "> no existe")


        