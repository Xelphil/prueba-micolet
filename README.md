# prueba-micolet
Para ejecutar el codigo:
1.	Instalar Vagrant, VirtualBox y descomprimir el archivo micotel.7z
1.	Abrir consola de comandos.
2.	Dentro de la consola, ir a la carpeta donde hayas descomprimido el repositorio.
3.	Ejecutar el comando vagrant up y vagrant ssh para arrancar y entrar a la máquina virtual.
4.	Una vez dentro de la máquina virtual, ir a la carpeta del proyecto: cd /vagrant/micotel/.
5.	Iniciar el entorno virtual: source venv/bin/activate.
6.	Crear la base de datos con la siguiente estructura:
  	id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mujer = Column(VARCHAR(2), nullable=True)
    hombre = Column(VARCHAR(2), nullable=True)
    infantil = Column(VARCHAR(2), nullable=True)
8.	descomentar la linea del config: 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') y poner el servidor creado
9.	Arrancar flask: flask run --host=0.0.0.0
