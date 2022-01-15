from flask import Flask
from flask import render_template

app = Flask("mypaw")


@app.route("/")
def hello():
    return render_template('index.html', name="Laeticia")


@app.route("/test")
def test():
    return "Passt!"


@app.route("/")
def logo():
    return render_template('img src="static/img/paw.png"')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
