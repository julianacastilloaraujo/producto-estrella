from collections import Counter

# Creamos una lista de strings
lista_strings = ['Maiz grano', 'Algodon hueso', 'Tomate verde', 'Naranja',
'Sorgo escobero', 'Papaya', 'Cafe cereza', 'Alfalfa achicalada', 'Frijol',
'Maiz grano', 'Maiz grano', 'Maiz grano', 'Naranja', 'Avena forrajera en verde', 'Alfalfa verde',
'Sorgo grano', 'Maiz grano', 'Cafe cereza', 'Pastos y praderas', 'Trigo grano',
'Cacahuate', 'Alfafa verde', 'Naranja', 'Maiz grano',
'Cebolla', 'Arroz palay', 'Naranja', 'Maiz grano', 'Cafe cereza', 'Maiz grano', 'Frijol']

# Contamos la cantidad de ocurrencias de cada elemento
contador = Counter(lista_strings)

# Obtenemos el elemento más común y su cantidad de ocurrencias
valor_mas_comun, cantidad = contador.most_common(1)[0]

# Imprimimos el resultado
print(f"El valor más repetitivo es '{valor_mas_comun}', con un total de {cantidad} ocurrencias.")


