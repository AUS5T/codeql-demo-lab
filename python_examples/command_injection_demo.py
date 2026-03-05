# Intentionally insecure example for CodeQL demo purposes only.
# Demonstrates OS command injection via a Flask request parameter.

from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/run")
def run():
    cmd = request.args.get("cmd", "echo hello")

    # Vulnerable: user-controlled input executed by a shell
    subprocess.run(cmd, shell=True, check=False)

    return "ok"
