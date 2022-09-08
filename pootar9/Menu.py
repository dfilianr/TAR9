from Funciones import Funciones
from POO.Persona import Personas
from borrar import borrarPantalla
from Helpers import Helper
from Numeros_Operaciones import Numeros_Operaciones
from Concatenaciones import Con
from Cadenas import Cadenas
from Tuplas import Tuplas
from Listas import Listas
from Diccionarios import Diccionarios
from if_else import If
from OperadoresLogicos import Operadores_Logicos
from OperadorTernario import OperadoresTernarios
from Range import Range
from For import For
from if_In import IfIn
from Factorial import Factorial
from whhile import Whhile
from Break_Continue_Pass import Breakk
from Generadores import *
from Excepciones import Excepciones
from Módulo.funcionesMatematicas import *
from Paquete1.funcionesCadenas import *
from Paquete1.funcionesNumericas import *
from POO.Curso import Curso
from POO.Cuenta import Cuenta
from POO.Herencia import *
from POO.HerenciaMultiple import ClaseA,ClaseB,ClaseX
from POO.Polimorfismo import *
from POO.RelacionesClases import *

import os
helper = Helper()
lista=["1) Hola Mundo","2) Variables","3) Conversiones","4) Numeros y Operaciones Matemáticas","5) Concatenación","6) Funciones De Cadenas",
       "7) Tuplas","8) Listas","9) Diccionarios","10) Condición If","11) Funciones","12) Operadores Lógicos","13) Operadores Ternarios",
       "14) Range","15) For","16) If in","17) Factorial","18) While","19) Break y Continue","20) Generadores ","21) Generadores 2","22) Excepciones",
       "23) Raise","24) Modulos","25) Paquete 1","26) Persona","27) Curso","28) Cuenta","29) Herencia","30) Herencia Múltiple","31) Polimorfismo",
       "32) Relaciones Entre Clases","33) Salir"]
