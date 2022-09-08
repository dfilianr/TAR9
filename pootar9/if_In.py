class IfIn():
  def lil(self):

    print("--Cursos--")
    print("Matemática - Biologia - Lenguaje - Ciencias")

    curso = input("Ingrese el curso deseado")

    if curso in ("Matemática - Biologia - Lenguaje - Ciencias"):
      print("Curso {0} seleccionado.".format(curso))
    else:
      print("No existe ese curso:")
