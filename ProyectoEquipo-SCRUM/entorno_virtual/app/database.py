import os
import mysql.connector
from flask import g, Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)
# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 3306)
}

# Función para obtener la conexión a la base de datos
def get_db():
    # Si 'db' no está en el contexto global de Flask 'g'
    if 'db' not in g:
        # Crear una nueva conexión a la base de datos y guardarla en 'g'
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    # Retornar la conexión a la base de datos
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Extraer la conexión a la base de datos de 'g' y eliminarla
    db = g.pop('db', None)
    # Si la conexión existe, cerrarla
    if db is not None:
        db.close()

# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    # Registrar 'close_db' para que se ejecute al final del contexto de la aplicación
    app.teardown_appcontext(close_db)

# # Función para obtener todos los pedidos desde la base de datos
# def obtener_pedidos():
#     try:
#         conexion = mysql.connector.connect(**DATABASE_CONFIG)
#         cursor = conexion.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM pedidos")
#         pedidos = cursor.fetchall()
#         cursor.close()
#         conexion.close()
#         return pedidos
#     except mysql.connector.Error as error:
#         print(f"Error al obtener pedidos de la base de datos: {error}")
#         return []

# # Ruta para la página principal
# @app.route('/')
# def index():
#     # Obtener todos los pedidos desde la base de datos
#     pedidos = obtener_pedidos()
#     return render_template('index.html', pedidos=pedidos)

# if __name__ == '__main__':
#     app.run(debug=True)