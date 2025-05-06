#algoritmo que leia o nome e a idade de uma peso e imprima na tela o
#nome da pessoa e se ela é maior ou menor de idade.

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

print("Nome:", nome)

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")