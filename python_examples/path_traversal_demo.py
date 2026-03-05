# Intentionally insecure example for CodeQL demo purposes only.
# Demonstrates path traversal vulnerability.

from flask import Flask, request

app = Flask(__name__)

@app.get("/read")
def read_file():
    filename = request.args.get("file")

    # Vulnerable: user-controlled file path
    with open(filename, "r") as f:
        return f.read()
