#=================================================
#            Alistamento Militar
#=================================================

nome = input("Digite o nome: ")
Idade = int(input("Digite sua Idade: "))

print ("\nOlá {}!" .format(nome))
print ("Sua idade é {} anos." .format(Idade))

if Idade < 17:
    print("Situação: Você ainda não está na idade prevista.")
    print("Aguarde e acompanhe as orientações oficiais.")

elif Idade == 17:
    print("Situação: Você tem 17 anos.")
    print("Pode começar a se preparar para o alistamento.")
    print("Consulte as orientações oficiais.")

elif Idade == 18:
    print("Situação: Você tem 18 anos.")
    print("Verifique o prazo para realizar seu alistamento militar.")

else:
    print("Situação: Você tem mais de 18 anos.")
    print("Consulte a Junta de Serviço Militar.")
    print("Verifique sua situação e como regularizá-la.")




