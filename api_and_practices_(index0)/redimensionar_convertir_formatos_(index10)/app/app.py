from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_value = request.form["user_value"]
        # Aquí puede hacer algo con el valor ingresado por el usuario
        return "El valor ingresado por el usuario es: {}".format(user_value)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
