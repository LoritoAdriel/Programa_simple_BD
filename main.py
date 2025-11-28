# main.py
from database import Database
from models.cine import Cine
from models.sucursal import Sucursal
from models.sala import Sala
from models.asiento import Asiento
from models.pelicula import Pelicula
from models.funcion import Funcion
from models.cliente import Cliente
from models.venta import Venta
from models.tarifa import Tarifa
from models.entrada import Entrada
from models.validaciones import input_entero, input_fecha, input_hora, input_id_valido, input_no_vacio, input_opcion, input_valoracion, input_dni

from datetime import date


# ---------------------------
#  CONEXIÓN A LA BASE DE DATOS
# ---------------------------

DB = Database(
    host='localhost',
    user='root',
    password='root',
    database='Cine'
)

# Instancias de modelos
cine_m = Cine(DB)
sucursal_m = Sucursal(DB)
sala_m = Sala(DB)
asiento_m = Asiento(DB)
pelicula_m = Pelicula(DB)
funcion_m = Funcion(DB)
cliente_m = Cliente(DB)
venta_m = Venta(DB)
tarifa_m = Tarifa(DB)
entrada_m = Entrada(DB)


# -----------------------------
# Menús
# -----------------------------

def menu_cines():
    while True:
        print("\n--- MENÚ CINES ---")
        print("1. Agregar cine")
        print("2. Listar cines")
        print("3. Actualizar cine")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            nombre = input_no_vacio("Nombre: ")
            direccion = input_no_vacio("Dirección: ")
            cuit = input_entero("CUIT: ")
            cine_m.create(nombre, direccion, cuit)
        elif op == '2':
            for c in cine_m.list_all():
                print(c)
        elif op == '3':
            actualizar_generico(cine_m, "id_cine")
        elif op == '0':
            break


def menu_sucursales():
    while True:
        print("\n--- MENÚ SUCURSALES ---")
        print("1. Agregar sucursal")
        print("2. Listar sucursales")
        print("3. Actualizar sucursal")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            nombre = input_no_vacio("Nombre: ")
            direccion = input_no_vacio("Dirección: ")
            numero = input_entero("Número sucursal: ")

            ids_cine = [c["id_cine"] for c in cine_m.list_all()]
            id_cine = input_id_valido("ID cine: ", ids_cine)

            sucursal_m.create(nombre, direccion, numero, id_cine)
        elif op == '2':
            for s in sucursal_m.list_all():
                print(s)
        elif op == '3':
            actualizar_generico(sucursal_m, "id_sucursal")
        elif op == '0':
            break


def menu_salas():
    while True:
        print("\n--- MENÚ SALAS ---")
        print("1. Agregar sala")
        print("2. Listar salas")
        print("3. Actualizar sala")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            ids_sucursal = [s["id_sucursal"] for s in sucursal_m.list_all()]
            id_sucursal = input_id_valido("ID Sucursal: ", ids_sucursal)

            numero_sala = input_entero("Número de sala: ")
            capacidad = input_entero("Capacidad: ")
            tipo = input_opcion("Tipo (2D/3D/4D): ", ["2D", "3D", "4D"])

            sala_m.create(id_sucursal, numero_sala, capacidad, tipo)
        elif op == '2':
            for s in sala_m.list_all():
                print(s)
        elif op == '3':
            actualizar_generico(sala_m, "id_sala")
        elif op == '0':
            break


def menu_asientos():
    while True:
        print("\n--- MENÚ ASIENTOS ---")
        print("1. Agregar asiento")
        print("2. Listar asientos")
        print("3. Actualizar asiento")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            ids_salas = [s["id_sala"] for s in sala_m.list_all()]
            id_sala = input_id_valido("ID sala: ", ids_salas)
            
            fila = input("Fila (A-Z): ").upper()
            if not (len(fila) == 1 and 'A' <= fila <= 'Z'):
                print("La fila debe ser una letra entre A y Z.")
                continue
            
            num = input_entero("Número asiento: ")
            
            if asiento_m.exists(id_sala, fila, num):
                print("Ya existe un asiento en esa sala con esa fila y número.")
                continue
            asiento_m.create(id_sala, fila, num)
        elif op == '2':
            for a in asiento_m.list_all():
                print(a)
        elif op == '3':
            actualizar_generico(asiento_m, "id_asiento")
        elif op == '0':
            break


def menu_peliculas():
    while True:
        print("\n--- MENÚ PELÍCULAS ---")
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Actualizar pelicula")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            titulo = input_no_vacio("Título: ")
            reparto = input_no_vacio("Reparto: ")
            sinopsis = input_no_vacio("Sinopsis: ")
            dur = input_entero("Duración (minutos): ")
            genero = input_no_vacio("Género: ")
            clasif = input_no_vacio("Clasificación: ")
            val = input_valoracion("Valoración (0-5): ")
            pelicula_m.create(titulo, reparto, sinopsis, dur, genero, clasif, val)
        elif op == '2':
            for p in pelicula_m.list_all():
                print(p)
        elif op == '3':
            actualizar_generico(pelicula_m, "id_pelicula")
        elif op == '0':
            break


