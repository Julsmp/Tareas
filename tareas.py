"""

Qué falta?

- Imprimir imprima solo el nombre de la tarea. 
- Poder acceder a la tarea
- Dentro de la tarea ver toda la información, descripción, fecha, etc.. 
- Opciones dentro de la tarea: 
    - completar tarea 
    - modificar tarea (poder decidir qué parte modificas)
- Añadir fecha a la tarea
- añadir atributo de completado


"""

# Variables

Mylist=[]

# Clases

class Tareas():

    def __init__(self, titulo):
        self.titulo=titulo
        self.descripcion=""

    def __repr__(self):
        return str(self.__dict__)

    def mostrar(self):
        print("Titulo: ", self.titulo, "\nDescripcion: ", self.descripcion)

# Funciones

def añadir_tarea():
    titulo=input("Titulo de la tarea: ")
    descripcion=input("Descripcion: ")
    print()

    mitarea=Tareas(titulo)

    mitarea.descripcion=descripcion

    mitarea.mostrar()

    Mylist.append(mitarea)

def print_list():
    for tarea in Mylist:
    	print(tarea)

añadir_tarea()
añadir_tarea()
print_list()