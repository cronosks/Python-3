#=============================================
#        Comparando números
#=============================================

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print("o {} é maior que o {}" .format(n1, n2))
elif n1 < n2:
    print("o {} é maior que o {}" .format(n2, n1))

else:
    print("ambos os números {} e {} são da mesma proporção.".format(n1, n2))