def menu_funciones():
    while True:
        print("\n--- MENÚ FUNCIONES ---")
        print("1. Agregar función")
        print("2. Listar funciones")
        print("3. Actualizar funcion")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            ids_pelis = [p["id_pelicula"] for p in pelicula_m.list_all()]
            id_p = input_id_valido("ID película: ", ids_pelis)

            ids_salas = [s["id_sala"] for s in sala_m.list_all()]
            id_s = input_id_valido("ID sala: ", ids_salas)

            fecha = input_fecha("Fecha (YYYY-MM-DD): ")
            h_ini = input_hora("Hora inicio (HH:MM): ")
            h_fin = input_hora("Hora fin (HH:MM): ")
            funcion_m.create(id_p, id_s, fecha, h_ini, h_fin)
        elif op == '2':
            for f in funcion_m.list_all():
                print(f)
        elif op == '3':
            actualizar_generico(funcion_m, "id_funcion")
        elif op == '0':
            break


def menu_clientes():
    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Actualizar cliente")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            nom = input_no_vacio("Nombre: ")
            ape = input_no_vacio("Apellido: ")
            dni = input_dni()
            fn = input_fecha("Fecha nacimiento (YYYY-MM-DD): ")
            tel = input_entero("Teléfono: ")
            mail = input_no_vacio("Email: ")
            cliente_m.create(nom, ape, dni, fn, tel, mail)
        elif op == '2':
            for c in cliente_m.list_all():
                print(c)
        elif op == '3':
            actualizar_generico(cliente_m, "id_cliente")
        elif op == '0':
            break


def menu_tarifas():
    while True:
        print("\n--- MENÚ TARIFAS ---")
        print("1. Agregar tarifa")
        print("2. Listar tarifas")
        print("3. Actualizar tarifa")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            nombre = input_no_vacio("Nombre tarifa: ")
            precio = input_entero("Precio fijo: ")
            desc = input_entero("Valor descuento: ")
            tipo = input_opcion("Tipo descuento (Porcentual/Fijo): ",
                                ["Porcentual", "Fijo"])
            cat = input_opcion("Categoría base (Menor/Adulto/Jubilado): ",
                                ["Menor", "Adulto", "Jubilado"])
            tarifa_m.create(nombre, precio, desc, tipo, cat)
        elif op == '2':
            for t in tarifa_m.list_all():
                print(t)
        elif op == '3':
            actualizar_generico(tarifa_m, "id_tarifa")
        elif op == '0':
            break


def menu_ventas():
    while True:
        print("\n--- MENÚ VENTAS ---")
        print("1. Registrar venta simple")
        print("2. Listar ventas")
        print("3. Actualizar venta")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            ids_cliente = [s["id_cliente"] for s in cliente_m.list_all()]
            id_cliente = input_id_valido("ID cliente: ", ids_cliente)
            total = input_entero("Total: ")
            pago = input_opcion(
                "Tipo pago (Efectivo/Tarjeta/Transferencia): ",
                ["Efectivo", "Tarjeta", "Transferencia"]
            )
            venta_m.create(id_cliente, date.today(), total, pago)
        elif op == '2':
            for v in venta_m.list_all():
                print(v)
        elif op == '3':
            actualizar_generico(venta_m, "id_venta")
        elif op == '0':
            break


def menu_entradas():
    while True:
        print("\n--- MENÚ ENTRADAS ---")
        print("1. Registrar entrada")
        print("2. Listar entradas")
        print("3. Actualizar entrada")
        print("0. Volver")
        op = input("Opción: ")
        if op == '1':
            ids_venta = [c["id_venta"] for c in venta_m.list_all()]
            id_venta = input_id_valido("ID venta: ", ids_venta)
            ids_funcion = [c["id_funcion"] for c in funcion_m.list_all()]
            id_funcion = input_id_valido("ID función: ", ids_funcion)
            ids_asiento = [c["id_asiento"] for c in asiento_m.list_all()]
            id_asiento = input_id_valido("ID asiento: ", ids_asiento)
            ids_tarifa = [c["id_tarifa"] for c in tarifa_m.list_all()]
            id_tarifa = input_id_valido("ID tarifa: ", ids_tarifa)
            tarifa = tarifa_m.get_by_id(id_tarifa)
            precio = tarifa["precio_fijo"]
            entrada_m.create(id_venta, id_funcion, id_asiento, id_tarifa, precio)
        elif op == '2':
            for e in entrada_m.list_all():
                print(e)
        elif op == '3':
            actualizar_generico(entrada_m, "id_entrada")
        elif op == '0':
            break


# -----------------------------
# MODIFICAR REGISTRO
# -----------------------------

def actualizar_generico(modelo, id_campo):
    print("\n--- MODIFICAR REGISTRO ---")
    id_valor = input(f"Ingrese {id_campo}: ")

    registro = modelo.get_by_id(id_valor)

    if not registro:
        print("No existe un registro con ese ID.")
        return

    print("\nValores actuales:")
    for k, v in registro.items():
        print(f"{k}: {v}")

    print("\nIngrese los campos que desea modificar. Deje vacío para no cambiarlo.")

    nuevos_valores = {}

    for campo, valor_actual in registro.items():
        if campo == id_campo:
            continue
        nuevo = input(f"{campo} ({valor_actual}): ")

        if nuevo.strip() != "":
            nuevos_valores[campo] = nuevo

    if not nuevos_valores:
        print("No se modificó nada.")
        return

    modelo.update(id_valor, nuevos_valores)

    print("✔ Registro actualizado correctamente.")
    
    
