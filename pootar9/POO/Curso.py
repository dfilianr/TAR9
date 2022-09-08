class Curso():
    def __init__(self,nom,cre,pro):
        self.nombre = nom
        self.creditox = cre
        self.profesion = pro
        self.__imparticion = "Presencial"

    def mostrarDatos(self):
        dat = "Nombre: {} / Créditos: {} / Modo de impartición: {} "
        print(dat.format(self.nombre,self.creditox,self.__imparticion))
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("existe docente asignado")
        else:
            print("No es necesario asignar un docente")

    def __verificarDocente(self):
        print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False
    #toString
    def __str__(self):
        texto = "Nombre: {} - Créditos: {}"
        return texto.format(self.nombre,self.creditox)

# curso1 = Curso("Matemáticas","5","d")
# print(curso1)
# curso1.mostrarDatos()


# curso1 = Curso("Ingeniera","5","d")
# print(curso1.nombre)
