# --------------------------------
#         APP DE TAREAS
#     Made by Julia Martínez
#        v. 1.0 09/2020
# --------------------------------

import re

# --------------------------------
# Variables
# --------------------------------

Mylist=[]
Lista_Completadas=[]

# --------------------------------
# Clases
# --------------------------------

class Tareas():

    def __init__(self, titulo):
        self.titulo=titulo
        self.descripcion=""
        self.completa=False
        self.fecha=None

    def __completar(self, completamos):
        self.completa=completamos

    def __repr__(self):
        return str(self.__dict__)

    def mostrar(self):
        print("Titulo: ", self.titulo, "\nDescripcion: ", self.descripcion)

# --------------------------------
# Funciones de tareas
# --------------------------------

def añadir_tarea():
    titulo=input("Titulo de la tarea: ")
    descripcion=input("Descripcion: ")
    print()

    mitarea=Tareas(titulo)

    mitarea.descripcion=descripcion

    mitarea.mostrar()

    Mylist.append(mitarea)

    #Preguntar si quiere añadir más información a la tarea
    respuesta_fecha = input("Quieres añadir fecha a la tarea? Responde 'si' o 'no'. ")
    if respuesta_fecha.capitalize == "Si":
        pass
    elif respuesta_fecha.capitalize == "No":
        añadir_tarea()

def completar_tarea():
    print_list()
    num=input("\n Escribe el número de la tarea que quieres completar. Escribe 999 para cancelar. \n")

    if num != "999":
        if re.search ("[0-9]", num):
            num=int(num)

            Tarea_eliminar = Tareas("titulo")
            Tarea_eliminar = Mylist[num]
            
            Lista_Completadas.append(Tarea_eliminar)
            Mylist.pop(num)
            print("Tarea completada")
        else:
            print("Debías escribir el número. Volvamos a intentarlo. \n")
            completar_tarea()
    else:
        print("Volviendo al menú inicial")
        menu_inicial()

def print_list():
    for tarea.titulo in enumerate(Mylist):
    	print(tarea.titulo)

def añadir_fecha():
    pass


def print_completadas():
    if Lista_Completadas: 
        print("¡Felicidades! Has completado las siguientes tareas: ")
        print(Lista_Completadas)
    else: 
        print("Todavía no has completado ninguna tarea. ¡Ánimo!")
        menu_inicial()

# --------------------------------
#Funciones de funcionamiento
# --------------------------------

def menu_inicial():
    while True: #Bucle inicial
        print("\n")
        if Mylist: 
            print("Estas son las tareas que te quedan por completar: ")
            print_list()
            print("\n") #Esto cambiarlo por una tarea más adelante
            print("- Escribe '1' para añadir una tarea \n- Escribe '2' para completar una tarea \n- Escribe '3' para ver las tareas completadas")
            resp_menu = input("")
        else: 
            print("\n") #Esto cambiarlo por una tarea más adelante
            print("- Escribe '1' para añadir una tarea \n- Escribe '2' para completar una tarea \n- Escribe '3' para ver las tareas completadas")
            resp_menu = input("")           

        if resp_menu == "1":
            añadir_tarea()
        elif resp_menu == "2": #imprimir la lista numerada, pedirle que ponga el numero
            completar_tarea()
        elif resp_menu == "3":
            print_completadas()
        else:
            print("Esa respuesta no es correcta")

def menu_lista():
    pass

def menu_tarea():
    pass

#Comprobando xD
menu_inicial()
