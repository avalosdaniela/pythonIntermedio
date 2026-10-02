""" Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario. """

print("--- División ---")
numero1 = int(input("\nIngrese el primer número: "))
numero2 = int(input("\nIngrese el segundo número: "))

try:
    resultado = numero1 / numero2
    print(f"\nEl resultado de {numero1} / {numero2} es: {resultado}")
except ZeroDivisionError:
    print("\nNo se puede dividir por 0. (ZeroDivisionError)")

