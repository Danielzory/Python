#Estrutura condicional ternária

idade = int(input("Informe sua idade: \n"))

status = "Adulto" if idade >= 18 else "menor de idade"

print(status)

#Exercício

nota = int(input("Informe sua nota: \n"))

resultado = "Alta" if nota >= 8 else "média" if nota >= 6 and nota <= 7 else "Baixa"

print(resultado)