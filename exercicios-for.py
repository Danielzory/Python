#for + range

for i in range(0, 11):
    
    print(i)
print("-------------------------------------")    

#for - determianndo intervalo

for i in range(10, 0, -1):

    print(i)   
print("-------------------------------------")

for j in range(10, 30, 3):

    print(j)
print("-------------------------------------")   

soma = 0

for i in range(1, 11, 2):
     print(f"Numero impar atual {i}")

     soma += i
print(f"A soma dos numeros impares é {soma}")
print("-------------------------------------") 


#Exercício 1

resultado = 1

for mult in range(1, 6):

    resultado *= mult
    print(f"Multiplicando por {mult}, o resultado parcial é {resultado}")

print(f"O resultado final da multiplicação de 1 a 5 é: {resultado}")   

print("-------------------------------------") 
#Exercício 2

numeroFinal = int(input("Informe o número  máximo de sua soma de pares: "))
ress = 0

for numeroInicial in range(1, numeroFinal+1):

    if numeroInicial % 2 == 0:
        ress += numeroInicial
        print(f"Soma parcial: {ress}")
print(f"A soma dos numeros pares entre 1 e {numeroFinal} é: {ress}")        

