# Game
Actividad - Desarrollo de un juego.

--- **Nombre del juego**: ExcelRaincher

--- **Descripcion:** En el proyecto buscamos generar el primer mini juego para la compañia Crudzaso Games, nuestro primer juego se llama ExcelRaincher, con ExcelRaincher tendremos un juego de simulación agrícola, te conviertes en un granjero encargado de comprar y vender animales para hacer crecer tu granja. Al iniciar, recibes una gallina inicial que comienza a producir dinero mientras la mantienes en tu granja. A medida que pasa el tiempo, podrás reinvertir tus ganancias para adquirir nuevos animales, cada uno con diferentes niveles de producción. El objetivo final es expandir tu granja lo más posible y reunir la mayor cantidad de animales para maximizar tus ganancias. 

--- **Intrucciones de ejecucion:**

**¿Cómo jugar?**

   **> Descarga el juego**
   Primero, baja los archivos del juego desde este repositorio (Enlace/Clonar este repositorio).

   **> Abre la carpeta del juego**
   Entra donde guardaste los archivos.

   **> Haz clic para empezar**
   Busca el archivo del juego main.py y dale doble clic para abrirlo.

   ¡Y listo!

  El juego se abrirá y tendrás tu primera gallinita lista para darte monedas.

--- **Tenemos librerias???** 
librerias suadas:<
librerias de importacion
uuid
getpass
haslib
colorama
Diccionarios propios para guardar la informacion de data.py

--- **Descripción de la gestión de información implementada:**

El juego gestiona la información relacionada con los animales que posee el jugador. Los animales disponibles actualmente son gallinas, pavos, cerdos, ovejas y vacas, cada uno con su propio costo, proceso de compra/venta y cantidad de dinero que genera con el tiempo.

Toda esta información se organiza mediante diccionarios y librerias ademas de que se actualiza automáticamente cada vez que el jugador compra o vende un animal.

Tambien, el sistema mantiene un registro del dinero disponible del jugador y calcula de forma continua las ganancias producidas por todos los animales.
La información actualizada de la granja se muestra en pantalla, permitiendo al jugador tomar decisiones estratégicas sobre sus compras y su progreso dentro del juego.
