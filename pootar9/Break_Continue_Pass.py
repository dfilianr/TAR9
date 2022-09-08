from ast import Pass
class Breakk():
  def leall(self):

    for numero in range(1,6):
      if numero == 3:
        break
      print("El número es : {}".format(numero))
    print("Bucle terminado")

    #Continue: Omite una parte del bucle cuando se cumple
    #una condición y contnua el resto

    for numero in range(1,6):
      if numero == 3:
        continue
      print("El número es : {}".format(numero))
    print("Bucle terminado")

    #Pass: Permite continuar con una sentnecia o función
    #que ya no tiene o aún no tiene un bloque de codigo util

    for numero in range(1,6):
      if numero <= 3:
        Pass
      else:
        print("El siguiente valor es mayor a 3: ")
      print("El número es : {}".format(numero))
    print("Bucle terminado")

    def funcionSinImplementar():
      pass

