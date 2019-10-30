def calcular_franja(dia, hora):
    if dia >= 6:
        franja = "Franja C"
    else:
        if (hora >= 20) and (hora <= 23):
            franja = "Franja A"
        else:
            franja = "Franja B"
    return franja


def precio_comercial(franja, tiempo):
    if franja == "Franja A":
        precio = tiempo * (10000000/60)
    elif franja == "Franja B":
        precio = tiempo * (7000000/60)
    else:
        precio = tiempo * (12000000/60)
    return precio


def principal():
    empresa = (input("Ingrese el nombre de la Empresa:\n"))
    dia = eval(input("Ingrese el día del Comercial: \n"))
    hora = eval(input("Ingrese la hora del Comercial: \n"))
    tiempo = eval(input("Ingrese la duración del Comercial (En Segundos): \n"))
    franja = calcular_franja(dia, hora)
    precio = precio_comercial(franja, tiempo)
    print("La empresa", empresa, "debe pagar", precio, "por su comercial en la", franja)


principal()
