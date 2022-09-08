class Personas():
    apellidos = ""
    nombres = ""
    edad = 0
    despierta = False

    def despertar(self):
        self.despierta = True
        print("Buen día.")

persona1=Personas()
persona1.apellidos="García Fuentes"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2=Personas()
persona2.apellidos="Paz Torres"
print(persona2.apellidos)
print(persona2.despierta)