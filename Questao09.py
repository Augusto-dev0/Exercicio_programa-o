#Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma
#pessoa, leia o seu peso e sua altura e imprima na tela sua condição de acordo
#com a tabela abaixo:

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print("Peso ideal")
elif imc >= 25 and imc <= 29.9:
    print("Levemente acima do peso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade grau I")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")