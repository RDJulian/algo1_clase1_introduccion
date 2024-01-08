def numero_opuesto(numero):
    return -numero


def la_respuesta_a_todo():
    return 42


def imprimir_paridad(numero: int) -> None:
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")


def campeon_del_mundo(equipo: str) -> bool:
    return equipo == "Argentina"


def main():
    equipo = input("Ingrese un equipo: ")
    if campeon_del_mundo(equipo):
        print("Otro día, otra coronación de gloria.")


if __name__ == "__main__":
    main()
