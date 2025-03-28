from flask import Flask, render_template
from login import app  # Importamos la app desde login.py

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
