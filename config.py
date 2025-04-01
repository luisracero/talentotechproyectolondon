import os

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Alex0489'  # Cambia con tu contraseña
    MYSQL_DB = 'usuarios'  # Nombre de la base de datos
    MYSQL_CURSORCLASS = 'DictCursor'
    SECRET_KEY = os.urandom(24)  # Clave secreta aleatoria para sesiones
