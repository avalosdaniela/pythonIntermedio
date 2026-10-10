""" Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario. """

def buscar_palabra(palabra, *lista):
    print(f"\nLa palabra '{palabra}' está en la lista." if palabra in lista else f"\nLa palabra '{palabra}' no está en la lista.")

cantidad = int(input("\nIngrese la cantidad de palabras: "))
lista = []

for i in range(cantidad):
    lista.append(input(f"\nIngrese la palabra N°{i + 1}: "))

palabra = input("\n> Ingrese la palabra a buscar: ")

buscar_palabra(palabra, *lista)