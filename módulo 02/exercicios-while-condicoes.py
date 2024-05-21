#While usando condições complexas
print('Exercicio 1 -----------------------------')
x, y = 5, 15

while x < 10 and y > 10:

    print(f"X: {x}, y: {y}")

    x += 1
    y -= 1
print("loop concluido")
print(f"Valores finais de x e y: {x} e {y}")     


print('Exercicio 2 -----------------------------')

numero_secreto1 = 7
numero_secreto2 = 3

tentativas = 5

adivinhou1 = False
adivinhou2 = False

while tentativas >0 and tentativas <= 5 and (not adivinhou1 or not adivinhou2):
    print(f"Tentativas restantes: {tentativas}")

    palpite1 = int(input("Primeiro número entre 1 - 10: "))
    palpite2 = int(input("Segundo número entre 1 - 10: "))

    if palpite1 == numero_secreto1:
        print("Você adinvihou o primeiro número")

        adivinhou1 = True

    if palpite2 == numero_secreto2:
        print("Você adinvihou o segundo número")

        adivinhou2 = True

    if not adivinhou1 or not adivinhou2:

        print("Tente novamente")

        tentativas -= 1
if adivinhou1 and adivinhou2:

    print("Parabens, você acertou ambos os números")
else:

    print(f"Você não conseguiu adinvinhas os números, eles eram {numero_secreto1} e {numero_secreto2}")            




