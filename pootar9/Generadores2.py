def devuelveLenguajes(*lenguajes):
  for leng in lenguajes:
    yield leng
        
lennguajesObtenidos=devuelveLenguajes("Python","Java","PHP","Ruby","JavaScript")
print(next(lennguajesObtenidos))
print(next(lennguajesObtenidos))


def devuelveLenguajes(*lenguajes):
  for leng in lenguajes:
    for letra in leng:
      yield letra
lennguajesObtenidos=devuelveLenguajes("Python","Java","PHP","Ruby","JavaScript")
print(next(lennguajesObtenidos))
print(next(lennguajesObtenidos))

def devuelveLenguajes(*lenguajes):
  for leng in lenguajes:
      yield from leng
lennguajesObtenidos=devuelveLenguajes("Python","Java","PHP","Ruby","JavaScript")
print(next(lennguajesObtenidos))
print(next(lennguajesObtenidos))
      
      