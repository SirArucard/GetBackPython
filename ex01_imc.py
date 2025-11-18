peso = float(input("Me informe seu peso em kg: "))
altura = float(input("Agora me informe sua altura em m: "))

calcIMC = peso / (altura * altura)
print(f"Seu imc é {calcIMC:.2f}")