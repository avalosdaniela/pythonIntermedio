""" Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario. """

print("--- División ---")
try:
    numero1 = int(input("\nIngrese el primer número: "))
    numero2 = int(input("\nIngrese el segundo número: "))

    resultado = numero1 / numero2

    print(f"\nEl resultado de {numero1} / {numero2} es: {resultado}")
except ZeroDivisionError:
    print("\nNo se puede dividir por 0. (ZeroDivisionError)")
except ValueError:
    print("\nNo ingresaste un número válido. (ValueError)")