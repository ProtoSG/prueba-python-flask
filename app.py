import os 
from dotenv import load_dotenv
from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
load_dotenv()

TURSO_DATABASE_URL = os.environ.get('TURSO_DATABASE_URL')
TURSO_AUTH_TOKEN = os.environ.get('TURSO_AUTH_TOKEN')

db_url = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"
engine = create_engine(db_url, echo=True)

# Crear un sessionmaker
SessionLocal = sessionmaker(bind=engine)

@app.route('/', methods=['GET'])
def get_productos():
    try:
        session = SessionLocal()
        sql = text("""
            SELECT p.producto_id, p.nombre, p.precio, p.descripcion, p.imagen_url, c.categoria_id, c.nombre AS nombre_categoria
            FROM Producto p
            JOIN Categoria c ON p.categoria_id = c.categoria_id;
        """)
                    
        datos = session.execute(sql)
        productos = []
        for fila in datos:
            producto = {
                'id': fila[0],
                'nombre': fila[1],
                'precio': fila[2],
                'descripcion': fila[3],
                'imagen_url': fila[4],
                'categoria': {
                    'id' : fila[5],
                    'nombre' : fila[6]
                }
            }
            productos.append(producto)
        return jsonify(productos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

if __name__ == "__main__":
    app.run(debug=True)

