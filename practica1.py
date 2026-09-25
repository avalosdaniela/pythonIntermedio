conjuntoA = {1, 6, 9, 2, 7}
conjuntoB = {2, 3, 6, 5, 4, 8}

""" 1. Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos. """

# Unión entre el conjunto A y B

print(conjuntoA | conjuntoB)


""" 2. Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B """

# Intersección entre el conjunto A y B

print(conjuntoA & conjuntoB)


""" 3. Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos. """

# Diferencia simétrica entre el conjunto A y B

print(conjuntoA.symmetric_difference(conjuntoB))


""" 4. Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B. """

# Verifica si A es subconjunto de B

print(conjuntoA.issubset(conjuntoB))


""" 5. Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto. """

# Cantidad de elementos del conjunto A

print(len(conjuntoA))