opcion=""
while opcion != "33":
  borrarPantalla()
  opcion = helper.menu(lista,"Menu Principal")
  borrarPantalla()
  if opcion == "1":
      print("*" * 20, "Hola Mundo", "*" * 20)
      print("Hola Mundo")
      input("presiona cualquier tecla para regresar")
      borrarPantalla()

  if opcion == "2":
    print("*"*20,"Tipos De Variables","*"*20)
    nombre = "UskoKruM2010"
    print("{} es una variable tipo char".format(nombre))
    edad = 25
    print("{} es una variable tipo entero".format(edad))
    edad = True
    print("{} es una variable tipo Booleano".format(edad))
    sueldo = 205.10
    print("{} es una variable tipo sueldo".format(sueldo))
    input("presiona cualquier tecla para regresar")
    borrarPantalla()
    os.system("clear")

  if opcion == "3":
    print("*" * 20, "Conversiones", "*" * 20)
    numero1 = "35"
    numero2 = "18"
    print("la concatenación de {} y {} es: {}".format(numero1,numero2,(numero1 + numero2)))

    num1 = int(numero1)
    num2 = int(numero2)
    print("la suma de {} + {} es: {}".format(numero1,numero2,(num1 + num2)))

    sueldo = 1200.43
    sueldoEntero = int(sueldo)
    print("El sueldo entero es de:",sueldoEntero)

    valor = "4500.89"
    valorDecimal = float(valor)
    print("El valor decimal es de:",valorDecimal * 3)

    edad = 100
    print("los digitos que tiene {} son: {}".format(edad,len(str(edad))))

    for i in range(5):
      print("Un arbolito",(i + 1) * "* ")
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "4":
    print("*"*20,"Numeros y Operaciones Matemáticas","*"*20)
    obj = Numeros_Operaciones()
    obj.ConcatenaciónTodo()
    obj.Facil()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "5":
    print("*" * 20, "Concatenaciones", "*" * 20)
    obj = Con()
    obj.concate()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "6":
    print("*" * 20, "Funciones De Cadenas", "*" * 20)
    obj = Cadenas()
    obj.lalo()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "7":
    print("*" * 20, "Tuplas", "*" * 20)
    obj = Tuplas()
    obj.lula()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "8":
    print("*" * 20, "Listas", "*" * 20)
    obj = Listas()
    obj.lila()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "9":
    print("*" * 20, "Diccionarios", "*" * 20)
    obj = Diccionarios()
    obj.lilionarios()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "10":
    print("*" * 20, "Funciones If", "*" * 20)
    obj = If()
    obj.il()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "11":
    print("*" * 20, "Funciones", "*" * 20)
    obj = Funciones()
    obj.saludar()
    sueldo = int(input("Ingrese un sueldo: "))
    obj.evaluaSueldoMinimo(sueldo)
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "12":
    print("*" * 20, "Operadores Lógicos", "*" * 20)
    obj = Operadores_Logicos()
    obj.oleladoles()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "13":
    print("*" * 20, "Operadores Ternarios", "*" * 20)
    obj = OperadoresTernarios()
    obj.lelnarios()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "14":
    print("*" * 20, "Range", "*" * 20)
    obj = Range()
    obj.lanle()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "15":
    print("*" * 20, "For", "*" * 20)
    obj = For()
    obj.lol()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "16":
    print("*" * 20, "If in", "*" * 20)
    obj = IfIn()
    obj.lil()
    input("presiona cualquier tecla para regresar: ")
    borrarPantalla()

  if opcion == "17":
    print("*" * 20, "Factorial", "*" * 20)
    obj = Factorial()
    obj.lallolial()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "18":
    print("*" * 20, "While", "*" * 20)
    obj = Whhile()
    obj.lile()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "19":
    print("*" * 20, "Break y Continue", "*" * 20)
    obj = Breakk()
    obj.leall()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "20":
    print("*" * 20, "Generadores", "*" * 20)
    limite=int(input("Ingrese limite: "))
    print(GeneraMultiplos7(limite))
    print(generadorMultiplo7(limite))
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "21":
    print("*" * 20, "Generadores 2", "*" * 20)

    def devuelveLenguajes(*lenguajes):
      for leng in lenguajes:
        yield leng

    lennguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
    print(next(lennguajesObtenidos))
    print(next(lennguajesObtenidos))

    def devuelveLenguajes(*lenguajes):
      for leng in lenguajes:
        for letra in leng:
          yield letra

    lennguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
    print(next(lennguajesObtenidos))
    print(next(lennguajesObtenidos))

    def devuelveLenguajes(*lenguajes):
      for leng in lenguajes:
        yield from leng

    lennguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
    print(next(lennguajesObtenidos))
    print(next(lennguajesObtenidos))
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "22":
    print("*" * 20, "Excepciones", "*" * 20)
    obj = Excepciones()
    obj.elellioles()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "23":
    print("*" * 20, "Raise", "*" * 20)

    def evaluarNota(nota):
      if nota < 0:
        raise ZeroDivisionError("Este mensaje es personalizado")
      elif nota >= 16:
        print("Excelente")
      elif nota >= 11:
        print("Aprobado")
      else:
        print("Reprobado")

    evaluarNota(30)
    print("Este es el fin de mi programa")

    def evaluarNota2(nota):
      if nota < 0:
        raise ValueError("Valor Incorrecto")
      elif nota >= 16:
        print("Excelente")
      elif nota >= 11:
        print("Aprobado")
      else:
        print("Reprobado")

    evaluarNota2(40)
    print("Este es el fin de mi programa")
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "24":
    print("*" * 20, "Modulos", "*" * 20)
    print(sumar(5,6))
    print(multiplicar(5,6))
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "25":
    print("*" * 20, "Paquete 1", "*" * 20)
    print(multiplicar(5,6))
    print(potenciar(6,8))
    print(contarLetras("lalito"))
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "26":
    print("*" * 20, "Persona", "*" * 20)
    obj = Personas()
    obj.despertar()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "27":
    print("*" * 20, "Curso", "*" * 20)
    obj = Curso("Matemáticas","5","d")
    obj.mostrarDatos()
    input("presiona cualquier tecla para regresar")
    borrarPantalla()

  if opcion == "28":
      print("*" * 20, "Cuenta", "*" * 20)
      obj = Cuenta("Oscar García",15000,"Soles")
      print(obj.get_Saldo())
      print(obj.get_Propietario())
      print(obj.get_Moneda())
      input("presiona cualquier tecla para regresar")
      borrarPantalla()


  if opcion == "29":
      print("*" * 20, "Herencia", "*" * 20)
      obj = Persona("Torres", "López", "Juan")
      obj.mostrarNombreCompleto()
      obj.datos()
      obj1 = Estudiante()
      input("presiona cualquier tecla para regresar")
      borrarPantalla()

  if opcion == "30":
      print("*" * 20, "Herencia Múltiple", "*" * 20)
      obj = ClaseA("y","x")
      obj1 = ClaseB(12,13,14)
      obj2 = ClaseX(15,21)
      print(obj)
      print(obj1)
      print(obj2)
      input("presiona cualquier tecla para regresar")
      borrarPantalla()

  if opcion == "31":
      print("*" * 20, "Polimorfismo", "*" * 20)
      obj = Estudiante()
      obj.describir()
      obj1 = Docente()
      obj1.describir()
      obj2 = Trabajador()
      print(describirPersona(doc1))
      input("presiona cualquier tecla para regresar")
      borrarPantalla()

  if opcion == "32":
      print("*" * 20, "Relaciones Entre Clases", "*" * 20)
      obj = Pais("Perú", "Martín Vizcarra")
      obj1 = Ciudad("Chiclayo", 150000, pais1)
      obj2 = Urbanizacion("María de los Angeles", ciudad1)
      print(pais1)
      print(ciudad1)
      print(urba1)
      input("presiona cualquier tecla para regresar")
      borrarPantalla()


















