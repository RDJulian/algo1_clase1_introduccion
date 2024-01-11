"""Leer dos números A y B e intercambiar el valor de sus variables."""


def leer_numero() -> int:
    return int(input("Ingrese un numero: "))


def intercambiar(a: int, b: int) -> tuple[int, int]:
    return b, a


def imprimir_valores(a: int, b: int) -> None:
    print(f"El valor de a es {a} y el de b es {b}")


def main():
    a = leer_numero()
    b = leer_numero()

    imprimir_valores(a, b)
    a, b = intercambiar(a, b)
    imprimir_valores(a, b)


if __name__ == "__main__":
    main()
