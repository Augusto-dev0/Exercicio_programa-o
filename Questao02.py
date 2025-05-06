#Faça um algoritmo para receber um número qualquer e imprimir na tela se o
#número é par ou ímpar, positivo ou negativo.

numero = int(input("Informe um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")