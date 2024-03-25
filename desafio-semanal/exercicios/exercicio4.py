# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

frutas = ['Banana', 'Maçã', 'Pera', 'Banana', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera']

dic_frutas = {}

for fruta in frutas:
  if fruta in dic_frutas:
    dic_frutas[fruta] += 1
  else:
    dic_frutas[fruta] = 1

print(dic_frutas)