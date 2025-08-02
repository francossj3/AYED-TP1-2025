# AyED TP2 - UTN 2025
# Alumnos: Franco Abramor, Alejandro Ciaralucci, Fabricio Pretel, Iván Torres

# Declaracion de variables
#string: usuarios, claves, tipos_usuario, nombres_usuarios, aerolineas_nombre, aerolineas_estado, vuelos_origen, vuelos_destino, vuelos_fecha, vuelos_hora, vuelos_estado, promociones_desc, promociones_estado, asientos, reservas_estado, novedades_texto, novedades_fecha_pub, novedades_fecha_exp
#int: MAX_USUARIOS, MAX_VUELOS, MAX_AEROLINEAS, FILAS_POR_VUELO, COLUMNAS_AVION, MAX_RESERVAS, vuelos_codigo, vuelos_aerolinea, vuelos_precio, promociones_codigo, promociones_dcto, promociones_aerolinea, reservas_usuario, reservas_codigo, reservas_vuelo, cant_vuelos, cant_reservas


#Importamos las librerias necesarias
import os
import random
from datetime import datetime
from pwinput import pwinput

#Constantes
MAX_USUARIOS = 10
MAX_VUELOS = 20
MAX_AEROLINEAS = 5
FILAS_POR_VUELO = 40
COLUMNAS_AVION = 6
MAX_RESERVAS = 100

