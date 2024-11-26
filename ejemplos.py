
def Bienvenido():
    print("Hola eres bienvenido")

Bienvenido()

#segundo ejercicio

print("\n")

#diseña una funcion que sume 2 numeros

def suma(a,b):
    print(f"el resultado de la suma es: {a+b}")

#funcion que divida 2 numeros y retorne el valor 

def dividir(i,j):
    return i/j
print(f"el resultado es: {dividir(20,2)}")
k=dividir(30,10)
print(f"el valor de k es: {k}")

print("\n")
#funcion con parametros arbitrarios

def calcularPromedio(*numeros):
    return sum(numeros)/len(numeros)
print(calcularPromedio(10,20,30))

print("\n 5to ejemplo")
#parametros por defecto
def potencia(base,exponente=2):
    return base**exponente
print(potencia(10,5))
print(potencia(10))

print("\n ejemplo 6")
#crear 3 funciones
#una funcion cargar 2 valores por teclado
#otra funcion que sume
#otra que muestre el resultado

def presentacion():
    print("programa que permite cargar 2 valores por teclado ")
    print("efectua la suma de los valores ")
    print("muestra el resultado de la suma ")
    print("**")

def cargar_suma():
    valor1=int(input("Ingrese el valor 1: "))
    valor2=int(input("Ingrese el valor 2: "))
    print(f"La sumna de estos valores es: {valor1+valor2}")

def finalizar ():
    print("Gracias por utilizar el programa")

presentacion()
cargar_suma()
finalizar()

print("\n ejemplo 7")
#programa que muestre el mayor de 3 numeros
def mayor(v1,v2,v3):
    print("El mayor valor de los 3 es: ")
    if v1>v2 and v1>v3:
        print(v1)
    elif v2>v1 and v2>v3:
        print(v2)
    else:
        print(v3)


def cargarDatos():
    x=int(input("Ingrese valor 1: "))
    y=int(input("Ingrese valor 2: "))
    z=int(input("Ingrese valor 3: "))
    mayor(x,y,z)

cargarDatos()

print("\n ejemplo 8")

#funcion que recibe una lista de numeros y suma todos elemntos de la lista devolviendo el resultado de la suma

def sumar(lista):
    s=0
    for i in lista:
        s=s+i
    return s

def mayorn(lista):
    may=0
    for j in range(len(lista)):
        if may < lista[j]:
            may=lista[j]
    print(f"El mayor valor de la lista es: {may}")





lista1=[15,11,13,18,11,12,9,8,19,6,5,24,3,22,111]
resultado = sumar(lista1)
mayorn(lista1)
print(resultado)