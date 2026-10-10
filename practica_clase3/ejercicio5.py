""" Imprimir un mensaje de error si no se pasan suficientes argumentos. """

def sumar_numeros(*lista):
    try:
        suma = lista[0] + lista[1]
    except IndexError:
        print("\nNecesita ingresar al menos 2 números para poder sumarlos.")
    else:
        for numero in lista[2:]:
            suma += numero
        print(f"\n> La suma de los números es: {suma}")

cantidad = int(input("\nIngrese la cantidad de números: "))
lista = []

for i in range(cantidad):
    lista.append(int(input(f"\nIngrese el número N°{i + 1}: ")))

sumar_numeros(*lista)