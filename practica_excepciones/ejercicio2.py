""" Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario. """

numero = 6
texto = "hola"

try: 
    resultado = numero + texto
    print("El resultado es: ", resultado)

except TypeError:
    print("No se puede sumar una cadena de texto con un número. (TypeError)")