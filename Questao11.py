#algoritmo que leia quatro notas obtidas por um aluno, calcule a
#média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi
#aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final
#deve ser maior ou igual a 7.

nome = input("Digite o nome do aluno: ")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

print("Nome:", nome)
print("Média:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
