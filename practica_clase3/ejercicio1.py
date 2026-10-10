""" Calcular el mayor de dos números ingresados por teclado usando un operador
ternario. """

numero1 = int(input("\nIngrese el primer número: "))
numero2 = int(input("\nIngrese el segundo número: "))

print("\nEl mayor número es:", numero1 if numero1 > numero2 else numero2)