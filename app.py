from flask import Flask
from flask import render_template, request
from werkzeug.utils import secure_filename
import os
import shutil
from prediction import prueba


app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['imagenes'] = "./imagenes"


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/cuenta')
def cuenta():
    shutil.rmtree('imagenes')
    os.mkdir('imagenes')
    return render_template('cuenta.html')


@app.route('/recicla')
def recicla():
    return render_template('recicla.html')


@app.route("/upload", methods=["POST"])
def uploader():
    if request.method == "POST":
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['imagenes'], filename))
        objeto = prueba()
        respuesta = objeto.archivoCorrecto(filename,f)



    return render_template('recicla.html', answers = respuesta)





if __name__ == "__main__":
    app.run()
