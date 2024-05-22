#Taboada

number = int(input("Você quer a taboada de qual número?\n"))

for i in range(1, 11):

    mult = i * number

    print(f"{i} * {number} = {mult}")

print("--------------------------------------")    

#Soma dos quadrados

intervalo = int(input("Até que número você deseja visualizar a lista dos quadrados?\n"))

sum = 0

for j in range(1, intervalo+1):

    square = j * j
    print(f"Quadrado de {j}: {square}")

    sum += square

soma = input(f"Você deseja saber a soma de todos estes números? - (s/n): ")    

while True:
    if soma == "s":
        print(f"A soma dos quadrados é: {sum}")
        break
    elif soma == "n":
        print("Ok, fim do programa, obrigado") 
        break
    else:
        print("Opção inválida, digite s para sim e n para não") 
        soma = input(f"Você deseja saber a soma de todos estes números? - (s/n): ") 
print("--------------------------------------")           

