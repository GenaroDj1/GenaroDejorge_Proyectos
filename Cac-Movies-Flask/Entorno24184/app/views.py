#Views es la capa logica de nuestro proyecto
from flask import jsonify, request
from app.models import Movie 

#Aca generamos los metodos que nos permite trabajar con nuestra base de datos.

def index():
    return jsonify({'message': 'Hello World API Cac-movies'})

def create_movie(): #Este metodo permite crear los datos de la pelicula
    data = request.json
    #Generamos una nueva instancia movie. Aca tambien deberemos modificar sus campos por las del formulario.
    new_movie = Movie(title=data['title'], director=data['director'], release_date=data['release_date'], banner=data['banner'])
    new_movie.save() #aca la guardamos en el .save de models.
    return jsonify({'message': 'Movie created successfully'}), 201

def get_all_movies():
    movies = Movie.get_all()
    return jsonify([movie.serialize() for movie in movies])

def get_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie: #si no encuentra la peli tira ese error y si no devuelve sus datos (serialize)
        return jsonify({'message': 'Movie not found'}), 404
    return jsonify(movie.serialize())

def update_movie(movie_id): #Actualizacion de datos
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    data = request.json
    movie.title = data['title']
    movie.director = data['director']
    movie.release_date = data['release_date']
    movie.banner = data['banner']
    movie.save()
    return jsonify({'message': 'Movie updated successfully'})

def delete_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    movie.delete()
    return jsonify({'message': 'Movie deleted successfully'})