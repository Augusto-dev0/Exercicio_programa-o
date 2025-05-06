#algoritmo que leia uma temperatura em Fahrenheit e calcule a
#temperatura correspondente em grau Celsius. Imprima na tela as duas
#temperaturas.

f = float(input("Temperatura em Fahrenheit: "))

c = (5 * (f - 32)) / 9

print("Fahrenheit:", f)
print("Celsius:", c)