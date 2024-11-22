#Parte 1: Declaración Básica de Funciones

def bienvenida(nombre):
    saludo = "Hola " + nombre + " como estas?"
    return saludo
nombre = input("Introduzca su nombre")
print(bienvenida(nombre))

def area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area
   
radio = int(input("Introduzca el radio"))
print("Area =",area_circulo(radio))

#parte2
def descuento(precio,porcentaje):
    descuento = precio * ((100 - porcentaje) / 100)
    return descuento
precio = int(input("Introduzca el precio del producto:"))
porcentaje = int(input("Introduzca el porcentaje de descuento:"))
print(f"Con el {porcentaje}% de descuento el nuevo precio es: ${descuento(precio,porcentaje)} pesos COP")

#parte3
def mayor_valor(*num):
    mayor = max(num)
    return mayor
print(f"El numero mayor es {mayor_valor(2, 4, 5, 6, 70, 5)}")

#parte4
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

