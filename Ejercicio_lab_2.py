#Alejandro Angel Perez    Grupo  3CV5
import os
from math import sqrt 
def Mayusculas():
    print (f"ingrese la cadena")
    cadena = input()
    cadena2 = cadena.upper()
    print (f"Cadena en Mayusculas")
    print(cadena2)

def Cubo():
    print (f"ingrese un numero")
    a = int (input ())
    b = a
    for i in range(1,3):
        b*=a
    print (f"El cubo de {a} es: {b}")

def EcuacionG():
    a = int(input(f"Ingrese el coeficiente de la variable cuadrática: "))
    b = int(input(f"Ingrese el coeficiente de la variable lineal: "))
    c = int(input(f"Ingrese el término independiente: "))
    print (f"Su ecuacion es ({a}x^2)+({b}x)+({c})")
    d = (b*b)-(4*a*c)
    if d<0:
        print(f"La solución de la ecuación es con numeros complejos")
    else:
        sol1 = (-b+sqrt((b*b)-(4*a*c)))/(2*a)
        sol2 = (-b-sqrt((b*b)-(4*a*c)))/(2*a)
        print(f"Las soluciones de la ecuación son:")
        print (f"X1={sol1}")
        print (f"X2={sol2}")

b = 1
while b==1:
    print (f"   Menu")
    print (f"1.- Convertidor a letras mayusculas.")
    print (f"2.- Cubo de un numero.")
    print (f"3.- solucion de ecuacion de segundo grado.")
    print (f"4.- Salir.")
    print (f"Seleccione una opcion")
    a = int(input())
    os.system ("clear")
    if a==1:
        print (f"Seleccione una opcion")
        print (f"1.- Calcular por funcion.")
        print (f"2.- Calcular con lambda.")
        c = int(input())
        if c==1:
            Mayusculas()
        else:
            cad2 = lambda x: x.upper()
            print (f"ingrese la cadena")
            cad1 = input()
            resultado=cad2(cad1)
            print (resultado)
        print (f"Presione enter para continuar")
        d = input()
        os.system ("clear")
    elif a==2:
        print (f"Seleccione una opcion")
        print (f"1.- Calcular por funcion.")
        print (f"2.- Calcular con lambda.")
        c = int(input())
        if c==1:
            Cubo()
        else:
            resultado = lambda x: x*x*x
            print (f"ingrese un numero")
            cub = int (input ())
            res=resultado(cub)
            print(res)
        print (f"Presione enter para continuar")
        d = input()
        os.system ("clear")
    elif a==3:
        print (f"Seleccione una opcion")
        print (f"1.- Calcular por funcion.")
        print (f"2.- Calcular con lambda.")
        c = int(input())
        if c==1:
            EcuacionG()
        else:
            e = int(input(f"Ingrese el coeficiente de la variable cuadrática: "))
            f = int(input(f"Ingrese el coeficiente de la variable lineal: "))
            g = int(input(f"Ingrese el término independiente: "))
            print (f"Su ecuacion es ({e}x^2)+({f}x)+({g})")
            d = (f*f)-(4*e*g)
            if d<0:
                print(f"La solución de la ecuación es con numeros complejos")
            else:
                sol1 = lambda x, y, z: (-y+sqrt((y*y)-(4*x*z)))/(2*x)
                sol2 = lambda x, y, z: (-y-sqrt((y*y)-(4*x*z)))/(2*x)
                print(f"Las soluciones de la ecuación son:")
                resultado=sol1(e,f,g)
                print (f"X1={resultado}")
                resultado=sol2(e,f,g)
                print (f"X2={resultado}")
        print (f"Presione enter para continuar")
        d = input()
        os.system ("clear")
    elif a==4:
        b = 0
    else:
        print(f"El valor no es valido") 
    


