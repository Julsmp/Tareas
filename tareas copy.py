# --------------------------------
#         APP DE TAREAS
#     Made by Julia Martínez
#        v. 1.0 09/2020
# --------------------------------

import re
from time import *

# --------------------------------
# Variables
# --------------------------------

Lista_tareas=[]
Lista_completadas=[]

# --------------------------------
# Clases
# --------------------------------

class Tareas():

    def __init__(self, titulo):
        self.titulo=titulo
        self.descripcion=""
        self.completa=False
        self.fecha=None

    def __str__(self):
        return "ok"

    def completar(self, completada):
        self.completa=completada

    def añadir_fecha(self, fecha):
        self.fecha=fecha

    def __repr__(self):
        return str(self.__dict__)

    def mostrar(self):
        print("Titulo: ", self.titulo, "\nDescripcion: ", self.descripcion)

def añadir_tarea():
    titulo=input("Titulo de la tarea: ")
    descripcion=input("Descripcion: ")
    print()

    mitarea=Tareas(titulo)
    mitarea.descripcion=descripcion

    respuesta_fecha="1"

    if respuesta_fecha=="1":
        fecha=input("¿Qué fecha?")
        mitarea.añadir_fecha(fecha)
        Lista_tareas.append(mitarea)
    

    print(Lista_tareas)

añadir_tarea()
print(Lista_tareas)