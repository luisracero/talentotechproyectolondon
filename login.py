import MySQLdb  # Asegúrate de tener instalado mysqlclient o MySQL-connector
from config import Config

def crear_base_de_datos():
    try:
        # Conectar con MySQL sin especificar la base de datos
        conn = MySQLdb.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            passwd=Config.MYSQL_PASSWORD
        )
        cursor = conn.cursor()
        
        # Crear la base de datos si no existe
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DB}")
        conn.commit()
        
        # Cerrar conexión
        cursor.close()
        conn.close()
        print("✅ Base de datos creada correctamente (si no existía).")
    
    except MySQLdb.Error as e:
        print(f"❌ Error al crear la base de datos: {e}")
