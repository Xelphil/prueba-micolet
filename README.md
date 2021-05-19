# prueba-micolet
Para ejecutar el codigo:
1.	Instalar Vagrant, VirtualBox y descomprimir el archivo micotel.7z
1.	Abrir consola de comandos.
2.	Dentro de la consola, ir a la carpeta donde hayas descomprimido el repositorio.
3.	Ejecutar el comando vagrant up y vagrant ssh para arrancar y entrar a la máquina virtual.
4.	Una vez dentro de la máquina virtual, ir a la carpeta del proyecto: cd /vagrant/micotel/.
5.	Iniciar el entorno virtual: source venv/bin/activate.
6.	export FLASK_APP=micotel.py
7.	Crear la base de datos:
    -  flask db init
    -  flask db migrate -m "micotel table"
    -  flask db upgrade
8.	Arrancar flask: flask run --host=0.0.0.0
