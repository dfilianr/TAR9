#Raise: Sirve para lanzar(de forma intencional) excepciones en python

def evaluarNota(nota):
  if nota<0:
    raise ZeroDivisionError("Este mensaje es personalizado")
  elif nota >=16:
    print("Excelente")
  elif nota>=11:
    print("Aprobado")
  else:
    print("Reprobado")

evaluarNota(-1)
print("Este es el fin de mi programa")

def evaluarNota2(nota):
      if nota<0:
        raise ValueError("Valor Incorrecto")
      elif nota >=16:
        print("Excelente")
      elif nota>=11:
        print("Aprobado")
      else:
        print("Reprobado")

evaluarNota2(-1)
print("Este es el fin de mi programa")