#correciondeltp1
def fecha_valida(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

usuarios = ["admin@ventaspasajes777.com", "ceo1@ventaspasajes777.com", "ceo2@ventaspasajes777.com", "usuario1@ventaspasajes777.com", "usuario2@ventaspasajes777.com", "", "", "", "", ""]
claves = ["admin123", "ceo123", "ceo456", "usuario123", "usuario456", "", "", "", "", ""]
tipos_usuario = ["administrador", "ceo", "ceo", "usuario", "usuario", "", "", "", "", ""]
nombres_usuarios = ["Admin", "CEO1", "CEO2", "Usuario1", "Usuario2", "", "", "", "", ""]

aerolineas_nombre = ["Aerolineas Argentinas", "LATAM", "Flybondi", "GOL", "Iberia"]
aerolineas_codigo = [0, 1, 2, 3, 4]
aerolineas_estado = ["A"] * MAX_AEROLINEAS

cant_vuelos = 0
vuelos_codigo = [0]*MAX_VUELOS
vuelos_aerolinea = [0]*MAX_VUELOS
vuelos_origen = [""]*MAX_VUELOS
vuelos_destino = [""]*MAX_VUELOS
vuelos_fecha = [""]*MAX_VUELOS
vuelos_hora = [""]*MAX_VUELOS
vuelos_precio = [0]*MAX_VUELOS
vuelos_estado = [""]*MAX_VUELOS

promociones_codigo = [0]*MAX_VUELOS
promociones_desc = [""]*MAX_VUELOS
promociones_dcto = [0]*MAX_VUELOS
promociones_estado = [""]*MAX_VUELOS
promociones_aerolinea = [0]*MAX_VUELOS

asientos = [[random.choice(["L", "O", "R"]) for _ in range(COLUMNAS_AVION)] for _ in range(FILAS_POR_VUELO * MAX_VUELOS)]

reservas_usuario = [0]*MAX_RESERVAS
reservas_codigo = [0]*MAX_RESERVAS
reservas_vuelo = [0]*MAX_RESERVAS
reservas_estado = [""]*MAX_RESERVAS
cant_reservas = 0

novedades_texto = [
    "Debido a tareas de mantenimiento, el aeropuerto permanecerá cerrado el próximo domingo.",
    "¡Felices fiestas! Ofrecemos un 10% de descuento adicional en todos los vuelos para pasajeros Premium.",
    "Recordamos a los pasajeros que deben llegar al aeropuerto con al menos 3 horas de anticipación para vuelos internacionales."
]
novedades_fecha_pub = ["01/06/2025", "01/12/2025", "01/01/2025"]
novedades_fecha_exp = ["30/06/2025", "31/12/2025", "31/12/2025"]

def mostrar_cartel(texto):
    print("\n" + "="*60)
    print(f"{texto.center(60)}")
    print("="*60)

def cartel_construccion():
    print("\n" + "#"*60)
    print("#" + " "*58 + "#")
    print("#" + " EN CONSTRUCCIÓN...".center(58) + "#")
    print("#" + " "*58 + "#")
    print("#"*60 + "\n")

#login
def login():
    mostrar_cartel("INICIAR SESIÓN")
    intentos = 0
    while intentos < 3:
        correo = input("Correo: ").lower()
        clave = pwinput("Contraseña: ")
        for i in range(MAX_USUARIOS):
            if usuarios[i] == correo and claves[i] == clave:
                print(f"Bienvenido/a {nombres_usuarios[i]} ({tipos_usuario[i]})")
                return i
        print("Credenciales incorrectas. Intente nuevamente.")
        intentos += 1
    print("Demasiados intentos fallidos.")
    return -1

#registro
def registrar_usuario():
    mostrar_cartel("REGISTRARSE")
    for i in range(MAX_USUARIOS):
        if usuarios[i] == "":
            usuarios[i] = input("Nuevo correo: ").lower()
            claves[i] = pwinput("Nueva contraseña: ")
            nombres_usuarios[i] = input("Nombre completo: ")
            tipos_usuario[i] = "usuario"
            print("Usuario registrado exitosamente.")
            return
    print("No hay espacio para nuevos usuarios.")

#menus

def menu_administrador():
    opcion = ""
    while opcion != "4":
        mostrar_cartel("MENÚ ADMINISTRADOR")
        print("1. Gestión de aerolíneas")
        print("2. Crear aerolínea")
        print("3. Modificar aerolínea")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            mostrar_aerolineas()
        elif opcion == "2":
            crear_aerolinea()
        elif opcion == "3":
            modificar_aerolinea()
        elif opcion != "4":
            cartel_construccion()

def menu_ceo():
    opcion = ""
    while opcion != "5":
        mostrar_cartel("MENÚ CEO")
        print("1. Gestión de vuelos")
        print("2. Crear vuelo")
        print("3. Modificar vuelo")
        print("4. Eliminar vuelo")
        print("5. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            listar_vuelos_por_aerolinea()
        elif opcion == "2":
            crear_vuelo()
        elif opcion == "3":
            modificar_vuelo()
        elif opcion == "4":
            eliminar_vuelo()
        elif opcion != "5":
            cartel_construccion()

def menu_usuario():
    opcion = ""
    while opcion != "3":
        mostrar_cartel("MENÚ USUARIO")
        print("1. Buscar vuelos")
        print("2. Buscar asientos")
        print("3. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            buscar_vuelos()
        elif opcion == "2":
            buscar_asientos()
        elif opcion != "3":
            cartel_construccion()

#menuprincipal

def menu_principal():
    while True:
        mostrar_cartel("VENTAS PASAJES 777 - TP2")
        print("1. Iniciar sesión")
        print("2. Registrarme")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pos_usuario = login()
            if pos_usuario != -1:
                tipo = tipos_usuario[pos_usuario]
                if tipo == "administrador":
                    menu_administrador()
                elif tipo == "ceo":
                    menu_ceo()
                elif tipo == "usuario":
                    menu_usuario()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            return
        else:
            print("Opción inválida.")

#funcionesadmin
def mostrar_aerolineas():
    mostrar_cartel("LISTADO DE AEROLÍNEAS")
    for i in range(MAX_AEROLINEAS):
        estado = "Activa" if aerolineas_estado[i] == "A" else "Baja"
        print(f"Código: {aerolineas_codigo[i]} | Nombre: {aerolineas_nombre[i]} | Estado: {estado}")

def crear_aerolinea():
    mostrar_cartel("CREAR AEROLÍNEA")
    for i in range(MAX_AEROLINEAS):
        if aerolineas_estado[i] == "B":
            nombre = input("Ingrese el nombre de la nueva aerolínea: ")
            aerolineas_nombre[i] = nombre
            aerolineas_estado[i] = "A"
            print("Aerolínea creada exitosamente.")
            return
    print("No hay lugar para crear nuevas aerolíneas.")

def modificar_aerolinea():
    mostrar_cartel("MODIFICAR AEROLÍNEA")
    mostrar_aerolineas()
    cod = int(input("Ingrese el código de la aerolínea a modificar: "))
    if 0 <= cod < MAX_AEROLINEAS and aerolineas_estado[cod] == "A":
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        aerolineas_nombre[cod] = nuevo_nombre
        print("Nombre modificado con éxito.")
    else:
        print("Código inválido o aerolínea dada de baja.")

#funcionesceo

def buscar_aerolinea(cod):
    for i in range(MAX_AEROLINEAS):
        if aerolineas_codigo[i] == cod and aerolineas_estado[i] == "A":
            return i
    return -1

def mostrar_vuelos():
    mostrar_cartel("LISTADO DE VUELOS")
    for i in range(cant_vuelos):
        if vuelos_estado[i] == "A":
            print(f"Código: {i} | Aerolínea: {aerolineas_nombre[vuelos_aerolinea[i]]} | Origen: {vuelos_origen[i]} | Destino: {vuelos_destino[i]} | Fecha: {vuelos_fecha[i]} | Hora: {vuelos_hora[i]} | Precio: ${vuelos_precio[i]}")

def crear_vuelo():
    global cant_vuelos
    opcion = "s"
    while opcion == "s" and cant_vuelos < MAX_VUELOS:
        mostrar_cartel("CREAR VUELO")
        ver = input("¿Desea ver los vuelos ya cargados? (s/n): ").lower()
        if ver == "s":
            mostrar_vuelos()

        cod_aero = int(input("Código de aerolínea: "))
        pos = buscar_aerolinea(cod_aero)
        if pos == -1:
            print("Código inválido.")
        else:
            origen = input("Origen: ").strip().upper()
            destino = input("Destino: ").strip().upper()
            if origen == "" or destino == "" or origen == destino:
                print("Origen y destino deben ser distintos y no vacíos.")
                continue
            vuelos_codigo[cant_vuelos] = cant_vuelos
            vuelos_aerolinea[cant_vuelos] = cod_aero
            vuelos_origen[cant_vuelos] = origen
            vuelos_destino[cant_vuelos] = destino
            vuelos_fecha[cant_vuelos] = input("Fecha (dd/mm/aaaa): ")
            vuelos_hora[cant_vuelos] = input("Hora (HH:MM): ")
            precio = int(input("Precio: "))
            if precio <= 0:
                print("El precio debe ser mayor a cero.")
                continue
            vuelos_precio[cant_vuelos] = precio
            vuelos_estado[cant_vuelos] = "A"
            cant_vuelos += 1
            print("Vuelo creado exitosamente.")
        opcion = input("¿Desea cargar otro vuelo? (s/n): ").lower()

    if cant_vuelos == MAX_VUELOS:
        print("No hay más espacio para vuelos.")

def modificar_vuelo():
    mostrar_cartel("MODIFICAR VUELO")
    mostrar_vuelos()
    cod = int(input("Ingrese el código del vuelo a modificar: "))
    if 0 <= cod < cant_vuelos:
        if vuelos_estado[cod] == "B":
            activar = input("El vuelo está dado de baja. ¿Desea activarlo? (s/n): ").lower()
            if activar == "s":
                vuelos_estado[cod] = "A"
        if vuelos_estado[cod] == "A":
            vuelos_origen[cod] = input("Nuevo origen: ").upper()
            vuelos_destino[cod] = input("Nuevo destino: ").upper()
            vuelos_fecha[cod] = input("Nueva fecha (dd/mm/aaaa): ")
            vuelos_hora[cod] = input("Nueva hora (HH:MM): ")
            vuelos_precio[cod] = int(input("Nuevo precio: "))
            print("Vuelo modificado.")
    else:
        print("Código inválido.")

def eliminar_vuelo():
    mostrar_cartel("ELIMINAR VUELO")
    mostrar_vuelos()
    cod = int(input("Ingrese el código del vuelo a eliminar: "))
    if 0 <= cod < cant_vuelos and vuelos_estado[cod] == "A":
        confirmar = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()
        if confirmar == "s":
            vuelos_estado[cod] = "B"
            print("Vuelo eliminado lógicamente.")
    else:
        print("Código inválido o vuelo ya dado de baja.")

def listar_vuelos_por_aerolinea():
    mostrar_cartel("REPORTE DE VUELOS VIGENTES POR AEROLÍNEA")
    conteo = [0] * MAX_AEROLINEAS
    hoy = datetime.now().strftime("%d/%m/%Y")
    for i in range(cant_vuelos):
        if vuelos_estado[i] == "A" and vuelos_fecha[i] > hoy:
            conteo[vuelos_aerolinea[i]] += 1

    orden = sorted(range(MAX_AEROLINEAS), key=lambda x: conteo[x], reverse=True)

    print(f"{'POSICIÓN':<10}{'AEROLÍNEA':<25}{'CANTIDAD DE VUELOS'}")
    print("-" * 60)
    for pos, i in enumerate(orden):
        print(f"{pos:<10}{aerolineas_nombre[i]:<25}{conteo[i]}")
    print("-" * 60)
    print(f"TOTAL DE VUELOS VIGENTES: {sum(conteo)}")
    print(f"Aerolínea con MAYOR cantidad de vuelos: {aerolineas_nombre[orden[0]]} ({conteo[orden[0]]})")
    print(f"Aerolínea con MENOR cantidad de vuelos: {aerolineas_nombre[orden[-1]]} ({conteo[orden[-1]]})")

#funcionesusuario
def buscar_vuelos():
    mostrar_cartel("BUSCAR VUELOS")
    fecha_buscada = input("Ingrese la fecha deseada (dd/mm/aaaa): ")
    hoy = datetime.now().strftime("%d/%m/%Y")
    encontrados = 0
    for i in range(cant_vuelos):
        if vuelos_estado[i] == "A" and vuelos_fecha[i] >= hoy:
            print(f"Código: {vuelos_codigo[i]} | Aerolínea: {aerolineas_nombre[vuelos_aerolinea[i]]} | Origen: {vuelos_origen[i]} | Destino: {vuelos_destino[i]} | Fecha: {vuelos_fecha[i]} | Hora: {vuelos_hora[i]} | Precio: ${vuelos_precio[i]}")
            encontrados += 1
    print(f"Total de vuelos disponibles: {encontrados}")

def buscar_asientos():
    mostrar_cartel("BUSCAR ASIENTOS")
    cod_vuelo = int(input("Ingrese el código del vuelo: "))
    if 0 <= cod_vuelo < cant_vuelos and vuelos_estado[cod_vuelo] == "A":
        print("\nAsientos del vuelo (L: Libre, O: Ocupado, R: Reservado):\n")
        for fila in range(FILAS_POR_VUELO):
            fila_real = cod_vuelo * FILAS_POR_VUELO + fila
            print(f"Fila {fila+1:02d}: {asientos[fila_real]}")
        input("\nPresione ENTER para volver al menú...")
    else:
        print("Código de vuelo inválido o vuelo no activo.")
