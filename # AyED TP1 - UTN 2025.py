# AyED TP1 - UTN 2025
# Alumnos: Abramor Franco (comisión 8) - Ciaralucci Alejandro (comisión 8) - Pretel Fabricio (comisión 2) - Ivan Torres (se cambio de grupo a ultimo momento con el codigo casi terminado y no pudimos conseguir otro integrante)
#Declaración de variables
#integer:  opcion, opcion_submenu, cod_novedad1, cod_novedad2, cod_novedad3
#string:   nombre_aerolinea, codigo_iata, descripcion_aerolinea, cod_pais, usuario_admin, clave_admin, texto_novedad1, texto_novedad2, texto_novedad3, fecha_publicacion1, fecha_publicacion2, fecha_publicacion, fecha_expiracion1, fecha_expiracion2, fecha_expiracion3

# Importamos las librerias necesarias
import os
from pwinput import pwinput 

usuario_admin = "administrador@ventaspasajes.com"
clave_admin = "administrador"

# Variables para contar aerolíneas separadas por país
contador_arg = 0;

contador_chi = 0;

contador_bra = 0;

# Variables para novedades
cod_novedad1 = 1;
texto_novedad1 = "Debido a tareas de mantenimiento, el aeropuerto permanecerá cerrado el próximo domingo";
fecha_publicacion1 = "01/06/2025";
fecha_expiracion1 = "30/06/2025";

cod_novedad2 = 2;
texto_novedad2 = "¡Felices fiestas! Ofrecemos un 10% de descuento adicional en todos los vuelos para pasajeros Premium";
fecha_publicacion2 = "01/12/2025";
fecha_expiracion2 = "31/12/2025";

cod_novedad3 = 3;
texto_novedad3 = "Recordamos a los pasajeros que deben llegar al aeropuerto con al menos 3 horas de anticipación para vuelos internacionales";
fecha_publicacion3 = "01/01/2025";
fecha_expiracion3 = "31/12/2025";

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_en_construccion():
    print("\nEn construcción...\n")

def mostrar_menu_principal():
    print("\n----- MENÚ PRINCIPAL -----")
    print("1. Gestión de Aerolíneas")
    print("2. Aprobar/Denegar Promociones")
    print("3. Gestión de Novedades")
    print("4. Reportes")
    print("5. Salir")

def mostrar_submenu_aerolineas():
    print("\n----- GESTIÓN DE AEROLÍNEAS -----")
    print("a. Crear Aerolínea")
    print("b. Modificar Aerolínea")
    print("c. Eliminar Aerolínea")
    print("d. Volver")

def mostrar_submenu_novedades():
    print("\n----- GESTIÓN DE NOVEDADES -----")
    print("a. Crear Novedad")
    print("b. Modificar Novedad")
    print("c. Eliminar Novedad")
    print("d. Ver Novedades")
    print("e. Volver")

def mostrar_submenu_reportes():
    print("\n----- REPORTES -----")
    print("a. Reporte de Ventas")
    print("b. Reporte de Vuelos")
    print("c. Reporte de Usuarios")
    print("d. Volver")

def crear_aerolinea():

    global contador_arg, contador_chi, contador_bra

    seguir = "s"
    while seguir.lower() == "s":
        limpiar_pantalla()
        print("\n----- CREAR AEROLÍNEA -----")

        nombre_valido = False
        while not nombre_valido:
            nombre = input("Ingrese el nombre de la aerolínea: ")
            if nombre.strip() != "":
                nombre_valido = True
            else:
                print("El nombre no puede estar vacío.")

        codigo_valido = False
        while not codigo_valido:
            codigo_iata = input("Ingrese el código IATA (3 caracteres): ")
            if len(codigo_iata) == 3 and codigo_iata.isalpha():
                codigo_iata = codigo_iata.upper()
                codigo_valido = True
            else:
                print("El código IATA debe tener exactamente 3 caracteres alfabéticos.")

        descripcion = input("Ingrese la descripción de la aerolínea a crear: ")

        pais_valido = False
        while not pais_valido:
            pais = input("Ingrese el código de país (ARG, CHI o BRA): ").upper()
            if pais in ["ARG", "CHI", "BRA"]:
                pais_valido = True
            else:
                print("Código de país inexistente. Debe ser ARG, CHI o BRA.")

        # Actualizamos contadores por país
        if pais == "ARG":
            contador_arg += 1
        elif pais == "CHI":
            contador_chi += 1
        elif pais == "BRA":
            contador_bra += 1

        print("\nAerolínea creada exitosamente!")

        # Preguntar si desea seguir
        seguir = input("\n¿Desea ingresar otra aerolínea? (S/N): ")
        while seguir.lower() not in ["s", "n"]:
            seguir = input("Opción inválida. Ingrese 'S' para continuar o 'N' para salir: ")

    # Mostrar estadísticas
    paises = {
        "ARG": contador_arg,
        "CHI": contador_chi,
        "BRA": contador_bra
    }

    max_pais = max(paises, key=paises.get)
    min_pais = min(paises, key=paises.get)

    print("\nEstadísticas de aerolíneas por país:")
    print(f"ARG: {contador_arg} aerolíneas")
    print(f"CHI: {contador_chi} aerolíneas")
    print(f"BRA: {contador_bra} aerolíneas")
    print(f"\nPaís con más aerolíneas: {max_pais} ({paises[max_pais]})")
    print(f"País con menos aerolíneas: {min_pais} ({paises[min_pais]})")


