#=================================================
#           Classificando Atletas
#=================================================

nome = input("Digite o nome do atleta: ")
idade = int(input("Digite a idade do atleta: "))

print("\n===================================")
print("        RESULTADO DO ATLETA")
print("===================================")

print("Nome: {}" .format(nome))
print("Idade: {}" .format(idade))

if 0 > idade:
    print("Idade inválida!")

if idade <= 9:
    print("Categoria: MIRIM")

elif idade <= 14:
    print("Categoria: INFANTIL")

elif idade <= 19:
    print("Categoria: JÚNIOR")

elif idade <= 25:
    print("Categoria: SÊNIOR")

else:
    print("Categoria: MASTER")