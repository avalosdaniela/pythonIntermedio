""" Calcular el promedio de una lista de números usando args y un operador ternario. """

def calcular_promedio(*lista):
    suma = 0
    contador = 0
    for numero in lista:
        suma += numero
        contador += 1
    print(f"\nEl promedio es: {suma / contador}" if contador > 0 else "\nNo se puede calcular el promedio porque no ingresaron números.")

cantidad = int(input("\nIngrese la cantidad de números: "))
lista = []

for i in range(cantidad):
    lista.append(float(input(f"\nIngrese el número N°{i + 1}: ")))

calcular_promedio(*lista)