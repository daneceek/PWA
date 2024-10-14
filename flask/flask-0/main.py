from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "ahoj, světe, jak se vede?"

@app.route("/seznam")
def seznam():
    vysledek = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=h1, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Nadpis webu</h1>
        <ul>
            <li>Hardware</li>
            <li>Software</li>
            <li>Spotřební zboži</li>
        </ul>
    </body>
    </html>
    
    
    """
    return vysledek

@app.route("/mocnina/<int:a>/<int:b>/")
def mocnina(a, b):
    return f"{a} na {b} je {a**b}"
if __name__ == "__main__":
    app.run(debug=True)