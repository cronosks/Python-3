#====================================================
#                  Nota Aluno
#====================================================

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

print("\n===================================")
print("        RESULTADO DO ALUNO")
print("===================================")

print("Aluno:", nome)
print("Prova 1:", nota1)
print("Prova 2:", nota2)
print("Prova 3:", nota3)
print("Média: ", round(media, 2))

if media >= 7:
    print("Situação: APROVADO!")

elif media >= 5:
    print("Situação: RECUPERAÇÃO!")

else:
    print("Situação: REPROVADO!")


