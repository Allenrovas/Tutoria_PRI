from Album import Album
from tkinter import *
from tkinter import ttk

class GestorAlbumes:
    def __init__(self):
        self.albumes = []
        self.id_siguiente = 1
    
    def agregar_album(self, album):
        album.id = self.id_siguiente
        self.albumes.append(album)
        self.id_siguiente += 1

    def eliminar_album(self, album_id):
        for album in self.albumes:
            if album.id == album_id:
                self.albumes.remove(album)
                break

def agregarAlbum():
    ventana_agregar = Toplevel(ventana)
    ventana_agregar.title("Agregar Álbum")
    ventana_agregar.geometry("600x425")
    ventana_agregar.config(bg="SkyBlue1")

    labelTitulo = Label(ventana_agregar, text="Título: ", font=("Arial",16,"italic"), bg="Skyblue1")
    labelAnio = Label(ventana_agregar, text="Año: ", font=("Arial",16,"italic"), bg="Skyblue1")
    labelArtista = Label(ventana_agregar, text="Artista: ", font=("Arial",16,"italic"), bg="Skyblue1")

    inputTitulo = Entry(ventana_agregar, font=("Arial",16,"italic"))
    inputAnio = Entry(ventana_agregar, font=("Arial",16,"italic"))
    inputArtista = Entry(ventana_agregar, font=("Arial",16,"italic"))

    btn_Guardar = Button(ventana_agregar, text= "Agregar Álbum", command=lambda:guardarAlbum(inputTitulo.get(),inputArtista.get(),inputAnio.get()), font=("Arial",12,"italic"), width=15, height=1)

    labelTitulo.place(x=0,y=25,width=150)
    labelAnio.place(x=0,y=125,width=150)
    labelArtista.place(x=0,y=225,width=150)

    inputTitulo.place(x=175,y=25,width=300)
    inputAnio.place(x=175,y=125,width=300)
    inputArtista.place(x=175,y=225,width=300)

    btn_Guardar.place(x=175,y=275,width=150)

def guardarAlbum(titulo,artista,anio):
    album = Album(None,titulo, artista,anio)
    gestor.agregar_album(album)
    actualizar_tabla()


def actualizar_tabla():
    for i in tabla.get_children():
        tabla.delete(i)
    for album in gestor.albumes:
        tabla.insert("","end",values=(album.id,album.titulo,album.artista,album.anio))


def eliminarAlbum():
    seleccion = tabla.selection()
    if seleccion:
        item = seleccion[0]
        album_id = tabla.item(item,"values")[0]
        gestor.eliminar_album(int(album_id))
        actualizar_tabla()


ventana = Tk()
ventana.geometry("1200x825")
ventana.title("Gestor de Álbumes")
ventana.config(bg="SkyBlue1")

gestor = GestorAlbumes()

tabla = ttk.Treeview(ventana, columns=("ID","Titulo", "Artista", "Año"))
tabla.heading("#1", text="ID")
tabla.heading("#2", text="Título")
tabla.heading("#3", text="Artista")
tabla.heading("#4", text="Año")
tabla.tag_configure("myfont",font=("Arial",12))

#Botón para agregar álbum
btn_agregar = Button(ventana, text= "Agregar Álbum", command=agregarAlbum, font=("Arial",12,"italic"), width=15, height=1)

#Botón para eliminar álbum
btn_eliminar = Button(ventana, text= "Eliminar Álbum", command=eliminarAlbum, font=("Arial",12,"italic"), width=15, height=1)

Titulo = Label(ventana, text= "Gestor de Álbumes", font=("Arial",16,"italic"), bg="Skyblue1")
scrollbar = ttk.Scrollbar(ventana, orient="vertical")
scrollbar.config(command=tabla.yview)
scrollbar.pack(side="right",fill="y")
Titulo.place(x=300,y=25,width=600)
tabla.place(x=100, y=75)
btn_agregar.place(x=200, y=350, width=200, height=50)
btn_eliminar.place(x=600, y=350, width=200, height=50)

ventana.mainloop()