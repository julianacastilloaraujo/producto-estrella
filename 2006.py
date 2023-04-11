from collections import Counter

# Creamos una lista de strings
lista_strings = ['Avena forrajera en verde', 'Sorgo forrajero en verde', 'Sorgo grano', 'Maiz grano', 'Nuez', 'Maiz forrajero en verde',
'Maiz grano', 'Chile verde', 'Verdolaga', 'Maiz grano', 'Cafe cereza', 'Maiz grano', 'Maiz grano', 'Avena forrajera en verde', 'Sorgo grano',
'Cafe cereza', 'Naranja', 'Maiz grano', 'Maiz grano', 'Alfalfa verde', 'Frijol', 'Pastos y praderas achicalado', 'Elote', 'Trigo grano', 'Sandia',
'Okra', 'Maiz grano', 'Frijol', 'Pastos y praderas', 'Sorgo forrajero en verde']

# Contamos la cantidad de ocurrencias de cada elemento
contador = Counter(lista_strings)

# Obtenemos el elemento más común y su cantidad de ocurrencias
valor_mas_comun, cantidad = contador.most_common(1)[0]

# Imprimimos el resultado
print(f"El valor más repetitivo es '{valor_mas_comun}', con un total de {cantidad} ocurrencias.")

