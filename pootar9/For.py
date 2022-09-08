class For():
  def lol(self):

    for num in range(0,20,2):
      print("Valor actual: {}".format(num))

    for i in range(1,13):
      print("{} * {} es: {}".format(i,i,(i * i)))

    for nom in ["Karen","Oscar","Héctor","Leonardo"]:
      print("Cantidad de letras de {0} es: {1}".format(nom,len(nom)))