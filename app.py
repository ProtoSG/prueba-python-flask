import os 
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()
app = Flask(__name__)

TURSO_DATABASE_URL = os.environ.get('TURSO_DATABASE_URL')
TURSO_AUTH_TOKEN = os.environ.get('TURSO_AUTH_TOKEN')


dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

engine = create_engine(dbUrl, echo=True)

@app.route('/', methods=['GET'])
def get_producto():
    session = Session(engine)
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

# @app.before_first_request
# def create_tables():
#     db.create_all()

# @app.route('/todos', methods=['GET'])
# def get_todos():
#     todos = Todo.query.all()
#     return jsonify([todo.to_dict() for todo in todos])
#
# @app.route('/todos/<int:todo_id>', methods=['GET'])
# def get_todo(todo_id):
#     todo = Todo.query.get_or_404(todo_id)
#     return jsonify(todo.to_dict())
#
# @app.route('/todos', methods=['POST'])
# def create_todo():
#     data = request.get_json()
#     new_todo = Todo(
#         title=data.get('title'),
#         description=data.get('description', '')
#     )
#     db.session.add(new_todo)
#     db.session.commit()
#     return jsonify(new_todo.to_dict()), 201
#
# @app.route('/todos/<int:todo_id>', methods=['PUT'])
# def update_todo(todo_id):
#     todo = Todo.query.get_or_404(todo_id)
#     data = request.get_json()
#     todo.title = data.get('title', todo.title)
#     todo.description = data.get('description', todo.description)
#     todo.done = data.get('done', todo.done)
#     db.session.commit()
#     return jsonify(todo.to_dict())
#
# @app.route('/todos/<int:todo_id>', methods=['DELETE'])
# def delete_todo(todo_id):
#     todo = Todo.query.get_or_404(todo_id)
#     db.session.delete(todo)
#     db.session.commit()
#     return '', 204

if __name__ == '__main__':
    app.run(debug=False)

