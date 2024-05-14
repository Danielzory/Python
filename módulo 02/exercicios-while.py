#Exercícios while PY

print("--------------------Ex1-----------------------------")

senha = "gordo"

tentativa = input("Qual a senha para acessar a geladeira dos doces?\n")

while (tentativa != senha):

    tentativa = input(f"Essa não é a senha... {tentativa}... Tente novamente: \n")

print("Parabens! Acesso liberado")    

print("----------------------------------------------------")


while True:
    user_input = input("Digite sair para encerrar o programa: ")
    if user_input == "sair":
        break

print("--------------------Ex2-----------------------------")    
import random

numero_secreto = random.randint(1,100)
tentativas = 0

print(f"Finge que não sabe - {numero_secreto}")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto: 
        print("O número secreto é maior, tente novamente")
    elif palpite > numero_secreto:
        print("O Número secreto é menor, tente novamente")    
    else:
        print(f"Parabens você acertou o número secreto em {tentativas} tentativas")
        break   
print("----------------------------------------------------")  

print("--------------------Ex3-----------------------------") 

usuario_umber = int(input("Digite um número entre 0 e 100 e tente acertar o número secreto, serrar vamos descontar a somas de seus erros do seu salário: "))
desconto = 0

while (usuario_umber !=0):
    desconto += usuario_umber

    usuario_umber = int(input("Errou... tente novamente: "))
print(f"Parabens, você acertou, o saldo descontado será de {desconto} Reais")    


print("--------------------Ex3-----------------------------")

magic_number = int(input("Hora da mágica, digite números aleatórios, depois digite o zero para encerrar, vou te dizer qual maior número digitado: "))

bigger = 0

while magic_number !=0:
    if bigger < magic_number:
        bigger = magic_number
    magic_number = int(input("Mais um?: "))    
print(f"O maior número digitado foi {bigger}")      
print("--------------------------------------------------")  