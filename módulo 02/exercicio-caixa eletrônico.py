#Exercicio caixa eletrônico

saldo = 0

while True:
    print("Bem vindo, ecolha uma das opções abaixo:")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("------------------------------\n Digite 1 para Verificar o Saldo \n Digite 2 para Realizar um depósito \n Digite e para Realizar um Saque \n Digite 4 para sair\n------------------------------")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    opcao = float(input("Escolha uma opção entre (1-4): "))

    if opcao == 1: 
        print("=============================================================================================")
        print(f"Seu saldo atual é {saldo: .2f} Reais")
        print("=============================================================================================")
    elif opcao == 2:
        deposito = float(input("Informe o valor depositado: "))

        if  deposito > 0:
            saldo = deposito + saldo
            print(f"Deposito de {deposito: .2f} Reais realizado com sucesso! Novo saldo: {saldo: .2f} Reais")
        else:
            print("Informe um valor positivo")

    elif opcao == 3:
        saque = float(input("Informe o valor do saque: "))

        if saque <= saldo and saque > 0:
            saldo = saldo - saque
            print(f"Saque no valor de {saque: .2f} Reais realizado com sucesso! Novo saldo: {saldo: .2f} Reais")
        else:
            print("Saldo insufuciênte ou valor inválido, tente novamente")

    elif opcao == 4:
        print("Realizando logout, obrigado!")         
        break

    else:
        print("Opção inválida, tente novamente")    