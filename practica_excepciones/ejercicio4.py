""" Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe """

nombre_archivo = "olivia.txt"

try:
    archivo = open(nombre_archivo, "r")
    print(archivo.read())
    archivo.close()
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no existe. (FileNotFoundError)")
    try:
        archivo = open(nombre_archivo, "w")
        archivo.close()
        print(f"\n> Se creó el archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"\n> No se pudo crear el archivo: {e}")
else:
    print(f"> El archivo '{nombre_archivo}' ya existe")