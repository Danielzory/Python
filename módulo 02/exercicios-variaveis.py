# Variáveis

nome = "Ana Paula"
idade = 30

print("tipo das variáveis", type(nome),type(idade))

# Alteerando o tipo

idade = str (30)

print("Tipo davariável trasformada", type(idade))

# Case sensitive 
i = 30
I = True

print("Variavel i = ", i, "variável I = ", I)

# Atribuindo valores a variáveis em sequência

var1, var2, var3 = "texto1", "texto2", "texto3"

print("var1 = ", var1, "var2 = ", var2, "var3 = ", var3)

#comentário longo
"""
caso eu deseje declarar o mesmo valor a várias variáveis...

"""
var1 = var2 = var3 = "Texto para todas variáveis"

print("var1, var2 e var3 tem seu valor igual a = ", var1,var2,var3)

"""
Caso exista uma coleção de valores em uma variável, podemos extrair em variáveis, isto é chamado de descompactar
"""

textos = "descompactar 1-", "descompactar2-", "descompactado"

desc1, desc2, desc3 = textos

print("Descompactando:", desc1, desc2, desc3)

print("---------------------Exercícios 1---------------------------")
#Exercícos

#1. Declare uma variável chamada "idade" e atribua o valor 25 a ela.
idade = 25
#2. Declare uma variável chamda "nome" e atribua o valor "João" a  ela.
nome = "João"
#3. Declare uma váriavel chamda "saldo" e atribua o valor 100.50 a ela.
saldo = 100.50
#4. crie uma variável chamada "soma" e atibua a soma entre idade e saldo a ela.
soma = saldo + idade
#5. Imprima o valor de soma na tela.
print("A soma entre o saldo e a idade de", nome,"é igual a", soma)

print("---------------------Exercícios 2---------------------------")
#Exercícos

nota1 = 7.5
nota2 = 8.3
nota3 = 6.9

media = (nota1 + nota2 + nota3)/3

print("A media entre as notas é:", format(media, ".2f")) #para formatar - duas casas decimais

