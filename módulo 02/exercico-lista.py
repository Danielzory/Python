#Listas

#operações básicas com listas

"""
Adicionar Elementos: append(), inset()
Remover elementos: remove(), pop()
Concatenar listas: +, extend()
Repetir listas: *
Verificar se um item existe na lista: in
"""

#Adicionar elementos

frutas = ['maça', 'banana']

frutas.append('manga') #adiciona no final

print(frutas)

frutas.insert(1, 'abacaxi') #adiciona em um local específico

print(frutas)

#remover elementos

frutas.remove('abacaxi') #remove o primeiro item da lista que tem o valor especificado

print(frutas)

frutas.pop(0) #remove elementos de acordo com o indice ou ultimo item...

print(frutas)

#Concatenar listas

impares = [ 1,3,5,7 ]
pares = [ 2,4,6,8 ]

numeros = impares + pares #une duas listas

print(numeros)


impares.extend(pares) #Adiciona os elemementos de uma lista (ou qualquer iterável) ao final da lista atual

print(numeros)

#Repetir listas

repeticao = [ 'a', 'b' ] * 3

print(repeticao)

#verificando se item existe na lista

print('manga' in frutas)
print('goiaba' in frutas)


print('____________Exercícios_______________')

#1, 2, 3
animais = []
animais.append('gato')
animais.append('cachorro')
animais.append('pássaro')
print(animais)

animais.insert(1, 'peixe')
print(animais)

#4, 5

animais.remove('gato')
print(animais)

animais.pop()
print(animais)

#6, 7

animais_novos = ['tartaruga', 'hamster']

animais_domesticos = animais_novos + animais

print(animais_domesticos)

#8, 9

animais_domesticos = animais_domesticos * 2

print(animais_domesticos)

print('cachorro' in animais_domesticos)


