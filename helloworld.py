from flask import Flask
from flask import render_template, request

app = Flask("mypaw")
mypets = [("cat", "henry", 7, "kibble", "none", "anxiety", "owner"),
          ("dog", "lucy", 3, "wet food", "cbd", "none", "foster")
          ]

# @app.route("/mypets", methods=["GET", "POST"])
#def home():
    #print(request.form)
    #mypets.append(
        #(
           # request.form.get("animal"),
            #request.form.get("name"),
            #float(request.form.get("age")),
            #request.form.get("food"),
            #request.form.get("medication"),
            #request.form.get("special needs"),
            #request.form.get("status"),
# ))
    #return render_template("mypets.html")


@app.route("/savedpets")
def show_savedpets():
    return render_template("savedpets.html")


@app.route("/")
def hello():
    return render_template('index.html', name="Laeticia")


@app.route("/mypets")
def mypets():
    return render_template('mypets.html')


@app.route("/")
def logo():
    return render_template('img src="static/img/paw.png"')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
