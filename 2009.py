from collections import Counter

# Creamos una lista de strings
lista_strings = ['Maiz forrajero en verde', 'Tomate rojo', 'Elote', 'Maiz grano', 'Sorgo forrajero en verde',
'Cana de azucar', 'Frijol', 'Alfalfa achicalada', 'Frijol', 'Avena grano', 'Maiz grano', 'Maiz grano', 'Naranja', 'Maiz forrajero seco', 'Maiz grano', 'Fresa',
'Elote', 'Pastos y praderas', 'Pastos y praderas', 'Maiz grano', 'Maiz grano', 'Frijol', 'Maiz grano', 'Mandarina', 'Maiz grano', 'Nuez',
'Naranja', 'Maiz grano', 'Maiz grano', 'Cafe cereza', 'Pastos y praderas', 'Maiz grano']

# Contamos la cantidad de ocurrencias de cada elemento
contador = Counter(lista_strings)

# Obtenemos el elemento más común y su cantidad de ocurrencias
valor_mas_comun, cantidad = contador.most_common(1)[0]

# Imprimimos el resultado
print(f"El valor más repetitivo es '{valor_mas_comun}', con un total de {cantidad} ocurrencias.")


