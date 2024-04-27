#radom
import random

print("random com randorange de 1 a 100 =",random.randrange(1,100))

print("random com random gera números aleatórios entre 0 e 1 =", random.random())

print("random com randint gera número entre um intervalor, porém inclui os extremos =", random.randint(1,100))

d20 = ["1 Critical failure", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, "20 Critical Damage!"]

print("Usando seleção aleatória de intens de um array com radom =", random.choice(d20))

cards = ["Copas", "Pals", "Ouro", "Espadas"]

random.shuffle(cards)

print("Radon para embaralhar itens de um array =", cards)

print("Para imprimir número aléatórios  de ponto flutuante entre intervalos específicos =", random.uniform(5.5, 9.6))