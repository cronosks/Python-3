#======================================================
#             Gerenciador De Pagamentos
#======================================================

print("===================================")
print("      GERENCIADOR DE PAGAMENTOS")
print("===================================")

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto (R$): "))

print("\nEscolha a forma de pagamento:")
print("1 - Dinheiro ou cheque à vista")
print("2 - Cartão à vista")
print("3 - Cartão parcelado em até 2 vezes")
print("4 - Cartão parcelado em 3 vezes ou mais")

opcao = int(input("Digite a opção desejada: "))

print("\n===================================")
print("        RESUMO DA COMPRA")
print("===================================")

if preco <= 0:
    print("Erro: o preço deve ser maior que zero.")

elif opcao == 1:
    desconto = preco * 0.10
    total = preco - desconto

    print("Produto: {}" .format(produto))
    print("Pagamento: Dinheiro ou cheque")
    print("Desconto: R$ {}" .format(round(desconto, 2)))
    print("Total a pagar: R$ {}" .format(round(total, 2)))

elif opcao == 2:
    desconto = preco * 0.05
    total = preco - desconto

    print("Produto: {}" .format(produto))
    print("Pagamento: Cartão à vista")
    print("Desconto: R$ {}" .format(round(desconto, 2)))
    print("Total a pagar: R$ {}" .format(round(total, 2)))

elif opcao == 3:
    total = preco
    parcela = total / 2

    print("Produto:{}" .format(produto))
    print("Pagamento: Cartão em até 2 vezes")
    print("Total a pagar: R$ {}" .format(round(total, 2)))
    print("Valor de cada parcela: R$ {}" .format(round(parcela, 2)))

elif opcao == 4:
    vezes = int(input("Em quantas vezes deseja parcelar? "))

    if vezes < 3:
        print("Erro: escolha pelo menos 3 parcelas.")

    else:
        juros = preco * 0.20
        total = preco + juros
        parcela = total / vezes

        print("Produto:", produto)
        print("Pagamento: Cartão parcelado")
        print("Juros: R$", round(juros, 2))
        print("Total com juros: R$", round(total, 2))
        print("Quantidade de parcelas:", vezes)
        print("Valor de cada parcela: R$", round(parcela, 2))

else:
    print("Opção inválida! Escolha de 1 a 4.")

print("===================================")