from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from login import app, db  # Importamos la app y la base de datos desde login.py

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

@app.route("/citas", methods=["GET", "POST"])
@login_required  # Solo permite citas a usuarios autenticados
def citas():
    if request.method == "POST":
        nombre = request.form["nombre"]
        celular = request.form["celular"]
        correo = request.form["correo"]
        servicio = request.form["servicio"]
        adiciones = request.form.getlist("adiciones")
        fecha = request.form["fecha"]

        adiciones_str = ", ".join(adiciones)

        nueva_cita = Cita(
            nombre=nombre,
            celular=celular,
            correo=correo,
            servicio=servicio,
            adiciones=adiciones_str,
            fecha=fecha
        )

        db.session.add(nueva_cita)
        db.session.commit()

        return redirect(url_for("inicio"))

    return render_template("citas.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

if __name__ == "__main__":
    app.run(debug=True)
