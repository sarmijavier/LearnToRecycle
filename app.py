from flask import Flask
from flask import render_template, request
from werkzeug.utils import secure_filename
import os
import shutil
from prediction import Predict


app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['images'] = "./images"


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/cuenta')
def cuenta():
    shutil.rmtree('images')
    os.mkdir('images')
    return render_template('cuenta.html')


@app.route('/recicla')
def recicla():
    return render_template('recicla.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/upload", methods=["POST"])
def uploader():
    if request.method == "POST":
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['images'], filename))
        objeto = Predict()
        MainAnswer = objeto.typeOfFile(filename, f)
    return render_template('recicla.html', answers=MainAnswer)



if __name__ == "__main__":
    app.run()
