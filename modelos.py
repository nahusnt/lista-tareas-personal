from bson import ObjectId

class Tarea:
    def __init__(self, titulo, completada=False, id_tarea=None):
        self.id = id_tarea
        self.titulo = titulo
        self.completada = completada

    def a_diccionario(self):
        """Convierte el objeto a un diccionario compatible con MongoDB"""
        return {
            "titulo": self.titulo,
            "completada": self.completada
        }

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, tarea):
        self.tareas.append(tarea)

    def obtener_todas(self):
        return self.tareas

class RepositorioTareas:
    def __init__(self, db):
        self.coleccion = db['tareas']

    def guardar(self, tarea):
        resultado = self.coleccion.insert_one(tarea.a_diccionario())
        tarea.id = str(resultado.inserted_id)
        return tarea

    def cargar_todas(self):
        lista = ListaTareas()
        documentos = self.coleccion.find()
        for doc in documentos:
            t = Tarea(
                titulo=doc['titulo'],
                completada=doc.get('completada', False),
                id_tarea=str(doc['_id'])
            )
            lista.agregar(t)
        return lista.obtener_todas()

    def eliminar(self, id_tarea):
        self.coleccion.delete_one({'_id': ObjectId(id_tarea)})