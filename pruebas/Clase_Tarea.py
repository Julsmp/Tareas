import pickle

class Tarea:

    #parámetros
    def __init__(self, titulo, descripcion, completada, fecha):
        self.titulo=titulo
        self.descripcion=descripcion
        self.completada=False
        self.fecha=None
        print("Se ha creado una nueva tarea: \n", self.titulo)

    def __str__(self):
        return "{}{}{}".format(self.titulo, self.descripcion, self.completada, self.fecha)

    def __repr__(self):
        return str(self.__dict__)

class ListaTareas:

    tareas=[]

    def agregarTareas(self, t):
        self.tareas.append(t)

    def mostrarTareas(self):
        for t in self.tareas:
            print(t)

    def __repr__(self):
        return str(self.__dict__)

#prueba
miLista=ListaTareas()
t=Tarea("Titulo", " ggg", False, 10)
miLista.agregarTareas(t)

miLista=ListaTareas()
t=Tarea("Titulo", " ", False, None)
miLista.agregarTareas(t)

miLista=ListaTareas()
t=Tarea("Titulo", " ", False, None)
miLista.agregarTareas(t)

miLista.mostrarTareas()