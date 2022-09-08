
class Numeros_Operaciones():
  def __init__(self):
    pass
  
  def ConcatenaciónTodo(self):
    num1=20
    num2=4
    print("Suma:",(num1+num2))
    print("Resta:",(num1-num2))
    print("Multiplicación:",(num1*num2))
    print("División:",(num1/num2))
    print("División Exacta:",(num1//num2))
    print("Potencia:",(num1**num2))

  def Facil(self):
    entero = 23
    decimal = 31.78
    complejo = 12 + 5j
    booleano = True

    print(entero)
    print(decimal)
    print(complejo)
    print(booleano)

obj=Numeros_Operaciones()
obj.ConcatenaciónTodo()
obj.Facil()