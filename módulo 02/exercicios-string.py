#Posição da letra - Em Python strings são tratadas como array
posicaoLetra = "Python"
frase = "olá, mundo"

print('->',posicaoLetra[0])
print('->',posicaoLetra[1])
print('->',posicaoLetra[2])
print('->',posicaoLetra[3])
print('->',posicaoLetra[4])
print('->',posicaoLetra[5])

print('Usando o fatiamento - slicing', posicaoLetra[1:4])
print('Frase:', frase, "- Fatiamento:", frase[0:3])
print("------------------------------------")

#Verificando se palafra existe em texto

texto = "O módulo de python é legal"

print("Buscando palavra em texto usando IN, retorna um boolean")

palavra = "python"

if palavra in frase:
    print('Sim, existe esta palavra na frase')
else:
    print('Não, não esta na frase')    
print("------------------------------------")    

#Removendo espaços "vazios"

fraseComEspaco = "        Opa! Têm muitos espaços      "

print('Frase com espaços',fraseComEspaco)

print('Retirando os espaços com a função .strip() = ', fraseComEspaco.strip())
print("------------------------------------") 

#Manipulando palavras de dentro do texto

frase2 = "Bom dia! o sol já nasceu lá na fazendinha..."

palavras = frase2.split()

print("O metodo Sprite retorna um array com cada palavra da frase:", palavras)

"""O metodo Sprite separa as palavras se baseando em cada espaço entre as palavras, caso eu não passe nenhum argumento"""

palavrasUnidas = ' '.join(palavras)

print("O metodo Join junta strings de array:", palavrasUnidas)

"""O metodo Join junta strings de array, utilizando um separador especificado entre cada elemento"""

palavraComCaracter = "****Opa****"

print("Usando o metodo strip para retirar algo do texto", palavraComCaracter)
print("Usando o stripe(*):", palavraComCaracter.strip('*'))

print("------------------------------------")


