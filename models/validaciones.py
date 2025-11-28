from datetime import datetime

# -------------------------------
# 1. Campo no vacío
# -------------------------------
def input_no_vacio(texto):
    while True:
        valor = input(texto).strip()
        if valor:
            return valor
        print("El campo no puede estar vacío.")


# -------------------------------
# 2. Número entero
# -------------------------------
def input_entero(texto):
    while True:
        valor = input(texto)
        if valor.isdigit():
            return int(valor)
        print("Debe ingresar un número entero válido.")


# -------------------------------
# 3. Número entero dentro de opciones existentes
# -------------------------------
def input_id_valido(texto, ids_validos):
    ids_validos = list(map(int, ids_validos))
    while True:
        valor = input_entero(texto)
        if valor in ids_validos:
            return valor
        print(f"Debe elegir un ID válido: {ids_validos}")


# -------------------------------
# 4. Validación por conjunto de opciones
# -------------------------------
def input_opcion(texto, opciones_validas):
    opciones_validas = [opt.lower() for opt in opciones_validas]
    while True:
        valor = input(texto).strip().lower()
        if valor in opciones_validas:
            return valor
        print(f"Debe ingresar una opción válida: {opciones_validas}")


# -------------------------------
# 5. Validación formato fecha
# -------------------------------
def input_fecha(texto):
    while True:
        valor = input(texto).strip()
        try:
            datetime.strptime(valor, "%Y-%m-%d")
            return valor
        except ValueError:
            print("Formato de fecha inválido. Debe ser YYYY-MM-DD.")
            

# -------------------------------
# 6. Validación formato hora
# -------------------------------
def input_hora(texto):
    while True:
        valor = input(texto).strip()
        try:
            datetime.strptime(valor, "%H:%M")
            return valor
        except ValueError:
            print("Formato de hora inválido. Debe ser HH:MM.")


# -------------------------------
# 7. Validación valoracion (0-5)
# -------------------------------
def input_valoracion(texto):
    while True:
        valor = input(texto)

        if valor.replace(".", "", 1).isdigit():

            try:
                num = float(valor)
            except ValueError:
                print("Debe ingresar un número decimal válido.")
                continue

            # No superar 5
            if num > 5:
                print("El valor no puede ser mayor que 5.")
                continue

            # Validar sólo 1 decimal si viene decimal
            if "." in valor:
                parte_decimal = valor.split(".")[1]
                if len(parte_decimal) != 1:
                    print("Solo se permite un decimal (ejemplo: 4.7).")
                    continue

            return num

        print("Debe ingresar un número decimal válido.")
        

# -------------------------------
# 7. Validación DNI
# -------------------------------
def input_dni(texto="DNI: "):
    while True:
        dni = input(texto)

        # Validar longitud exacta
        if len(dni) != 8:
            print("El DNI debe tener exactamente 8 dígitos.")
            continue

        # Validar que sean solo números
        if not dni.isdigit():
            print("El DNI solo puede contener números.")
            continue

        return dni