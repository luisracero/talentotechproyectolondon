from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from config import Config
from login import crear_base_de_datos
import MySQLdb

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY  # Importante para las sesiones

mysql = MySQL(app)

# Crear la base de datos si no existe
crear_base_de_datos()

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/citas")
def citas():
    return render_template("citas.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            # Crear conexión a la base de datos
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            
            # Consulta para verificar credenciales
            cursor.execute(
                "SELECT * FROM usuarios WHERE email = %s AND password = %s", 
                (email, password)
            )
            
            user = cursor.fetchone()
            cursor.close()
            
            if user:
                # Inicio de sesión exitoso
                session['user_id'] = user['id']  # Almacenar ID en sesión
                session['email'] = user['email']  # Almacenar email en sesión
                flash('Inicio de sesión exitoso', 'success')
                return redirect(url_for('inicio'))
            else:
                flash('Correo electrónico o contraseña incorrectos', 'error')
                
        except MySQLdb.Error as e:
            flash(f'Error al conectar con la base de datos: {str(e)}', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Limpiar la sesión
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)