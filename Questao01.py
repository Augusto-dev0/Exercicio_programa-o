# Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na
# tela a soma entre A e B é mostre se a soma é menor que C.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

# Soma de A e B
soma = A + B
print("A soma de A e B é:", soma)

# soma menor que C
if soma < C:
    print("A soma é menor que C.")
else:
    print("A soma não é menor que C.")
