from flask import Flask
from flask import render_template, request
import time

app = Flask("mypaw")


@app.route("/")
def hello():
    return render_template('index.html', name="Laeticia")


@app.route("/mypets")
def mypets():
    return render_template('mypets.html')


@app.route("/")
def logo():
    return render_template('img src="static/img/paw.png"')


# @app.route("/savedpets")
# def example():
#   return render_template('img src="static/img/example.png"')


# mypets = [("cat", "henry", 7, "kibble", "none", "anxiety", "owner"),
#        ("dog", "lucy", 3, "wet food", "cbd", "none", "foster")
#         ]

# this was supposed to be a list example for the pets

# @app.route("/mypets", methods=["GET", "POST"])
# def home():
# print(request.form)
# mypets.append(
# (
# request.form.get("animal"),
# request.form.get("name"),
# float(request.form.get("age")),
# request.form.get("food"),
# request.form.get("medication"),
# request.form.get("special needs"),
# request.form.get("status"),
# ))
# return render_template("mypets.html")

# 1) this code was supposed to save the pets (like a database)

@app.route("/savedpets")
def show_savedpets():
    return render_template("savedpets.html")


# 2) and then be displayed on /savedpets but it didn't work :(


# t = int(input("How many hours should the timer be set for?"))

# while t:
#   hrs = t // 3600
#  mins = t // 60
#   secs = t % 60
#   timer = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
#   print(timer, end="\r")
#   time.sleep(1)
#   t -= 1
# print('Time for medicine!')

# countdown for the next dose of medicine

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
