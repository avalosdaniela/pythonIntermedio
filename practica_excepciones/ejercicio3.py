""" Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra """

pokemon = {"nombre": "Jigglypuff", "tipo": "Hada", "evolucion": 2}

try:
    print(pokemon["nivel"])
except KeyError:
    print("No existe nivel en el diccionario. (KeyError)")