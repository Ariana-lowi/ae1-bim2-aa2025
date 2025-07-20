import os

RUTA_ARCHIVO = "data/inscripciones.txt"

def guardar_inscripcion(inscripcion):
    with open(RUTA_ARCHIVO, 'a', encoding='utf-8') as archivo:
        archivo.write(inscripcion)

def leer_inscripciones():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
        return archivo.readlines()
