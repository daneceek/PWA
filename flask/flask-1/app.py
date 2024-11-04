from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", title="Home", text="Ahoj", cislo=5, pole=[1,23,58,26])

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/clanky/")
def clanky():
    clanky = vrat_clanky()
    return render_template("clanky.html", clanky = clanky)

def vrat_clanky():
    return [
        {"nadpis": "Prvni clanek", "text":"toto je text prvního clanku", "autor": "Pavel Z."},
        {"nadpis": "Druhy clanek", "text":"toto je text druheho clanku", "autor": "Pavel Z."},
        {"nadpis": "Treti clanek", "text":"toto je text tretiho clanku", "autor": "Pavel Z."}
    ]


if __name__ == "__main__":
    app.run(debug=True)



# aktivovat prostredi (.venv\Scripts\activate)
# flask run --debug