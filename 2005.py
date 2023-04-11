from collections import Counter

# Creamos una lista de strings
lista_strings = ['Sorgo forrajero en verde', 'Pastos y praderas', 'Chilce verde', 'Maranon', 'Mqia grano',
 'Sorgo grano', 'Sorgo forrajero en verde', 'Maiz grano', 'Nuez', 'Chapulin', 
 'Maiz grano', 'Garbanzo forrajero', 'Maiz grano', 'Cafe cereza', 'Pastos y praderas', 'Pastos y praderas', 'Maiz grano', 'Sorgo grano', 
 'Cafe cereza', 'Pastos y praderas', 'Pastos y praderas', 'Maiz grano', 'Sorgo grano', 'Cafe cereza', 'Pastos y praderas'
 'Maiz grano', 'Maiz grano', 'Maiz grano', 'Elote', 'Pastos y pradera achicalado', 
 'Trigo grano', 'Cartamo', 'Naranja', 'Sorgo grano', 'Maiz grano', 'Maiz grano',
 'Pastos y praderas', 'Frijol']

# Contamos la cantidad de ocurrencias de cada elemento
contador = Counter(lista_strings)

# Obtenemos el elemento más común y su cantidad de ocurrencias
valor_mas_comun, cantidad = contador.most_common(1)[0]

# Imprimimos el resultado
print(f"El valor más repetitivo es '{valor_mas_comun}', con un total de {cantidad} ocurrencias.")

