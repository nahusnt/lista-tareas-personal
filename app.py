from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from modelos import Tarea, RepositorioTareas

app = Flask(__name__)


URI_ATLAS = "mongodb+srv://admin:admin1234@cluster0.h0mql0v.mongodb.net/?appName=Cluster0"

cliente = MongoClient(URI_ATLAS)
db = cliente['lista_tareas_db']
repo = RepositorioTareas(db)

@app.route('/')
def index():
    tareas = repo.cargar_todas()
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar():
    titulo = request.form.get('titulo')
    if titulo:
        nueva_tarea = Tarea(titulo=titulo)
        repo.guardar(nueva_tarea)
    return redirect(url_for('index'))

@app.route('/eliminar/<id_tarea>')
def eliminar(id_tarea):
    repo.eliminar(id_tarea)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)