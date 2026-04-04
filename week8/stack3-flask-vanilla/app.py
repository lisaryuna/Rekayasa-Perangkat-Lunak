from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_FILE = 'database.db'

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT)')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute('SELECT id, title, description FROM tasks')
        tasks = [{'id': row[0], 'title': row[1], 'description': row[2]} for row in cursor.fetchall()]
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (data['title'], data.get('description', '')))
        conn.commit()
        return jsonify({'id': cursor.lastrowid, 'title': data['title'], 'description': data.get('description', '')}), 201

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)