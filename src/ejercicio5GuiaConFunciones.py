"""Leer la base y la altura de un rectángulo, calcular el perímetro y la superficie."""


def ingresarNumero() -> int:
    return int(input("Ingrese un numero: "))


def multiplicar(unNumero: int, otroNumero: int) -> int:
    return unNumero * otroNumero


def sumar(unNumero: int, otroNumero: int) -> int:
    return unNumero + otroNumero


def imprimirResultado(unNumero: int) -> None:
    print(unNumero)


def calcularAreaRectangulo(base: int, altura: int) -> int:
    return multiplicar(base, altura)


def calcularPerimetroRectangulo(base: int, altura: int) -> int:
    return sumar(multiplicar(base, 2), multiplicar(altura, 2))


def main() -> None:
    base = ingresarNumero()
    altura = ingresarNumero()

    perimetro = calcularPerimetroRectangulo(base, altura)
    area = calcularAreaRectangulo(base, altura)

    imprimirResultado(perimetro)
    imprimirResultado(area)


main()

"""SnakeCase = uno_escribe_asi"""
"""CamelCase = unoEscribeAsi"""
