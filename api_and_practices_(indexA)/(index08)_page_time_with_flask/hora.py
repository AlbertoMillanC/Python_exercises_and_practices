from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    hora_actual = str(datetime.now().time())
    return render_template("index.html", hora=hora_actual)

if __name__ == "__main__":
    app.run()
