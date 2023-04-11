from collections import Counter

# Creamos una lista de strings
lista_strings = ['Tuna', 'Pastos y praderas seco', 'Tomate rojo', 'Naranja', 'Avena forrajera en verde', 'Papaya',
'Maiz grano', 'Alfalfa achicalada', 'Maiz forrajero en verde', 'Alfalfa verde', 'Maiz grano', 'Maiz grano', 'Cafe cereza', 'Sorgo grano', 'Pastos y praderas',
'Maiz grano', 'Sorgo grano', 'Maiz grano', 'Pastos y praderas', 'Maiz grano', 'Cacahuate', 'Frijol', 'Naranja', 'Maiz grano', 'Sorgo grano', 'Cartamo', 'Arroz palay', 'Maiz grano', 'Maiz grano', 'Cafe cereza',
'Pastos y praderas', 'Manzana']

# Contamos la cantidad de ocurrencias de cada elemento
contador = Counter(lista_strings)

# Obtenemos el elemento más común y su cantidad de ocurrencias
valor_mas_comun, cantidad = contador.most_common(1)[0]

# Imprimimos el resultado
print(f"El valor más repetitivo es '{valor_mas_comun}', con un total de {cantidad} ocurrencias.")



