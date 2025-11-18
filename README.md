# Game / ExcelRaincher
Actividad - Desarrollo de un juego.

--- **Nombre del juego**: ExcelRaincher

--- **Descripcion:** En el proyecto buscamos generar el primer mini juego para la compañia Crudzaso Games, el nombre del primer juego se llama ExcelRaincher, con ExcelRaincher tendremos un juego de simulación agrícola, te conviertes en un granjero encargado de comprar y vender animales para hacer crecer tu granja. Al iniciar, recibes una gallina con la cual el usuario comienza a producir dinero mientras la mantienes en tu granja. A medida que pasa el tiempo, podrás reinvertir tus ganancias para adquirir nuevos animales, cada uno con diferentes niveles de producción. **El objetivo final es expandir tu granja lo más posible y reunir la mayor cantidad de animales para maximizar tus ganancias. **

--- **Intrucciones de ejecucion:**

**¿Cómo jugar?**
   **>Instala Visual Studio Code**
       - Abra un explorador web y vaya a code.visualstudio.com.
       - Descargue la versión del sistema operativo. Visual Studio Code es compatible con Windows, Linux y macOS.
       - Una vez descargado, ejecute el instalador.
       - Abre el VS code desde la terminal usando ctrl + alt + T y escribe la palabra "code"
      Installar visualstudio code version 1.105.1
   
   **>Verificar el lenguaje de programacion intalado python**
       - Ve al sitio web oficial de Python (python.org), busca la versión 3.12.3 y descargarlo
       - Una vez descargado, abre el archivo instalador.
       - para abrirlo despues de finalizar la instalacion debes hacerlo desde la terminal usando ctrl + alt + T y escribe la frese  "python --version" y deberia               mostrarte lo siguiente:   Python 3.12.3
   
   **> Descarga el juego**
   Primero, baja el archivo del juego desde este repositorio (Enlace/Clonar este repositorio).

   **> Abre la carpeta del juego**
   Entra donde guardaste los archivos.

   **> Haz clic para empezar**
   Busca el archivo del juego main.py y dale doble clic para abrirlo.

   ¡Y listo!

  El juego se abrirá y tendrás tu primera gallinita lista para darte monedas.

--- **librerias usadas:** 
         **>> uuid** - identificador unico universal, es usado para identificadores de sesion. 
         **>> getpass **- Solicita una contraseña al usuario de forma segura, ocultando los caracteres que el usuario va escribiendo para obtener la informacion sin brechas de seguridad. este fue usado durante la autenticacion del usuario al inicio de nuestro codigo
haslib - 
         **>> colorama** - Genera color al codigo segun la necesidad, en nuetrro caso agregamos color con el fin de una mejor visual. 
random - Genera operaciones de aleatoriedad, durante el codigo se uso al momento de brindar una ganancia de forma aleatoria en un rango especifico.
         **>> time** - Genera marcas de tiempo, sirve ara obtener fechas, en nuestro caso fue usada con el fin de contabilizar el tiempo del animal dentro de la granja.
threading - Fue usado con el fin de activar diferentes tareas en paralelo.
         **>> Os:** realiza la funcion de limpieza de la consola, es decir, cada que queremos cambiar de proceso dentro del juego, la informacion previa se limpia del sistema con el fin de una mejor visual.

--- **Descripción de la gestión de información implementada:**

El juego gestiona la información relacionada con los animales que posee el jugador. Los animales disponibles actualmente son gallinas, pavos, cerdos, ovejas y vacas, cada uno con su propio costo, proceso de compra/venta y cantidad de dinero que genera con el tiempo.

Toda esta información se organiza mediante diccionarios y librerias ademas de que se actualiza automáticamente cada vez que el jugador compra o vende un animal.

Tambien, el sistema mantiene un registro del dinero disponible del jugador y calcula de forma continua las ganancias producidas por todos los animales.
La información actualizada de la granja se muestra en pantalla, permitiendo al jugador tomar decisiones estratégicas sobre sus compras y su progreso dentro del juego.
