def multiplicar(unNumero: int, otroNumero: int) -> int:
    return unNumero * otroNumero


def sumar(unNumero: int, otroNumero: int) -> int:
    return unNumero + otroNumero


def numeroCollatz(unNumero: int) -> int:
    return sumar(multiplicar(unNumero, 3), 1)


def ingresarNumero() -> int:
    return int(input("Ingrese un numero: "))


def imprimirResultado(unNumero: int) -> None:
    print(unNumero)


def main() -> None:
    unNumero = ingresarNumero()
    otroNumero = ingresarNumero()

    imprimirResultado(sumar(numeroCollatz(unNumero), numeroCollatz(otroNumero)))


main()
