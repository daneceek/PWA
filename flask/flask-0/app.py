from flask import Flask, request

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

# MOCNINA A ODMOCNINA #
# @app.route("/mocnina/<int:a>/<int:b>/")
# @app.route("/mocnina/<float:a>/<float:b>/")
# @app.route("/mocnina/<int:a>/<float:b>/")
# @app.route("/mocnina/<float:a>/<int:b>/")
# def mocnina(a, b):
#     return f"{a} na {b} je {a**b}"

# @app.route("/odmocnina/<float:a>/")
# @app.route("/odmocnina/<int:a>/")
# def odmocnina(a):
#     return f"odmocnina z {a} je {a**(1/2)}"


@app.route("/mocnina/")
def mocnina():
    vysledek = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=h1, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Mocnina</h1>
        <form action='/vypocet_mocniny' method='GET'>
            a = <input required type='text' name='a'> <br>
            x = <input required type='text' name='x'> <br>
            <input type='submit' value='Spočítat'>
        </form>    
    </body>
    </html>
    
    
    """
    return vysledek

@app.route("/vypocet_mocniny", methods= ["GET"])
def vypocet_mocniny():
    try:
        a = request.args["a"]
        x = request.args["x"]
    except:
        return "Error, data z formuláře nebyla správně předána!"
    try:
        moc = float(a) ** float(x)
    except:
        return "Error, musíte zadat pouze čísla!"
    return f"{a} na {x} je {moc}"

if __name__ == "__main__":
    app.run(debug=True)