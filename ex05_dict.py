texto_longo = input("Cole o texto que verificaremos o uso das palavras: ")
sep_palavras = texto_longo.split(' ')

contagem = {}

for palavra in sep_palavras:
    palavra.lower().strip("?!;,")
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print("\nFrequência de palavras:")
for chave, valor in contagem.items():
    print(f"{chave}: {valor}")