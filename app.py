from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import Config
from werkzeug.security import generate_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import User
from login import crear_base_de_datos

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

mysql = MySQL(app)
crear_base_de_datos()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_user'  # Redirige aquí si intenta acceder a /historial sin estar logueado

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(mysql, user_id)

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

# ✅ RUTA PROTEGIDA
@app.route('/login')
@login_required
def historial():
    return render_template("login.html")  # login.html contiene el historial




@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('inicio'))

from flask import jsonify, request
from flask_login import login_user

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    usuario = User.get_by_email(mysql, email)
    if usuario and usuario.verificar_password(password):
        login_user(usuario)
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "error", "msg": "Correo o contraseña incorrectos"}), 401


from flask import jsonify

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({"status": "error", "msg": "Todos los campos son obligatorios"}), 400

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        return jsonify({"status": "error", "msg": "Este correo ya está registrado"}), 409

    hashed_pw = generate_password_hash(password)
    cursor.execute("INSERT INTO usuarios (email, password_hash) VALUES (%s, %s)", (email, hashed_pw))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"status": "ok", "msg": "Registro exitoso. ¡Ahora inicia sesión!"})


if __name__ == "__main__":
    app.run(debug=True)
