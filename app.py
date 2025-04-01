from flask import Flask, render_template
from flask_mysqldb import MySQL
from config import Config
from login import crear_base_de_datos  # Importar solo la función, no la app

app = Flask(__name__)
app.config.from_object(Config)  # Cargar configuración desde config.py

mysql = MySQL(app)  # Inicializar MySQL con Flask

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

if __name__ == "__main__":
    app.run(debug=True)
