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
- Que la primera tarea del programa sea 'Aprender a utilizar el programa' y aprenda los comandos 
para evitar que aparezcan siempre las instrucciones y lo podrá recuperar en completados,
- Ver lista de completados

"""

# Variables

Mylist=[]
Lista_Completados=[]

# Clases

class Tareas():

    def __init__(self, titulo):
        self.titulo=titulo
        self.descripcion=""
        self.completa=False
        self.fecha=False

    def __completar(self, completamos):
        self.completa=completamos

    def __repr__(self):
        return str(self.__dict__)

    def mostrar(self):
        print("Titulo: ", self.titulo, "\nDescripcion: ", self.descripcion)

# Funciones de listas

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


def print_list():
    for tarea in Mylist:
    	print(tarea)

#Funciones de funcionamiento

def menu_inicial():
    while True: #Bucle inicial
        print("\n")
        print_list()
        print("\n") #Esto cambiarlo por una tarea más adelante
        print("Escribe '1' para añadir una tarea \n Escribe '2' para completar una tarea")
        resp_menu = input("- ")

        if resp_menu == "1":
            añadir_tarea()
        elif resp_menu == "2": #imprimir la lista numerada, pedirle que ponga el numero
            pass
        else:
            print("Esa respuesta no es correcta")


def menu_lista():
    pass

def menu_tarea():
    pass

#Comprobando xD
menu_inicial()
print_list()
