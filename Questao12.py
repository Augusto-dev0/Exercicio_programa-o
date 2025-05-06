#- Faça um algoritmo que leia o valor de um produto e determine o valor que
#deve ser pago, conforme a escolha da forma de pagamento pelo comprador e
#imprima na tela o valor final do produto a ser pago.

valor = float(input("Valor do produto: "))
codigo = int(input("Código da forma de pagamento: "))

if codigo == 1:
    total = valor - (valor * 0.15)
elif codigo == 2:
    total = valor - (valor * 0.10)
elif codigo == 3:
    total = valor
elif codigo == 4:
    total = valor + (valor * 0.10)
else:
    print("Código inválido")
    total = 0

if total != 0:
    print("Total a pagar:", total)
    