from app.database import get_db

class Movie:
    
    #Esto permite generar un objeto de tipo movie y pasarle parametros asociandolos a la variable correspondiente al objeto ej self.id_movie
    def __init__(self, id_movie=None, title=None, director=None, release_date=None, banner=None):
        self.id_movie = id_movie
        self.title = title
        self.director = director
        self.release_date = release_date
        self.banner = banner

    #Este metodo save(self), pertenece a las instancias (self) de arriba 
    def save(self): #para este metodo se necesita crear un metodo movie
        db = get_db() #este get_db se relaciona con database generando la coneccion.
        cursor = db.cursor()
        #Si existe ejecuta la query normal
        if self.id_movie:
            #%s es para indicar que es una cadena, %d es para decimales, %f para valores flow.
            cursor.execute("""
                UPDATE movies SET title = %s, director = %s, release_date = %s, banner = %s
                WHERE id_movie = %s
            """, (self.title, self.director, self.release_date, self.banner, self.id_movie))
        #Cambiar las palabras movies director, etc por las que necesitemos dell formulario.
        #Si no existe genera la insercion de la misma.
        else: 
            #insert permite ingresar todos los parametros ingresados en la base de datos.
            cursor.execute("""
                INSERT INTO movies (title, director, release_date, banner) VALUES (%s, %s, %s, %s)
            """, (self.title, self.director, self.release_date, self.banner))
            self.id_movie = cursor.lastrowid
            #lastrowid es una prop que permite generar una columna auto incrementable.  
        db.commit() #siempre que hagamos un save, delete o insert hay que poner un commit ya que es el encargado de reflejar ese nuevo cambio en nuestra base de datos.
        cursor.close() #Con esto cerramos la base de datos.

    #@ es un decorador 
    @staticmethod #staticmethod es una funcion que va a ser compartida, es decir, que no le pertenece a una instancia.
    def get_all(): #con solo poner el nombre de la clase movie get_all trae todas las clases a diferencia del save que tengo que crearlo para poder hacerlo, por esto es una clase compartida.
        db = get_db() #apertura base de datos
        cursor = db.cursor() #genero cursor
        cursor.execute("SELECT * FROM movies") #usamos el execute para pasarle la query que queremos que ejecute.
        rows = cursor.fetchall() #rows retorna en conjunto al fetchall un diccionario de todas las peliculas.
        movies = [Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4]) for row in rows] #indicamos donde va a estar cada segmetno de nuestra lista, el for itera por cada elemento de la lista
        cursor.close() #cerramos y retornamos a movies
        return movies

    @staticmethod
    def get_by_id(movie_id): #trae la pelicula por el id.
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies WHERE id_movie = %s", (movie_id,)) #enviamos la query que queremos que use + el valor del id (movie_id) es el parametro de la clase.
        row = cursor.fetchone() #al solo obtener un dato hacemos fetchone (para que solo obtengamos un dato)
        cursor.close()
        #lo que genera este if es que si la row ya existe hace que no retorne nada.
        if row:
            return Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM movies WHERE id_movie = %s", (self.id_movie,)) #self.id_movie está ya que le pasamos el id que queremos para que lo borre.
        db.commit()
        cursor.close()

    def serialize(self): #metodo creado por nosotros, este metodo retorna un estilo de diccionario con el id, tittle, director, realese date y banner.
        return {
            'id_movie': self.id_movie,
            'title': self.title,
            'director': self.director,
            'release_date': self.release_date.strftime('%Y-%m-%d'), #strftime genera formateos para fechas, como queremos ver ese dato digamos.
            'banner': self.banner
        }


