def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    print(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print(f"Tu ta magro")
    elif imc <= 24.9:
        print(f"Esta dentro do normal")
    elif imc <= 29.9:
        print(f"Sobre peso")
    elif imc <= 34.9:
        print(f"Ta gordo nessa porra")
    else:
        print ("THAIS CARLA PORRA?")

peso = float(input("Me informe seu peso em kg: "))
altura = float(input("Agora me informe sua altura em m: "))

valor_imc = calculo_imc(peso, altura)
classificar_imc(valor_imc)