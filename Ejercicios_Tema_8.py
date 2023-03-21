class Persona:
    def __init__(self):
        self.__edad = 0
        self.__nombre = ""
        self.__telefono = ""
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self, telefono):
        self.__telefono = telefono

# Creando objeto persona
persona = Persona()

# Asignando valores a las propiedades usando los setters
persona.set_edad(25)
persona.set_nombre("Juan")
persona.set_telefono("555-1234")

# Mostrando los valores de las propiedades usando los getters
print("Edad:", persona.get_edad())
print("Nombre:", persona.get_nombre())
print("Teléfono:", persona.get_telefono())
