from flask import Flask, render_template
app = Flask(__name__)

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