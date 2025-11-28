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
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            cuit = input("CUIT: ")
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
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            numero = input("Número sucursal: ")
            id_cine = input("ID cine: ")
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
            id_sucursal = input("ID Sucursal: ")
            numero_sala = input("Número de sala: ")
            capacidad = input("Capacidad: ")
            tipo = input("Tipo (2D/3D/4D): ")
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
            id_sala = input("ID sala: ")
            fila = input("Fila (A-Z): ")
            num = input("Número asiento: ")
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
            titulo = input("Título: ")
            reparto = input("Reparto: ")
            sinopsis = input("Sinopsis: ")
            dur = input("Duración: ")
            genero = input("Género: ")
            clasif = input("Clasificación: ")
            val = input("Valoración (0-5): ")
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
            id_p = input("ID película: ")
            id_s = input("ID sala: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            h_ini = input("Hora inicio (HH:MM): ")
            h_fin = input("Hora fin (HH:MM): ")
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
            nom = input("Nombre: ")
            ape = input("Apellido: ")
            dni = input("DNI: ")
            fn = input("Fecha nacimiento (YYYY-MM-DD): ")
            tel = input("Teléfono: ")
            mail = input("Email: ")
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
            nombre = input("Nombre tarifa: ")
            precio = input("Precio fijo: ")
            desc = input("Valor descuento: ")
            tipo = input("Tipo descuento (Porcentual/Fijo): ")
            cat = input("Categoría base: ")
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
            id_cliente = input("ID cliente: ")
            total = input("Total: ")
            pago = input("Tipo pago('Efectivo', 'Tarjeta', 'Transferencia'): ")
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
            id_venta = input("ID venta: ")
            id_funcion = input("ID función: ")
            id_asiento = input("ID asiento: ")
            id_tarifa = input("ID tarifa: ")
            precio = input("Precio final: ")
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
# MODIFICAR REGISTRO
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
    # 2. Películas disponibles en esa sucursal
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
    # 4. Asientos disponibles
    # ------------------------------
    asientos = asiento_m.get_disponibles(id_funcion)

    print("\nAsientos disponibles:")
    for a in asientos:
        print(f"{a['id_asiento']} - Fila {a['fila']} Asiento {a['numero_asiento']}")

    id_asiento = input("Seleccione asiento: ")

    # ------------------------------
    # 5. Elegir Tarifa
    # ------------------------------
    tarifas = tarifa_m.list_all()
    print("\nTarifas:")
    for t in tarifas:
        print(f"{t['id_tarifa']}. {t['nombre']} – ${t['precio_fijo']}")

    id_tarifa = input("Seleccione tarifa: ")

    # ------------------------------
    # 6. Cliente (registrar o recuperar)
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
        id_cliente = cliente['id_cliente']
    else:
        id_cliente = cliente['id_cliente']

    # ------------------------------
    # 7. Crear Venta
    # ------------------------------
    hoy = date.today()
    tarifa = tarifa_m.get_by_id(id_tarifa)
    precio = tarifa["precio_fijo"]
    
    tipo_pago = input("Tipo de pago ('Efectivo', 'Tarjeta', 'Transferencia'): ")
    venta_m.create(id_cliente, hoy, precio, tipo_pago)
    id_venta = venta_m.list_end_id()

    # ------------------------------
    # 8. Crear Entrada
    # ------------------------------
    entrada_m.create(id_venta, id_funcion, id_asiento, id_tarifa, precio)

    # ------------------------------
    # 9. Bloquear Asiento
    # ------------------------------
    asiento_m.update(id_asiento, {"estado": "no disponible"})

    print("\n Compra realizada con éxito!")


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