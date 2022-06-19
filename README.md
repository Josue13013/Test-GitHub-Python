# Test-GitHub-Python
Prueba Automatizada de inicio de sesion en GitHub escrita en Python

Esta es una prueba de Automatizacion de Inicio de Sesion en GitHub escrito en el lenguaje de Programacion Python.
Para su Ejecucion, Necesitara tener instalado como minimo el navegador Google Chrome y contar con una conexion a internet.

Pasos de Instalacion de herramientas requeridas para la ejecucion del Archivo: "web.py"
1) Instalacion de python en su ultima version, en caso de presentar errores instale python en la version 3.10.4 (Para mas informacion de como instalar dependiendo su sistema operativo ademas de recursos para su instalacion, visite: https://www.python.org/) Link para la descarga (en Windows 10): https://www.python.org/downloads/

2) Una vez completada la instalacion de python, instale pip (Sistema de gestion de paquetes en python), para saber como instalar pip de acuerdo a su sistema operativo, visite: https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/ Alli encontrara toda informacion necesaria sobre como instalar pip de acuerdo a su eleccion y a su sistema operativo.

3) Una vez instalado pip, descargue el archivo "web.py" (Guardelo en una carpeta separada)
4) En la carpeta que contiene el archivo "web.py" abra una terminal (Consola de comandos)
5) Ejecute el comando "pip install -U selenium" 
6) Una vez Terminada la instalacion de selenium (Culminacion de ejecucion del anterior comando), Ejecute el siguiente comando Ahora: "pip install pandas"
7) Una vez terminada la instalacion de pandas (Culminacion de ejecucion del anterior comando), abra su navegador google Chrome
8) Dirijase a la parte superior derecha y localice la opcion de "Mas" (tambien puede ser 3 puntos colocados de manera vertical) haga click alli
9) En el menu que surge haga click en "Ayuda"
10) Surgira un nuevo menmu de sub-opciones, elija: Informacion de Google Chrome
11) Se le mostrara la version de su Google Chrome.
12) Dirijase al sitio web:"https://chromedriver.chromium.org/downloads"
13) Busque entre las opciones de la pagina una version que se adapte a su version y haga click en el enlace correspondiente.(considere los 3 primeros numeros de su version instalada para una busqueda rapida en la pagina)
14) Se le mostraran las opciones correspondientes para cada sistema operativo, elija el adecuado para su sistema operativo y haga click en el enlace correspondiente y guarde el archivo.
15) Una vez descargado el archivo, este sera un zip, utilizando una herramienta de descompresion, descomprima el archivo.zip
16) Dependiendo de la herramienta que use para descomprimir el archivo, se le puede generar una carpeta con el mismo nombre del archivo zip, ingrese a la carpeta(de no ser asi, ignore este paso)
17) El archivo en cuestion tiene por nombre:"chromedriver", copie la ruta (directorio) de donde se encuentra el archivo "chromedriver"
18) Donde haya descargado el archivo "web.py" abra el archivo "web.py"(no lo ejecute, utilice un editor de archivos, Ejemplo: Visual Studio Code)
19) En la linea: "driver_path = " (sin borrar los parentesis y las comillas simplres a continuacion) elimine la ruta incluida al momento de descargar, y pegue el directorio (ruta) de su chromedriver.
20) Abra una linea (Consola) de comandos (Donde se encuentre el archivo "web.py") y ejecute el comando: "python web.py"

Se ejecutara el archivo "web.py" esto es lo que sucedera:
1) Se abrira un navegador google chrome y se auto-ajustara al tamaño de su pantalla(El tamaño sera de su pantalla completa)
2) Abrira la pagina de inicio de sesion de github
3) se llenaran los campos de usuario y contraseña
4) se hara click en el boton de "Sign in"
5) Iniciara sesion de manera automatica
6) al pasar 20 segundos la ventana (Navegador google Chrome) que se abrio, se cerrara.

Powered By Josué Rodrigo Chura Rojas :-)
