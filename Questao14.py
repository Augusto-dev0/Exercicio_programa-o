#Faça um algoritmo que receba um valor A e B, e troque o valor de A por B
#e o valor de B por A e imprima na tela os valores.

a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")

a, b = b, a

print("A agora vale:", a)
print("B agora vale:", b)