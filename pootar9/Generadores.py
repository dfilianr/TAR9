#Generadores: Permite extraer valores de una funcion
# y almacenarlos (de uno en uno) en objetos iterables(que se puedan recorrer)
#sin la necesidad de almacenar Todos A La Vez en la memoria Ram

def GeneraMultiplos7(limite):
  numero=1
  listaNumero=[]

  while numero <= limite:
    listaNumero.append(numero*7)
    numero=numero +1
  return listaNumero
print(GeneraMultiplos7(10))

def generadorMultiplo7(limite):
  numero=1
  while numero <=limite:
    yield numero * 7
    numero = numero + 1

obtieneMultiplo7=generadorMultiplo7(10)
#print(obtieneMultiplo7)
# for n in obtieneMultiplo7:
  # print(n)

#next():Retorna el sgte elemento de un objeto iterable

print(next(obtieneMultiplo7))
print("Acá hay 300 líneas de código...")
print(next(obtieneMultiplo7))
print("Acá hay 3000 líneas de código...")
print(next(obtieneMultiplo7))

