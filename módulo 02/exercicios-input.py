#Declaração

nome = input("Insira seu nome: \n")

print("\nOlá aluno", nome)

#Utilizando input junto com formatação do dado inserido

nota1 = float(input("digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2)/2

print("\nAluno:",nome, "Nota 1:", nota1, "Nota 2:", nota2, " - Média:", media)


#Exercício Tabuada

nome = input("Qual é o seu nome? \n")
print("Olá,", nome, "espero que esteja bem")
inputNumber = int(input("Você deseja ver a taboada de qual número?\n"))

tabuada = inputNumber * 1, inputNumber * 2, inputNumber * 3, inputNumber * 4, inputNumber * 5, inputNumber * 6, inputNumber * 7, inputNumber * 8, inputNumber * 9, inputNumber * 10

i1, i2, i3, i4, i5, i6, i7, i8, i9, i10 = tabuada

print(nome,"Segue taboada do número", inputNumber)
print("1 *", inputNumber, "=", i1)
print("2 *", inputNumber, "=", i2)
print("3 *", inputNumber, "=", i3)
print("4 *", inputNumber, "=", i4)
print("5 *", inputNumber, "=", i5)
print("6 *", inputNumber, "=", i6)
print("7 *", inputNumber, "=", i7)
print("8 *", inputNumber, "=", i8)
print("9 *", inputNumber, "=", i9)
print("10 *", inputNumber, "=", i10)
print("-----------Use com sabedoria----------------")

#Exercício idade

print("Olá! Deseja saber sua idade com base no ano em que nasceu?")
anoNasc = int(input("Informe seu ano de nascimento: \n"))
anoAtual = 2024

idade = anoAtual - anoNasc

print("Sua idade é de aproximadamente:", idade, "Anos")
print("---------------End------------------")