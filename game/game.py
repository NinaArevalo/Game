from colorama import init, Fore, Style
init(autoreset=True)
from tienda import mostrar_tienda, compra_animales
from perfil import modificar_perfil
menu = True
def menu_principal(): 
    print(f"""
╔══════════════════════════════════════════╗
║                                          ║
║                                          ║
║ {Fore.CYAN}      ┌──────────────────────────┐      ║
║        │      MENU PRINCIPAL      │      ║
║        └──────────────────────────┘      ║
║                                          ║
║          1 ▸ Perfil                      ║
║          2 ▸ Granja                      ║
║          3 ▸ Tienda                      ║
║          4 ▸ Salir                       ║
║                                          ║
║           Ingrese una opcion             ║
╚══════════════════════════════════════════╝
""")
def opciones_menu_pp(registrados, usuario_act):
    global menu
    print(f"""{Fore.GREEN}
                        🌿        .            .      🌾
                {Fore.GREEN}        ~^~    .         .        ~^~
        {Fore.GREEN}       ~^~    ~^~      .       ~^~      ~^~      . 
    {Fore.GREEN}   ~^~  ~^~   ~^~   ~^~    .    ~^~   ~^~   ~^~
{Fore.GREEN}  ~^~  ~^~  ~^~  ~^~  ~^~  ~^~   ~^~  ~^~  ~^~  ~^~  ~^~
{Fore.GREEN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{Fore.YELLOW}                /\        /\         /\        /\ 
{Fore.YELLOW}       /\      /  \  /\  /  \  /\   /  \  /\  /  \   /\ 
{Fore.YELLOW}    __/  \____/    \/  \/    \/  \_/    \/  \/    \_/  \__
{Fore.YELLOW}~~~                                                    ~~~

{Style.RESET_ALL}{Fore.WHITE}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   {Fore.CYAN}¡Bienvenido a Excel Rancher! 🌿✨{Fore.WHITE}                                  ║
║                                                                      ║
║   Un mundo de pixel-aventuras te espera: cultivos por cuidar,        ║
║   estaciones por descubrir y una granja lista para florecer          ║
║   contigo día a día. {Fore.GREEN}🌾💚{Fore.WHITE}                                            ║
║                                                                      ║
║   Respira profundo, toma tus herramientas…                           ║
║   ¡tu historia en Excel Rancher está por comenzar!                   ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                 {Fore.MAGENTA}⇦  Presiona ENTER para continuar  ⇨{Fore.WHITE}                  ║
╚══════════════════════════════════════════════════════════════════════╝
{Fore.GREEN}
""")
    input()
    while menu:
        menu_principal()
        op_menu = input(f"> ")
        if  not op_menu.isdigit():
            print("Inserte una opcion valida del menu.")
            continue
        else:
            pass
        op_menu = int(op_menu)
        match op_menu:
            case 1:
                modificar_perfil(registrados, usuario_act)
            case 2:
                pass
            case 3:
                mostrar_tienda()
                compra_animales()
            case 4:
                break
            case _:
                print("Ingrese una opcion valida del menu.")

