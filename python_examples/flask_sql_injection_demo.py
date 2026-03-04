# Intentionally insecure example for CodeQL demonstration
# Simulates a Flask API handler

from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()

    # Vulnerable query: user input concatenated directly
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    return "Query executed"
