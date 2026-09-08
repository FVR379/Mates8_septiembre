from flask import Flask, render_template, request, redirect, url_for
from registro import Registro
app = Flask(__name__)


@app.route("/procesar_registro",methods=["POST"])
def procesar():
    usuario_registrado={
        "nombre" : request.form['nombre'],
        "apellido" : request.form['apellido'],
        "edad": request.form['edad']
    }
    Registro.save(usuario_registrado)

    
    return redirect("/lista")

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html')

@app.route('/lista')
def lista():
    registros = Registro.get_all()
    return render_template('lista.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)