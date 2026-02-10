from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()   # ❌ Command Injection

app.run(host="0.0.0.0", port=5000)
