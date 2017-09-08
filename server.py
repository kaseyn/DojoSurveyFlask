from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def process():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template("result.html",name=name,location=location,language=language,comment=comment)

@app.route("/back")
def back():
    return redirect("/")

app.run(debug=True)