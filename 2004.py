from collections import Counter

# Creamos una lista de strings
lista_strings = ['Chile verde', 'Perejil', 'Naranja', 'Maiz grano', 'Sorgo escobero', 'Mango' ,'Maiz grano', 
'Avena forrajera achicalada', 'Maiz forrajero en verde', 'Frijol', 
'Maiz grano', 'Aguacate', 'Trigo grano', 'Maiz grano', 'Maiz grano', 'Hortalizas',
'Haba verde', 'Cafe cereza', 'Pastos y praderas', 'Cafe cereza', 'Col',
'Avena forrajera en verde', 'Chile verde', 'Pastos y praderas achicalado',
'Pastos y praderas seco', 'Sorgo forrajero en verde', 'Frijol', 
'Sorgo grano', 'Maiz grano', 'Cafe cereza', 'Naranja', 'Chile seco']

# Contamos la cantidad de ocurrencias de cada elemento
contador = Counter(lista_strings)

# Obtenemos el elemento más común y su cantidad de ocurrencias
valor_mas_comun, cantidad = contador.most_common(1)[0]

# Imprimimos el resultado
print(f"El valor más repetitivo es '{valor_mas_comun}', con un total de {cantidad} ocurrencias.")