def ver_novedades():
    print("\n----- NOVEDADES DEL SISTEMA -----");
    print("---------------------------------------------------------------------");
    print(f"Código: {cod_novedad1}");
    print(f"Texto: {texto_novedad1}");
    print(f"Fecha de publicación: {fecha_publicacion1}");
    print(f"Fecha de expiración: {fecha_expiracion1}");
    print("---------------------------------------------------------------------");
    print(f"Código: {cod_novedad2}")
    print(f"Texto: {texto_novedad2}");
    print(f"Fecha de publicación: {fecha_publicacion2}");
    print(f"Fecha de expiración: {fecha_expiracion2}");
    print("---------------------------------------------------------------------");
    print(f"Código: {cod_novedad3}")
    print(f"Texto: {texto_novedad3}");
    print(f"Fecha de publicación: {fecha_publicacion3}");
    print(f"Fecha de expiración: {fecha_expiracion3}");
    print("---------------------------------------------------------------------");

def modificar_novedad():
    global texto_novedad1, texto_novedad2, texto_novedad3
    global fecha_publicacion1, fecha_publicacion2, fecha_publicacion3
    global fecha_expiracion1, fecha_expiracion2, fecha_expiracion3

    ver_novedades()

    codigo_valido = False
    while not codigo_valido:
        try:
            codigo = int(input("\nIngrese el código de la novedad a modificar (1-3): "))
            if 1 <= codigo <= 3:
                codigo_valido = True
            else:
                print("Código inválido. Debe ser 1, 2 o 3.");
        except ValueError:
            limpiar_pantalla()
            print("Debe ingresar un número válido.");
             

    nuevo_texto = input("Ingrese el nuevo texto de la novedad: ")
    nueva_fecha_pub = input("Ingrese la nueva fecha de publicación (DD/MM/AAAA): ")
    nueva_fecha_exp = input("Ingrese la nueva fecha de expiración (DD/MM/AAAA): ")

    if codigo == 1:
        texto_novedad1 = nuevo_texto
        fecha_publicacion1 = nueva_fecha_pub
        fecha_expiracion1 = nueva_fecha_exp
    elif codigo == 2:
        texto_novedad2 = nuevo_texto
        fecha_publicacion2 = nueva_fecha_pub
        fecha_expiracion2 = nueva_fecha_exp
    elif codigo == 3:
        texto_novedad3 = nuevo_texto
        fecha_publicacion3 = nueva_fecha_pub
        fecha_expiracion3 = nueva_fecha_exp

    print("\nNovedad modificada exitosamente!")
    ver_novedades()

def autenticar_admin():
    intentos = 3

    while intentos > 0:
        print("\n----- INICIO DE SESIÓN -----")
        usuario = input("ingrese su Usuario: ")
        print( end="", flush=True);
        clave = pwinput("ingrese su Contraseña: ", mask="*")


        if usuario == usuario_admin and clave == clave_admin:
            return True

        intentos -= 1
        if intentos > 0:
            print(f"\nCredenciales incorrectas. Le quedan {intentos} intentos.");
        else:
            print("\nHa excedido el número máximo de intentos. Saliendo del sistema...");
            return False

    return False

def gestionar_aerolineas():
    opcion = ""

    while opcion != "d":
        
        mostrar_submenu_aerolineas()
        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a":
            limpiar_pantalla()
            crear_aerolinea()
        elif opcion == "b":
            limpiar_pantalla()
            mostrar_en_construccion()
        elif opcion == "c":
            limpiar_pantalla()
            mostrar_en_construccion()
        elif opcion == "d":
            print("\nVolviendo al menú principal...");
        else:
            print("\nOpción inválida. Intente nuevamente.");

def gestionar_novedades():
    opcion = ""
    limpiar_pantalla()
    while opcion != "e":
        
        mostrar_submenu_novedades()
        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a":
            limpiar_pantalla()
            mostrar_en_construccion()
        elif opcion == "b":
            limpiar_pantalla()
            modificar_novedad()
        elif opcion == "c":
            limpiar_pantalla()
            mostrar_en_construccion()
        elif opcion == "d":
            limpiar_pantalla()
            ver_novedades()
        elif opcion == "e":
            limpiar_pantalla()
            print("\nVolviendo al menú principal...");
        else:
            print("\nOpción inválida. Intente nuevamente.");

def generar_reportes():
    opcion = ""

    while opcion != "d":
        mostrar_submenu_reportes()
        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a":
            limpiar_pantalla()
            mostrar_en_construccion()
        elif opcion == "b":
            limpiar_pantalla()
            mostrar_en_construccion()
        elif opcion == "c":
            limpiar_pantalla()
            mostrar_en_construccion()
        elif opcion == "d":
            limpiar_pantalla()
            print("\nVolviendo al menú principal...");
        else:
            print("\nOpción inválida. Intente nuevamente.");

def main():
    if not autenticar_admin():
        return

    opcion = 0

    while opcion != 5:
        
        mostrar_menu_principal()

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("\nDebe ingresar un número válido.");
            continue

        if opcion == 1:
            limpiar_pantalla()
            gestionar_aerolineas()
        elif opcion == 2:
            limpiar_pantalla()
            mostrar_en_construccion()
        elif opcion == 3:
            limpiar_pantalla()
            gestionar_novedades()
        elif opcion == 4:
            limpiar_pantalla()
            generar_reportes()
        elif opcion == 5:
            print("\nGracias por usar el sistema. ¡Hasta pronto!");
        else:
            print("\nOpción inválida. Intente nuevamente.");

if __name__ == "__main__":
    main()