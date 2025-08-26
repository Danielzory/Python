#Lista Comprehensions

"""
Uma maneira de criar listas:  [x**2 for x in range(10) if x % 2 == 0]
Elas oferecem uma maneira conscisa de criar listas, e são frequentemente  mais compreesíveis e mais  
eficientes do que usar loops.
"""

#Exemplo

quadrados_loop  = []

for x in range(10):
    quadrados_loop.append(x**2)
print("Com loop",quadrados_loop) 

quadrados = [x**2 for x in range(10)]
print("Usando lista", quadrados)

print("_________________________________________")

#Exemplo 2

quadrados_pares = []

for x in range(10):
    if x % 2 ==  0:
        quadrados_pares.append(x**2)
print("Forma Tradicional", quadrados_pares)

quadrados_pares_list = [x**2 for x in range(10) if x % 2  == 0]
print("Cos Lista", quadrados_pares_list)

print("_________________________________________")

#Exemplo 3

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

combinacoes = []

for  x in a:

    for y in b:

        if x + y == 5:
            combinacoes.append((x, y))
print("Metodo Tradicional", combinacoes)

combinacoes_list = [(x , y) for x in a for y in b if (x + y == 5)]
print("Com lista", combinacoes_list)

print("____________________Exercício_______________________")

#1
cubo = [n**3 for n in range(10)]
print("Primeiro: ",cubo)

#2
divisivel_por_tres = [n for n in range(10) if n % 3 == 0]
print("Segundo: ", divisivel_por_tres)

#3
frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"]

fruttas_cinco_letras = [f for f in frutas if len(f) > 5]
print("Terceiro: ", fruttas_cinco_letras)

#4
notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82]

aprovados = [n for n in notas if n > 75]
aprovados.sort()
print("Quarto: ", aprovados)
