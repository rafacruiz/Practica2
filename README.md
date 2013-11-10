#Práctica 2: Aislamiento de una aplicación web usando

##Descripción
Crear una mini-aplicación web (un hola mundo o un simple formulario) y aislarlo en una jaula chroot.

Para la realización de esta segunda práctica de infraestructura virtual, vamos utilizamos la práctica de la asignatura Diseño de Aplicaciones para Internet realizada en Python. Consiste en un pequeño formulario que gestionamos con Python.

##Pasos para la creación de la Practica

Creamos una jaula con una distribucion Debian de 32bits con el comando 'debootstrap'. Para ello el primer paso es crear el directorio que va a contener la jaula.

	"mkdir /home/jaulas/debian"

Una vez tenemos el directorio, ejecutamos el siguiente comando para crear la jaula.

	"sudo debootstrap --arch=i386 wheezy /home/jaulas/debian/ http://ftp.us.debian.org/debian"

Accedemos la distribución.

	"chroot /home/jaulas/debian"

Una vez que estamos dentro configuramos nuestra distribución.

	Instalamos un paquete de español "apt-get install language-pack-es"
	Y actualizamos "apt-get update"

Cuando termina el paso anterior, instalamos el paquete que necesitamos para ejecutar nuestro formulario. Usamos el framework de webpy para realizar el formulario.

	"sudo apt-get install python-webpy"

Copiamos en el directorio de la jaula los archivos de nuestro formulario para poder ser ejecutado.

	"sudo cp practica3.py formulario3.py /home/jaulas/debian/home"
	
![Python](https://dl.dropboxusercontent.com/s/lmxr78i8g7i3uw6/prac3.png)

Y en el ultimo paso ejecutamos el formulario.

	"python practica3.py"

![Formulario](https://dl.dropboxusercontent.com/s/hbr2un5r37lyj32/formu.png)
