#===============================================
#          Analisando Triângulos v2.0
#===============================================

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

print("\n===================================")
print("          RESULTADO")
print("===================================")

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Erro: os lados devem ser maiores que zero.")

elif (lado1 + lado2 > lado3
      and lado1 + lado3 > lado2
      and lado2 + lado3 > lado1):

    print("As medidas formam um triângulo!")

    if lado1 == lado2 and lado2 == lado3:
        print("Classificação: EQUILÁTERO")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Classificação: ISÓSCELES")

    else:
        print("Classificação: ESCALENO")

else:
    print("Essas medidas não formam um triângulo.")

print("===================================")
