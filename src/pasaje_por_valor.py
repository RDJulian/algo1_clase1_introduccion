def sumar_diez(numero: int) -> None:
    # Se suma diez a la copia de la variable que se pasó por parámetro.
    # Por lo tanto, la original no se modifica.
    numero += 10


def main():
    numero = 1
    sumar_diez(numero)
    # Como la variable 'numero' se pasa por valor, al imprimir sigue siendo 1.
    print(numero)


if __name__ == "__main__":
    main()
