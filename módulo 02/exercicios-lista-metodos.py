#Metodos de Lista

"""
sort(): ordena a lista in-place.
reverse(): inverte a ordem dos elementos in-place.
count(): conta o número de ocorrência de um elemento.
index(): retorna o índice da primeira ocorrência de uma elemento
"""

numeros = [3,5,6,34,1,23,77,10]
frutas = ['banana', 'maça', 'uva', 'maça', 'pera', 'banana', 'banana']

print(numeros)
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)
frutas.sort()
print(frutas)
numeros.reverse()
print(numeros)

maca = frutas.count('maça')
banana = frutas.count('banana')
print(maca)
print(banana)

print(frutas.index('uva'))
print('_______________Exercícios______________')

#1
numbers = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]

#2

numbers.sort()
print('Questão 2: ', numbers)

#3

numbers.reverse()
print("Questão 3: ", numbers)

#4

print("Questão 4: ", numbers.count(11))


#5

print("Questão 5: ", numbers.index(78))

#6

try:
    numbers.index(102)
except:
    print("Numero não esta dentro da lista, te um outro por gentielza")
finally:
    print("Questão 6 Resolvida!")
    
