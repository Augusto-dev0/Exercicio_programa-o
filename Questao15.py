#algoritmo que leia o ano em que uma pessoa nasceu, imprima na
#tela quantos anos, meses e dias essa pessoa ja viveu.

nascimento = int(input("Ano de nascimento: "))
atual = int(input("Ano atual: "))

anos = atual - nascimento
meses = anos * 12
dias = anos * 365

print("Anos:", anos)
print("Meses:", meses)
print("Dias:", dias)