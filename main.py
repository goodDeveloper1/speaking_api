import os
from data import client
import json

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route("/<part>")
def returndata(part):
    with open(f"speaking_{part}_formatted.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data, 200

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))