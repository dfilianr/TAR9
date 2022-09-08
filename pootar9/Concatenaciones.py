class Con:
  def concate(self):
    text1="Hola"
    texto2="Mundo"
    textofinal=text1+" "+texto2
    print(textofinal)

    print("El saludo es: %s %s"%(text1,texto2))

    saludoFinal = "Saludo: {0} {1}".format(text1,texto2)
    print(saludoFinal)

    saludoFinal = "Saludo: {1} {0}".format(text1,texto2)
    print(saludoFinal)

    saludoFinal12="Saludo: {x} {y}".format(x=text1,y=texto2)
    print(saludoFinal12)

    saludoFinal12="Saludo: {x} {y}".format(y=text1,x=texto2)
    print(saludoFinal12)