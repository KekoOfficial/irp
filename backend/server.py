from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "irp.db"))

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return "🔥 IRP ONLINE 🔥"

@app.route("/login", methods=["POST"])
def login():
    password = request.json.get("password")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT name FROM users WHERE password=?", (password,))
    user = c.fetchone()

    if user:
        return jsonify({"status": "ok", "user": user[0]})

    return jsonify({"status": "error"})

@app.route("/create", methods=["POST"])
def create():
    data = request.json

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("INSERT INTO users (name, password) VALUES (?, ?)",
              (data["name"], data["password"]))

    conn.commit()
    conn.close()

    return jsonify({"status": "created"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)