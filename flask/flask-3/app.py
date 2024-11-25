from flask import Flask, request, render_template, url_for, session
import os
app = Flask(__name__)
app.secret_key = "tajný klíč" #vzdycky  

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/o_nas")
def o_nas():
    return render_template("o_nas.html")

@app.route("/fotogalerie")
def fotogalerie():
    files = os.listdir("static/img") # otevře složku, dá do seznamu její obsah
    return render_template("fotogalerie.html", files=files)

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/login", methods = {"POST", "GET"})
def login():
    
    if "uzivatel" in session:
        del session["uzivatel"]
    else:
        session["uzivatel"] = "Kateřina"
    return render_template("login.html")

@app.route("/nahrat_soubor", methods={"POST", "GET"})
def nahrat_soubor():
    chyba = ""
    uspech = ""
    if request.method == "POST":
        try:
            f = request.files["soubor"]
            f.save("static/img/" + f.filename)
            uspech = "soubor byl úspěšně uložen"
        except:
            chyba = "chyba při pokusu o uložení souboru."  
    return render_template("nahrat_soubor.html", uspech=uspech, chyba=chyba)


if __name__ == "__main__":
    app.run(debug=True)

