from Album import Album

#listaAlbumes = [Objeto1, Objeto2, Objeto3]
#Objeto1 = Album = {}
listaAlbumes = []

#Funcion para agregar 
def agregar_album():
    titulo = input("Ingrese el título del álbum: ")
    artista = input("Ingrese el nombre del artista: ")
    anio = input("Ingrese el año de lanzamiento: ")
    album = Album(titulo,artista,anio)
    listaAlbumes.append(album)
    print("Album agregado con nombre: ",album.titulo)

def mostrar_albumes():
    if listaAlbumes:
        for i, album in enumerate(listaAlbumes):
            print(f"Álbum {i + 1} - Título: {album.titulo}, Artista: {album.artista}, Año: {album.anio}")
    else:
        print("No hay álbumes en la lista.")


def bubble_sort(listaAlbumes):
    noNumeros = len(listaAlbumes)
    for i in range (noNumeros):
        for j in range (0, noNumeros-i-1):
            if listaAlbumes[j].anio > listaAlbumes[j+1].anio:
                listaAlbumes[j].anio, listaAlbumes[j+1].anio = listaAlbumes[j+1].anio, listaAlbumes[j].anio

while True:
    print("Menú: ")
    print("1. Agregar Álbum")
    print("2. Mostrar Álbumes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_album()
    elif opcion == "2":
        bubble_sort(listaAlbumes)
        mostrar_albumes()
    elif opcion =="3":
        break
    else:
        print("Opción no valida. Intente de nuevo.")