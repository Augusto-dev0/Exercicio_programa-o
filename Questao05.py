#Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de
#um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na
#tela o resultado. (Base para o Salário mínimo R$ 1.518,00).

salario = float(input("Digite o salário: "))
salario_minimo = 1518.00

quantidade = salario / salario_minimo

print("Você ganha", round(quantidade, 2), "salários mínimos.")