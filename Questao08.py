#Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela
#os valores em ordem decrescente.

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a > b and a > c:
    if b > c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b > a and b > c:
    if a > c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a > b:
        print(c, a, b)
    else:
        print(c, b, a)