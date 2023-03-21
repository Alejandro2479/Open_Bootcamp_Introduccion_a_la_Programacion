class Persona:
    def __init__(self, edad, nombre, telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono

class Cliente(Persona):
    def __init__(self, edad, nombre, telefono, credito):
        super().__init__(edad, nombre, telefono)
        self.credito = credito

class Trabajador(Persona):
    def __init__(self, edad, nombre, telefono, salario):
        super().__init__(edad, nombre, telefono)
        self.salario = salario

# Creando objeto cliente
cliente = Cliente(30, "Juan", "555-1234", 5000)
print("Cliente:")
print("Edad:", cliente.edad)
print("Nombre:", cliente.nombre)
print("Teléfono:", cliente.telefono)
print("Crédito:", cliente.credito)

# Creando objeto trabajador
trabajador = Trabajador(25, "María", "555-4321", 25000)
print("Trabajador:")
print("Edad:", trabajador.edad)
print("Nombre:", trabajador.nombre)
print("Teléfono:", trabajador.telefono)
print("Salario:", trabajador.salario)
