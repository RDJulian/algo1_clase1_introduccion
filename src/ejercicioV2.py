def multiplicacion(unNumero: int, otroNumero: int) -> int:
    return unNumero * otroNumero


def suma(unNumero: int, otroNumero: int) -> int:
    return unNumero + otroNumero


def numeroCollatz(unNumero: int) -> int:
    return suma(multiplicacion(unNumero, 3), 1)


def ingresarNumero() -> int:
    return int(input("Ingrese un numero: "))


def imprimirResultado(unNumero: int) -> None:
    print(unNumero)


def main() -> None:
    unNumero = ingresarNumero()
    otroNumero = ingresarNumero()

    imprimirResultado(suma(numeroCollatz(unNumero), numeroCollatz(otroNumero)))


main()
