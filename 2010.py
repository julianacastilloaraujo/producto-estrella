from collections import Counter

# Creamos una lista de strings
lista_strings = ['Maiz grano', 'Naranja', 'Maiz grano', 'Maiz grano', 'Avena forrajera en verde', 
'Papaya', 'Frijol', 'Maiz grano', 'Frijol', 'Maiz grano', 'Frijol',
'Limon', 'Col', 'Mango', 'Maiz grano', 'Maiz forrajero seco', 'Maiz grano', 'Alfalfa verde'
'Calabacita', 'Pastos y praderas', 'Pastos y praderas', 'Cafe cereza',
'Maiz grano', 'Frijol', 'Chile verde', 'Maiz grano', 'Tomate verde', 'Cebolla', 'Frijol',
'Naranja', 'Trigo grano', 'Cafe cereza', 'Henequen', 'Frijol']

# Contamos la cantidad de ocurrencias de cada elemento
contador = Counter(lista_strings)

# Obtenemos el elemento más común y su cantidad de ocurrencias
valor_mas_comun, cantidad = contador.most_common(1)[0]

# Imprimimos el resultado
print(f"El valor más repetitivo es '{valor_mas_comun}', con un total de {cantidad} ocurrencias.")



