class Cadenas():
    def lalo(self):
        text = "Bienvenidos al canal de UskokruM2010"
        print(text)
        print(text.lower())
        print(text.upper())
        print(text.title())
        print(text.find("al"))#Posicion donde se encuentra
        print(text.count("e"))#Cantidad eque se repite

        textoFinal = text.replace("e","3")
        print(textoFinal)

        valor = text.isnumeric()
        print(valor)

        cadenaSeparada = text.split(" ")
        print(cadenaSeparada)