# -----------------------------
# EMULAR COMPRA
# -----------------------------

def menu_compra():
    print("\n=== COMPRA DE ENTRADAS ===")

    # ------------------------------
    # 1. Seleccionar Sucursal
    # ------------------------------
    sucursales = sucursal_m.list_all()
    print("\nSucursales disponibles:")
    for s in sucursales:
        print(f"{s['id_sucursal']}. {s['nombre']} – {s['direccion']}")

    id_sucursal = input("Seleccione sucursal: ")

    # ------------------------------
    # 2. Películas disponibles
    # ------------------------------
    peliculas = sucursal_m.get_peliculas_disponibles(id_sucursal)
    print("\nPelículas disponibles:")
    for p in peliculas:
        print(f"{p['id_pelicula']}. {p['titulo']}")

    id_pelicula = input("Seleccione película: ")

    # ------------------------------
    # 3. Funciones disponibles
    # ------------------------------
    funciones = funcion_m.get_funciones(id_pelicula, id_sucursal)
    print("\nFunciones disponibles:")
    for f in funciones:
        print(f"{f['id_funcion']}. Sala {f['numero_sala']} - {f['fecha']} {f['hora_inicio']}")

    id_funcion = input("Seleccione función: ")

    # ------------------------------
    # 4. Selección de múltiples asientos
    # ------------------------------
    asientos_seleccionados = []

    while True:
        asientos = asiento_m.get_disponibles(id_funcion)
        print("\nAsientos disponibles:")
        for a in asientos:
            print(f"{a['id_asiento']} - Fila {a['fila']} Asiento {a['numero_asiento']}")

        id_asiento = input("Seleccione asiento: ")
        asientos_seleccionados.append(id_asiento)

        seguir = input("¿Desea elegir otro asiento? (s/n): ").lower()
        if seguir != "s":
            break

    # ------------------------------
    # 5. Elegir tarifa (una para todos)
    # ------------------------------
    tarifas = tarifa_m.list_all()
    print("\nTarifas:")
    for t in tarifas:
        print(f"{t['id_tarifa']}. {t['nombre']} – ${t['precio_fijo']}")

    id_tarifa = input("Seleccione tarifa: ")
    tarifa = tarifa_m.get_by_id(id_tarifa)
    precio_unitario = tarifa["precio_fijo"]

    # ------------------------------
    # 6. Cliente
    # ------------------------------
    dni = input("Ingrese DNI: ")
    cliente = cliente_m.get_by_dni(dni)

    if not cliente:
        print("Cliente no encontrado. Registrando nuevo...")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        email = input("Email: ")

        cliente_m.create(nombre, apellido, dni, None, None, email)
        cliente = cliente_m.get_by_dni(dni)

    id_cliente = cliente["id_cliente"]

    # ------------------------------
    # 7. Pago (al final)
    # ------------------------------
    total = precio_unitario * len(asientos_seleccionados)
    print(f"\nTotal a pagar por {len(asientos_seleccionados)} entrada(s): ${total}")

    tipo_pago = input("Tipo de pago (Efectivo/Tarjeta/Transferencia): ")

    # Crear la venta
    hoy = date.today()
    venta_m.create(id_cliente, hoy, total, tipo_pago)
    id_venta = venta_m.list_end_id()

    # ------------------------------
    # 8. Crear las entradas y bloquear asientos
    # ------------------------------
    for id_asiento in asientos_seleccionados:
        entrada_m.create(id_venta, id_funcion, id_asiento, id_tarifa, precio_unitario)
        asiento_m.update(id_asiento, {"estado": "no disponible"})

    print("\n¡Compra realizada con éxito!")


# -----------------------------
# MENÚ PRINCIPAL
# -----------------------------

def main():
    while True:
        print("\n===== SISTEMA DE CINE =====")
        print("1. Cines")
        print("2. Sucursales")
        print("3. Salas")
        print("4. Asientos")
        print("5. Películas")
        print("6. Funciones")
        print("7. Clientes")
        print("8. Ventas")
        print("9. Tarifas")
        print("10. Entradas")
        print("11. Emular compra")
        print("0. Salir")
        op = input("Opción: ")

        if op == '1': menu_cines()
        elif op == '2': menu_sucursales()
        elif op == '3': menu_salas()
        elif op == '4': menu_asientos()
        elif op == '5': menu_peliculas()
        elif op == '6': menu_funciones()
        elif op == '7': menu_clientes()
        elif op == '8': menu_ventas()
        elif op == '9': menu_tarifas()
        elif op == '10': menu_entradas()
        elif op == '11': menu_compra()
        elif op == '0': break
        else:
            print("Opción inválida")
            

if __name__ == '__main__':
    main()