"""Leer la base y la altura de un rectángulo, calcular el perímetro y la superficie."""

base = int(input("Ingrese un numero entero: "))
altura = int(input("Ingrese un numero entero: "))

perimetro = 2 * base + 2 * altura
area = base * altura

print(perimetro)
print(area)
