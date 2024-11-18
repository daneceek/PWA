from flask import Flask, request, render_template, url_for
import os
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/o_nas")
def o_nas():
    return render_template("o_nas.html")

@app.route("/fotogalerie")
def fotogalerie():
    files = os.listdir(url_for("static/img")) # otevře složku, dá do seznamu její obsah
    return render_template("fotogalerie.html", files=files)

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)

