def calcular_area_rectangulo(base: float, altura: float) -> float:
    return base * altura


def calcular_area_triangulo(base: float, altura: float) -> float:
    return base * altura / 2


def main():
    print("Area rectángulo 1:", calcular_area_rectangulo(5, 3))
    print("Area rectángulo 2:", calcular_area_rectangulo(4, 4))
    print("Area triángulo 1:", calcular_area_triangulo(3, 4))
    print("Area triángulo 2:", calcular_area_triangulo(5, 2))


if __name__ == "__main__":
    main()
