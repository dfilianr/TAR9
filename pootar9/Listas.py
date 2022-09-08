class Listas():
    def lila(self):
        lista1=["Oscar",25,98.3,True,"Flavio",56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])

        lista1.append("UskoKruM2010")
        print(lista1)

        lista1.insert(4,"Perú")
        print(lista1)

        lista1.extend(["Alejandro",110,False])
        print(lista1)

        print("La palabra Flavio está en la posición {}".format(lista1.index("Flavio")))

        lista1.remove(56.3)
        print(lista1)

        lista1.pop()#elimina el último
        print(lista1)

        lista2 = ["Chiclayo","Irma"]
        lista3 = lista1 + lista2
        print(lista3)

        print(lista2 * 4 )

        print("UskoKruM20224410" in lista1)