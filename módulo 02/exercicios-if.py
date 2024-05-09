#Exercício voto
print("Vamos verificar se você tem a idade necessária para votar")
idade = int(input("Informe sua idade abaixo: \n"))

if idade >= 16 and idade < 18:
    print(f"Você tem {idade} anos, seu voto é facultativo")
elif idade >=18 and idade < 65:
     print(f"Você tem {idade} anos, seu voto é obrigatório")   
elif idade >= 65:
     print(f"Você tem {idade} anos, você é idoso(a), seu voto é facultativo")     
else:
     print(f"Você tem {idade} anos, não pode votar")     


print("--------------end---------------")
#Exercício enquete
print("Informe uma nota entre 1 e 5 para nosso atendimento")
nota = int(input("Informe a nota:"))

if nota >=1 and nota < 2:
     print("Você considera nosso atendimento péssimo?")
     confirmacão = int(input("Digite 1 para sim e 2 para não: "))
     if confirmacão == 1:
          print("Lamentamos sua experiência e agradecemos pelo feedback")
     elif confirmacão == 2:
          print("Reinicie o atendimento para fazer a valiação correta")   
     else: 
        print("Opção inválida")
elif nota >= 2 and nota < 4:
     print("Você considera nosso atendimento Regular?")
     confirmacão = int(input("Digite 1 para sim e 2 para não: "))
     if confirmacão == 1:
          print("Vamos buscar evoluir, agradecemos pelo feedback")
     elif confirmacão == 2:
          print("Reinicie o atendimento para fazer a valiação correta")   
     else: 
          print("Opção inválida")
elif nota == 4:
     print("Você avaliou nosso atendimento como bom, agradecemos seu feedback") 
elif nota == 5:
     print("Que ótima noticia! Recebemos um Exelente de você!")     
else: 
     print("Nota inválida")  

print("----------End---------------")             

#Exercício desconto

valor = float(input("Informe o valor do produto e iremos verificar o valor do desconto disponível: \n"))

if valor < 500:
     print(f"Sua compra foi no valor de {valor} Reais, você não receberá desconto")
elif valor >= 500 and valor < 1000:
     valorComDesconto = (valor * 0.9)
     
     print(f"Compra no valor de {valor} Reais, você recebeu um desconto de 10% e só parará {valorComDesconto: .2f} Reais")    
else:
     valorComDesconto = valor * 0.8
     print(f"Compra no valor de {valor} Reais, você recebeu nosso desconto máximo e só para {valorComDesconto: .2f} Reais")  

print("------------End-------------")      
      
