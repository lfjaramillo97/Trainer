# Códigos ANSI para colores de texto
COLOR_ROJO = '\033[91m'
COLOR_VERDE = '\033[92m'
COLOR_AMARILLO = '\033[93m'
COLOR_AZUL = '\033[94m'
COLOR_RESET = '\033[0m'

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

dias_por_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

while True:
    # Solicitar entrada al usuario y validar el mes
    while True:
        mes_input = input(COLOR_VERDE + "Ingresa el número del mes (1-12): " + COLOR_RESET)
        if not mes_input.isdigit():
            print(COLOR_ROJO + "Por favor, ingresa un valor numérico para el mes." + COLOR_RESET)
            continue

        mes = int(mes_input)
        if mes < 1 or mes > 12:
            print(COLOR_ROJO + "Mes inválido. Inténtalo nuevamente." + COLOR_RESET)
        else:
            break

    while True:
        dia_input = input(COLOR_VERDE + f"Ingresa el día del mes (1-{dias_por_mes[mes]}): " + COLOR_RESET)
        if not dia_input.isdigit():
            print(COLOR_ROJO + "Por favor, ingresa un valor numérico para el día." + COLOR_RESET)
            continue

        dia = int(dia_input)
        if dia < 1 or dia > dias_por_mes[mes]:
            print(COLOR_ROJO + f"Día inválido. Ingresa un día entre 1 y {dias_por_mes[mes]}." + COLOR_RESET)
        else:
            break

    # Determinar la estación
    if (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
        color_estacion = COLOR_AZUL
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 10):
        estacion = "Verano"
        color_estacion = COLOR_AMARILLO
    elif (mes == 6 and dia >= 11) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 25):
        estacion = "Otoño"
        color_estacion = COLOR_AMARILLO
    elif (mes == 9 and dia >= 26) or (mes == 10 or mes == 11 or mes == 12):
        estacion = "Primavera"
        color_estacion = COLOR_VERDE

    print(
        f"En el mes de {meses[mes]}, en el día {dia}, estamos en la estación de: {color_estacion+estacion+COLOR_RESET}")

    opcion = input("\n¿Deseas ingresar otra fecha? (s/n): \n")
    if opcion.lower() != "s":
        print("\n**¡Programa Finalizado!**\n")
        break