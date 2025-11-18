from data import registrados
from auth import autenticacion_sesion, registrar_usuario
import getpass
import game

def login_user():
    opcion = ""
    while opcion != "3":
        print("\n1. Iniciar Sesion")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Ingresa la opción que deseas elegir: ")

        if opcion == "1":
            usuario = input("Ingresa tu usuario: ")
            password = getpass.getpass("Ingresa tu contraseña: ")
            if autenticacion_sesion(usuario, password, registrados):
                print(f"Bienvenido {usuario}")
                game.opciones_menu_pp(registrados, usuario)
            else:
                print("Usuario/Contraseña Incorrectos, vuelve a intentarlo")

        elif opcion == "2":
            usuario = input("Ingresa tu nombre de usuario: ")
            password = getpass.getpass("Ingresa tu contraseña: ")
            if registrar_usuario(usuario, password, registrados):
                print("Te registraste con éxito!")
            else:
                print("Error, usuario ya existente, inténtalo de nuevo")

        elif opcion == "3":
            print("Hasta luego!")
        else:
            print("Error, opción incorrecta")
login_user()
