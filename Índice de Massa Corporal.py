#=====================================================
#             Índice de Massa Corporal
#=====================================================

print("===================================")
print("    CALCULADORA DE IMC")
print("===================================")

nome = input("Digite seu nome: ")

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

print("\n===================================")
print("          RESULTADO")
print("===================================")

if peso <= 0 or altura <= 0:
    print("Erro: peso e altura devem ser maiores que zero.")

else:
    imc = peso / (altura ** 2)

    print("Nome: {}" .format(nome))
    print("Peso: {}Kg" .format(peso))
    print("Altura: {}m" .format(altura))
    print("Seu IMC é: {}" .format(round(imc, 2)))

    if imc < 18.5:
        print("Classificação: ABAIXO DO PESO")

    elif imc < 25:
        print("Classificação: PESO IDEAL")

    elif imc < 30:
        print("Classificação: SOBREPESO")

    elif imc <= 40:
        print("Classificação: OBESIDADE")

    else:
        print("Classificação: OBESIDADE MÓRBIDA")

print("===================================")

