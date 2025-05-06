#Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e
#B forem iguais, deverá somar os dois valores, caso contrário devera multiplicar
#A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a
#uma variável C e imprimir seu valor na tela.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))


if A == B:
    C = A + B

else:
    C = A - B

print("O resultado é:", C)