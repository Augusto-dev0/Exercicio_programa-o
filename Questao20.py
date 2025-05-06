# Faça um algoritmo que receba um valor inteiro e imprima na tela a sua
# tabuada.

n = int(input("Número: "))
x = 1

while x <= 10:
    print(n, "*", x, "=", n * x)
    x = x + 1
