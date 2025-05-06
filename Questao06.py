#Faça um algoritmo que leia um valor qualquer e imprima na tela com um
#reajuste de 5%.

valor = float(input("Digite um valor: "))
novo_valor = valor + (valor * 0.05)
print("Valor com reajuste de 5%:",int(novo_valor, 2))