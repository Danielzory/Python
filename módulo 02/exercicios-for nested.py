#loops aninhados

for i in range(4):

    for j in range (4):

        print(f"{i} * {j} = {i*j}")

print("----------------------------------")       


#Combinando for e  if em uma mesma linha

quadrados_pares = [x**2 for x in range(10) if x % 2 ==0]

"""O resultado é armazenado no array quadrados_pares"""

print(quadrados_pares)

texto = "Hello World"

consoantes = [char for char in texto if char.lower() not in 'aeiou']

print(consoantes)

#Exercício1 - Fatorial

numero = int(input("Você deseja o fatorial de?: "))

if numero < 0:

    print("insira um número positivo maior que zero")

else:

    fatorial = 1

    for mult in range(1, numero + 1):

        fatorial *= mult

        print(f"{mult}! =", end =" ")

        for i in range(1, mult +1):

            print(i, end=" ")

            if i != mult:

                print("* ", end = "")

        print(f"= {fatorial}")    

print("-----------------------end---------------------")      

#triangulo

altura = int(input("Qual a altura do seu triângulo? \n"))
simbolo = input("Selecione um símbolo: \n")

for i in range(altura):
   espacos = altura - i - 1
   caracteres = 2 * i + 1
   print(' ' * espacos + simbolo * caracteres) 

