lista = ['A', 'B', 'C', 'D', 'E']

for item in lista:

    print(item)

    if item == 'C':

        break


frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:

    print(fruta)



numero = int(input("Informe um número: "))

for i in range(1, numero+ 1):

    if i % 2 == 0:

        print(i, "Par")

    else: 

        print(i, "Impar")    

print("Fim da lista")      

#Lista de compras

itens = ["Pão", "Queijo", "Ovos", "Cebola", "Vinho"]

for item in itens:

    print(f"Eu preciso de {item}")

#Imprimir estrelas

for i in range (5,0,-1):

    print('*'*i)

#Palavras com mais de 4 letras

palavras = ["casa", "carro", "sol", "árvore"] 

for palavra in palavras:
    
    if len(palavra) >= 4:

        print(palavra)
        