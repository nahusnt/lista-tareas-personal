from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Acá va la URI que copiás de MongoDB Atlas:
URI_ATLAS = "mongodb+srv://admin:admin1234@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority"

cliente = MongoClient(URI_ATLAS)
db = cliente['lista_tareas_db']