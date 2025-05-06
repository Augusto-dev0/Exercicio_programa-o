#Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem
#1,10m e cresce 3 centímetros por ano. Faça um algoritmo que calcule e
#imprima na tela em quantos anos serão necessários para que Sara seja maior
#que Francisco.

f = 1.5
s = 1.1
a = 0

while s <= f:
    f = f + 0.02
    s = s + 0.03
    a = a + 1

print("Anos:", a)