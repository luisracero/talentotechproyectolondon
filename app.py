from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from config import Config
from login import crear_base_de_datos
from werkzeug.security import generate_password_hash, check_password_hash
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Maneja el registro de nuevos usuarios"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        
        # Validaciones básicas
        if not email or not password:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('login_user'))
        
        try:
            # Verificar si el email ya existe
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            if cursor.fetchone():
                flash('Este email ya está registrado', 'error')
                return redirect(url_for('login_user'))
            
            # Hashear y guardar la contraseña
            hashed_pw = generate_password_hash(password)
            cursor.execute(
                "INSERT INTO usuarios (email, password_hash) VALUES (%s, %s)",
                (email, hashed_pw)
            )
            mysql.connection.commit()
            
            flash('¡Registro exitoso! Ahora puedes iniciar sesión', 'success')
            return redirect(url_for('login_user'))
            
        except Exception as e:
            flash('Error en el registro. Intenta nuevamente.', 'error')
            print(f"Error: {str(e)}")
        finally:
            cursor.close()
    
    return redirect(url_for('login_user'))


@app.route('/logout')
def logout():
    # Limpiar la sesión
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)