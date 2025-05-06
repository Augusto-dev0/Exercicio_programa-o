#algoritmo que leia três valores que representam os três lados de
#um triângulo e verifique se são válidos, determine se o triângulo é equilátero,
#isósceles ou escaleno.

x = float(input("Lado 1: "))
y = float(input("Lado 2: "))
z = float(input("Lado 3: "))

if x + y > z and x + z > y and y + z > x:
    if x == y and y == z:
        print("Equilátero")
    elif x == y or x == z or y == z:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não forma triângulo")