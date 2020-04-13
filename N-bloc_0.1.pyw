#--------------------------------------------------Modulos-------------------------------------------------------
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as file
from io import open
import os


class N_bloc():
    def __init__(self):
        # La variable url se utilizara para almacenar la ruta del documento.
        self.url = ""
        # la variable title se usara para cambiar constantemente el nombre que se mostrara en la barra superior del archivo
        self.title = "N-bloc"
        self.tema = "white"
        self.root = Tk()
        self.root.title("N-bloc - Nuevo documento de texto")
        self.root.geometry("1000x610")
        self.root.resizable(0,0)
        self.menuBar = Menu(self.root)
        #-----------Barra de menu--------------
        self.root.config(menu=self.menuBar)
        self.archivoMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Archivo", menu=self.archivoMenu)
        self.archivoMenu.add_command(label="Nuevo", command=lambda:self.Nuevo())
        self.archivoMenu.add_command(label="Abrir", command=lambda:self.Abrir())
        self.archivoMenu.add_command(label="Guardar", command=lambda:self.Guardar())
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Salir", command=lambda:self.Salir())
        self.BuildMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label = "Build", menu=self.BuildMenu)
        self.BuildMenu.add_command(label = "Python", command=lambda:self.build_Py())
        self.BuildMenu.add_command(label = "Ruby", command=lambda:self.build_Ruby())
        self.preMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label= "Preferencias", menu=self.preMenu)
        self.preMenu.add_command(label="Temas", command=lambda:self.temas())
        self.fbox=Frame(self.root, width=1920, height=1080)
        self.fbox.place(x=0, y=0)
        #----------------TextBox------------------------
        self.box = Text(self.fbox, width=107, height = 30)
        self.box.grid(column = 1, row = 0)
        scroll = Scrollbar(self.fbox, command = self.box.yview)
        scroll.grid(column = 3, row = 0, sticky = "nsew")
        self.box.config(yscrollcommand = scroll.set)
        self.box.config(padx = 7, pady = 5, bd=0, font = ("Cambria", 13))
        self.root.mainloop()
    # El metodo Nuevo se encargara de crear un nuevo documento de texto cada vez que sea llamada
    def Nuevo(self):
        self.box.delete(1.0,"end")
        self.root.title(self.title + "- Nuevo documento de texto")
        # La funcion guardar sirve para guardar lo que esta escrito en el programa en un documento nuevo o sobre un documento ya
        #abierto

    def Guardar(self):
        #Creamos un condicional if para evaluar el documento sobre el que vamos a guardar
        #Si la variable url no tiene una ruta almacenada, quiere decir estamos trabajando sobre un documento nuevo
        #Asi que evaluamos si url no tiene nada, en caso de que sea asi, el bloque de codigo a continuacion se encargara
        #de tomar todo lo que este almacenado en el textbox del programa y guardarlo en la ruta y archivo que estan almacenados
        #en url.
        if self.url != "":
            texto = str(self.box.get(1.0, "end"))
            filed = open(self.url, 'w+')
            filed.write(texto)
            filed.close()
            self.root.title(self.title + " - " + self.url)
        #En caso de que url este vacia se ejecutara el siguiente bloque de codigo
        #Primero almacenamos una ruta junto con el nombre en que se quiere que se guarde el archivo
        #en la variable filed, luego creamos al condicional if validando si dentro de la variable filed esta vacia, en caso
        #de que si, en url lo que haremos es guardar el nombre del archivo, luego recorremos todos los datos dentro del textbox
        #depues instanciamos con filed, donde esta la ruta y nombre a open pasandole por parametro el nombre que esta en url
        #y creamos el nuevo documento de texto.
        else:
            filed = file.asksaveasfile(title="Guardar como", mode='w', defaultextension = ".txt")
            if filed is not None:
                self.url = filed.name
                texto = self.box.get(1.0, "end")
                filed = open(self.url, 'w+')
                filed.write(texto)
                filed.close()
                self.root.title(self.title + " - " + self.url)
    #La funcion Abrir sirve para abrir un documento ya guardado y que el texto en el se escriba en el textbox
    #Primero guardamos en url la ruta en donde se encuentra el documento de texto que se va a abrir
    #despues evaluamos si en la url verdaderamente hay alguna ruta, leemos todo el contenido dentro del documento abierto
    #y lo almacenamos en la variable "contenido", luego borramos todo lo que pueda estar en el textbox posteriormente
    #despues usamos el metodo insert del textbox para meter todo el texto que este posteriormente en la variable contenido
    #dentro del textbox del programa.
    def Abrir(self):
        self.url = file.askopenfilename(title="Abrir", initialdir=".", filetypes = (("Archivos de texto", "*.txt"), ("Archivos py", ".py")))
        if self.url != "":
            filed = open(self.url, 'r')
            contenido = filed.read()
            self.box.delete(1.0, "end")
            self.box.insert("insert", contenido)
            filed.close()
            self.root.title(self.title + " - " + self.url)
    #La funcion build lo que hace es abrir el archivo que se acaba de crear, se hace un el proceso de guardado normal
    #y luego se abre el archivo con la misma direccion donde se guardo.
    def build_Py(self):
        if self.url != "":
            texto = str(self.box.get(1.0, "end"))
            filed = open(self.url, 'w+')
            filed.write(texto)
            filed.close()
            root.title(self.title + " - " + self.url)
            os.startfile(self.url)
        else:
            filed = file.asksaveasfile(title="Guardar como", mode='w', defaultextension = ".py")
            if filed is not None:
                self.url = filed.name
                texto = self.box.get(1.0, "end")
                filed = open(self.url, 'w+')
                filed.write(texto)
                filed.close()
                self.root.title(self.title + " - " + self.url)
                os.startfile(self.url)
    def build_Ruby(self):
        if self.url != "":
            texto = str(self.box.get(1.0, "end"))
            filed = open(self.url, 'w+')
            filed.write(texto)
            filed.close()
            self.root.title(self.title + " - " + self.url)
            os.startfile(self.url)
        else:
            filed = file.asksaveasfile(title="Guardar como", mode='w', defaultextension = ".rb")
            if filed is not None:
                self.url = filed.name
                texto = self.box.get(1.0, "end")
                filed = open(self.url, 'w+')
                filed.write(texto)
                filed.close()
                self.root.title(self.title + " - " + self.url)
                os.startfile(self.url)
    #la funcion temas se encarga de evaluar el tema que esta puesto y en base al mismo cambiar al otro.
    def temas(self):
        if self.tema == "white":
            self.box.config(background="#21252b", fg="#c4ccdc", insertbackground="#c4ccdc")
            self.tema = "black"
        elif self.tema == "light":
            self.box.config(background="white", fg="black", insertbackground="black")
            self.tema = "white"
        elif self.tema == "black":
            self.box.config(background="#e4e2dd", fg="#634917", insertbackground="#634917")
            self.tema = "light"
    def Salir(self):
        self.root.destroy()




ventana = N_bloc()
