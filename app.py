from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///citas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Modelo de la tabla "citas"
class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    servicio = db.Column(db.String(100), nullable=False)
    adiciones = db.Column(db.String(200), nullable=True)
    fecha = db.Column(db.String(20), nullable=False)
    
# Crear la base de datos (solo la primera vez)
with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/citas", methods= ["GET", "POST"])
def citas():
    if request.method == "POST":
        # Obtener los datos del formulario
        nombre = request.form["nombre"]
        celular = request.form["celular"]
        correo = request.form["correo"]
        servicio = request.form["servicio"]
        adiciones = request.form.getlist("adiciones")  # Lista de adiciones seleccionadas
        fecha = request.form["fecha"]

        # Convertir la lista de adiciones a una cadena separada por comas
        adiciones_str = ", ".join(adiciones)

        # Crear una nueva cita
        nueva_cita = Cita(
            nombre=nombre,
            celular=celular,
            correo=correo,
            servicio=servicio,
            adiciones=adiciones_str,
            fecha=fecha
        )

         # Guardar la cita en la base de datos
        db.session.add(nueva_cita)
        db.session.commit()

        # Redirigir a una página de confirmación o a la lista de citas
        return redirect(url_for("inicio"))  # Cambia "inicio" por la página que desees

    # Si es una solicitud GET, simplemente renderiza la plantilla

    return render_template("citas.html")

@app.route("/productos") 
def productos():
    return render_template("productos.html")

if __name__ == "__main__":
    app.run(debug=True)