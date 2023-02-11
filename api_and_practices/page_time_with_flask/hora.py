from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "La hora actual es: " + str(datetime.now().time())

if __name__ == "__main__":
    app.run()
