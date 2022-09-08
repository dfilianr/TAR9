class Operadores_Logicos():
  def oleladoles(self):
    distancia=400
    numeroHermanos = 3
    salarioPadres=3000

    tineBeneficios = False

    if (distancia>1000 and numeroHermanos > 2) or salarioPadres < 2000:
      tineBeneficios = True

    print(not(tineBeneficios))

    if (5>3) and (8<15):
      print("Verdad")
    else:
      print("Es mentira...")

    if (5>3) or (8<15):
      print("Verdad")
    else:
      print("Es mentira...")