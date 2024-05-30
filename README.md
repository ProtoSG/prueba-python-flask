# Flask Todo API

Este es un proyecto de ejemplo que implementa una API RESTful para gestionar una lista de tareas utilizando Flask.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tuusuario/flask_todo.git
    cd flask_todo
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Ejecuta la aplicación:
    ```sh
    python app.py
    ```

## Uso

### Endpoints

- `GET /todos`: Obtiene todas las tareas.
- `GET /todos/<id>`: Obtiene una tarea por su ID.
- `POST /todos`: Crea una nueva tarea.
- `PUT /todos/<id>`: Actualiza una tarea existente.
- `DELETE /todos/<id>`: Elimina una tarea.

### Ejemplos de Requests

- Crear una nueva tarea:
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Nueva tarea", "description": "Descripción de la tarea"}' http://localhost:5000/todos
    ```

- Obtener todas las tareas:
    ```sh
    curl http://localhost:5000/todos
    ```

- Actualizar una tarea:
    ```sh
    curl -X PUT -H "Content-Type: application/json" -d '{"done": true}' http://localhost:5000/todos/1
    ```

- Eliminar una tarea:
    ```sh
    curl -X DELETE http://localhost:5000/todos/1
    ```


