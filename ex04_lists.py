listinha = []
for i in range (1, 6):
    numero = int(input("Me dê os números: "))
    listinha.append(numero)

print(f"Maior numero: {max(listinha)}")
print(f"Menor numero: {min(listinha)}")
print(f"A soma é: {sum(listinha)}")
print(f"Organizadin: {sorted(listinha)}")

