class persona():
    nombre= ""
    edad=""
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def print_informacion(self):
        print(self.nombre)
        print(self.edad)

class alumno(persona):
    calificacion=""
    def __init__(self, nombre, edad, calificacion):
        super().__init__(nombre, edad)
        self.calificacion = calificacion
    def print_informacion(self):
        super().print_informacion()
        print(self.calificacion)
paola = alumno('paola', 27, 5)
paola.print_informacion()

class empleado(persona):
    sueldo=""
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def print_informacion(self):
        super().print_informacion()
        print(self.sueldo)
paola = empleado('paola', 27, 20000)
paola.print_informacion()