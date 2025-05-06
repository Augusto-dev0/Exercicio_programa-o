#Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se
#ambos são VERDADEIRO ou FALSO. Sendo o numero 1 Verdadeiro e 0 Falso.

a = int(input("Digite 0 ou 1 para A: "))
b = int(input("Digite 0 ou 1 para B: "))

if a == 1 and b == 1:
    print("Ambos são VERDADEIROS")
elif a == 0 and b == 0:
    print("Ambos são FALSOS")
else:
    print("Os valores são diferentes")