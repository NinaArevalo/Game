import getpass
from auth import hash_password

def modificar_perfil(registrados, username_act):
    for usuario in registrados:
        if usuario['Usuario'] == username_act:
            perfil = usuario
            break
    else:
        print("Usuario no encontrado.")
        return
    
    while True:
        print("\n--- Panel de Modificación de Perfil ---")
        print("1. Cambiar nombre de usuario")
        print("2. Cambiar contraseña")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                nuevo_nombre = input("Nuevo nombre de usuario: ")
                perfil['Usuario'] = nuevo_nombre
                print("Nombre de usuario actualizado.")
            case "2":
                nueva_pass = getpass.getpass("Nueva contraseña: ")
                perfil['Password'] = hash_password(nueva_pass)
                print("Contraseña actualizada.")
            case "3":
                print("Saliste del panel de modificación.")
                break
            case _:
                print("Opción inválida, intenta de nuevo.")
