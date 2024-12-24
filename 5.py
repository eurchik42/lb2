import sqlite3
from flask import Flask, request, jsonify
app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT,content TEXT)''')
    conn.commit()
    conn.close()
def add_message_to_db(content):
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()
@app.route('/messages', methods=['POST'])
def save_message():
    if not request.is_json:
        return jsonify({"error": "Expected JSON data"}), 400
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({"error": "Missing 'content' in the request body"}), 400
    add_message_to_db(content)
    return jsonify({"message": "Message saved successfully"}), 200
if __name__ == '__main__':
    init_db()
    app.run(port=8000)
