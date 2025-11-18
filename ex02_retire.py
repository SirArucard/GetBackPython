idade = int(input("Qual a sua idade? \n"))
contribuicao = int(input("Quantos anos de contribuição você tem? \n"))

if idade >= 65 or contribuicao >= 30:
    print("Apto a se aposentar")
else:
    print("Continue trabalhando")