#Slicing de Lista
"""
Como acessar subconjuntos de listas
Omissão de índices iniciais ou finais
slicing com passos

o "slicing" é uma maneira poderosa de acessar subconjuntos de listas
"""

#Acessando subconjuntos especificando os indices de início e fim

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
subconjunto = lista[1:4]
print(subconjunto)

omissao_finais = lista[:2]
print(omissao_finais)

elemntos_finais = lista[2:]
print(elemntos_finais)

elementos_alternados = lista[::2] #do inicio ao final alternaod o indice em 2
print(elementos_alternados)

subconjunto_alternado = lista[2:8:2] #do indice 2 ao 8 alternado o indice 2 a 2
print(subconjunto_alternado)

print("________________Exercício____________________")

#1
cores = ['vermelho', 'verde', 'azul', 'amarelo', 'laranja', 'roxo', 'marrom', 'cinza']

#2
verde_azul = cores[1:3]
print(verde_azul)

#3
duas_cores = cores[:2]
print(duas_cores)
#4
amarelo_folow = cores[3:]
print(amarelo_folow)

#5
indice_impar = cores[1::2]
print(indice_impar)

#6
inverter = cores[::-1]
print(inverter)
