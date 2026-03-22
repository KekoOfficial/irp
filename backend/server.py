from flask import Flask, request, jsonify
from database import init_db
from auth import login
from chat import send_message, get_global
from creator import create_user

app = Flask(__name__)

init_db()

@app.route("/login", methods=["POST"])
def do_login():
    password = request.json["password"]
    user = login(password)

    if user:
        return jsonify({"status": "ok", "user": user})
    return jsonify({"status": "error"})

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    send_message(data["sender"], data["receiver"], data["message"])
    return jsonify({"status": "sent"})

@app.route("/global", methods=["GET"])
def global_chat():
    return jsonify(get_global())

@app.route("/create", methods=["POST"])
def create():
    data = request.json
    create_user(data["name"], data["password"])
    return jsonify({"status": "created"})

app.run(host="0.0.0.0", port=5000)