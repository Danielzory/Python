#Impimindo textos e variáveis (template strings / format String ou f - string)

nome = 'Daniel'
idade = 29
altura = 1.71
mensagem = f"Olá Mundo, meu nome é {nome}, tenho {idade} anos e {altura:.2f} de altura"

print(mensagem)

"""
Usa-se o f antes das aspas para tornar possível a inserção das variáveis dentro do texto, para incluir 
as variáveis basta usar colocá-las dentro das chaves {Variável}
"""

print("---------------------------------")

#to Uppercase e lowercase

texto = "olá galera, tudo bem?"

texto_upper = texto.upper()
texto_lower = texto.lower()
texto_capitalize = texto.capitalize()

print(f"Texto Upper - {texto_upper} - Texto Lower - {texto_lower}")
print(f"Texto com a primeira em maisculo - {texto_capitalize}")

#Contando quantas vezes a letra apareceu no texto

ocorrencia = texto.count('a') 
"""o count é case sensitive"""

print(f"Quantas vezes apareceram a letra a (menuscula) no texto: {ocorrencia}")
print("---------------------------------")

#Replace

texto_alterado = texto.replace('galera', 'turma')

print(f"Texto alterado: {texto_alterado}")
print("---------------------------------")
print("--------------Exercícios 1------------------")

#1 - 2 - 3
nome = 'Maria'
sobrenome = 'Silva'
idade = 30

#4 - 5
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

#6 - 7

mensagem = f"Bom dia, me chamo {nome_completo}, tenho {idade} anos de idade."

print(mensagem)

print("--------------Exercícios 2------------------")

#1 - 2
frase = "Python é uma linguagem de programação poderosa e versátil."

print(len(frase))

#3 
palavra = frase.split()[0]
"""Ou palavra = frase[0:6]"""
print(palavra)

#4
frase_maiuscula = frase.upper()
print(frase_maiuscula)

#5
frase_alterada = frase.replace('poderosa', 'incrível')
print(frase_alterada)



