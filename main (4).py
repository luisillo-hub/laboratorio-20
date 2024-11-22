#Escribir un programa que defina por asignación una lista de 6 enteros en el bloque
#principal del programa. Elaborar tres funciones, la primera recibe la lista y retorna la
#suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la
#última recibe la lista y retorna el menor

def mayor(lista):
    mayor = lista[0]
    for numero in lista: 
        if numero > mayor:
            mayor = numero
    return mayor
def menor(lista):
    menor = lista[0]
    for numero in lista: 
        if numero < menor:
            menor = numero
    return menor
def suma(lista):
    suma = 0
    for numero in lista: 
            suma = numero + suma
    return suma
numeros = [2, 0, 1]
print("Mayor:",mayor(numeros))
print("Menor:",menor(numeros))
print("Suma:",suma(numeros))