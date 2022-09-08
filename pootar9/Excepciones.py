#Excepcion:Eror en tiempo de ejeccución
#(durante la ejecución del programa)
class Excepciones():
  def elellioles(self):
    numero1=20
    numero2=2

    #print("la division de {} entre {} es: {}".format(numero1,numero2,(numero1/numero2)))

    try:
      resultado = numero1/numero2
      print(resultado)
    except ZeroDivisionError:
      print("No se puede dividir entre cero")
    finally:
      print("yo siempre aparezco")
    print("Aqui termina mi programa.")