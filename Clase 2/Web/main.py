from Album import Album

from flask import Flask, jsonify, request
import json
from flask_cors import(CORS)
# {
#     "artista" : "Queen",
#     "anio": 1977,
#     "titulo": "News of the World"
# }

app = Flask(__name__)
CORS(app)

albumes = []

@app.route('/', methods=['GET'])
def rutaInicial():
    return("Ruta inicial")

@app.route('/getAlbums',methods=['GET'])
def getAlbums():
    diccionario = [vars(album) for album in albumes]
    return jsonify(diccionario)

@app.route('/postAlbum', methods=['POST'])
def postAlbum():
    data = request.get_json()
    album = Album(len(albumes)+1,data['titulo'],data['artista'],data['anio'])
    albumes.append(album)
    return 'Album agregado con éxito', 201

@app.route('/deleteAlbum/<int:id>',methods=['DELETE'])
def deleteAlbum(id):
    for album in albumes:
        if album.id == id:
            albumes.remove(album)
            return 'Álbum eliminado', 200
    return 'Álbum no encontrado', 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
