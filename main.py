from flask import Flask, request, render_template
import distancia_form
import persona_form

rata = [1936, 1948, 1960, 1972, 1984, 1996, 2008]
tigre = [1937, 1949, 1961, 1973, 1985, 1997, 2009]
buey = [1938, 1950, 1962, 1974, 1986, 1998, 2010]
conejo = [1939, 1951, 1963, 1975, 1987, 1999, 2011]
dragon = [1940, 1952, 1964, 1976, 1988, 2000, 2012]
serpiente = [1941, 1953, 1965, 1977, 1989, 2001, 2013]
caballo = [1942, 1954, 1966, 1978, 1990, 2002, 2014]
cabra = [1943, 1955, 1967, 1979, 1991, 2003, 2015]
mono = [1944, 1956, 1968, 1980, 1992, 2004, 2016]
gallo = [1945, 1957, 1969, 1981, 1993, 2005, 2017]
perro = [1946, 1958, 1970, 1982, 1994, 2006, 2018]
cerdo = [1947, 1959, 1971, 1983, 1995, 2007, 2019]

zodiaco = {
            "none": "/",
            "rata": "./static/img/rata.jpg",
            "tigre": "./static/img/tigre.jpg",
            "buey": "./static/img/buey.jpg",
            "conejo": "./static/img/conejo.jpg",
            "dragon": "./static/img/dragon.jpg",
            "serpiente": "./static/img/serpiente.jpg",
            "caballo": "./static/img/caballo.jpg",
            "cabra": "./static/img/cabra.jpg",
            "mono": "./static/img/mono.jpg",
            "gallo": "./static/img/gallo.jpg",
            "perro": "./static/img/perro.jpg",
            "cerdo": "./static/img/cerdo.jpg"
           }

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

                
                
@app.route("/operaciones", methods=["GET", "POST"])
def calculo():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        op = request.form.get("rdOp")
        if op == "suma":
            total = num1 + num2
        elif op == "resta":
            total = num1 - num2
        if op == "multiplicacion":
            total = num1 * num2
        elif op == "division":
            total = num1 / num2
        return render_template("operaciones.html", total = total)
    else:
        return render_template("operaciones.html")
  
@app.route('/register')
def person():
    person_form = persona_form.PersonForm(request.form)
    return render_template("formPerson.html", form = person_form)

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = request.form.get("nombre")
    apaterno = request.form.get("apaterno")
    amaterno = request.form.get("amaterno")
    
    nombre_completo = nombre + " " + apaterno + " " + amaterno
    anio = int(request.form.get("anio"))
    img = zodiaco["none"]
    month = 2
    day = 8
    if int(request.form.get("mes")) <= month:
        if int(request.form.get("dia")) <= day:
            edad = 2024 - int(anio)
        else:
            edad = 2024 - int(anio) - 1
    else:
        edad = 2024 - int(anio)-1
            
    signo = "Ninguno"
    if anio in rata:
        img = zodiaco["rata"]
        signo = "rata"
    elif anio in tigre:
        img = zodiaco["tigre"]
        signo = "tigre"
    elif anio in buey:
        img = zodiaco["buey"]
        signo = "buey"
    elif anio in conejo:
        img = zodiaco["conejo"]
        signo = "conejo"
    elif anio in dragon:
        img = zodiaco["dragon"]
        signo = "dragon"
    elif anio in serpiente:
        img = zodiaco["serpiente"]
        signo = "serpiente"
    elif anio in caballo:
        img = zodiaco["caballo"]
        signo = "caballo"
    elif anio in cabra:
        img = zodiaco["cabra"]
        signo = "cabra"
    elif anio in mono:
        img = zodiaco["mono"]
        signo = "mono"
    elif anio in gallo:
        img = zodiaco["gallo"]
        signo = "gallo"
    elif anio in perro:
        img = zodiaco["perro"]
        signo = "perro"
    elif anio in cerdo:
        img = zodiaco["cerdo"]
        signo = "cerdo"
    
    return render_template("responsePerson.html", nombre = nombre_completo, edad = edad, img = img, signo = signo)
    


@app.route("/distancia", methods=['GET', 'POST'])
def alumnos():
    alumn_form = distancia_form.DistanceForm(request.form)
    if request.method == "POST":
        x1 = alumn_form.x1.data
        x2 = alumn_form.x2.data
        
        y1 = alumn_form.y1.data
        y2 = alumn_form.y2.data
        total = ((x1-x2)**2 + (y1 - y2)**2)**0.5
        print("x1:{}".format(x1))
        print("x2:{}".format(x2))
        print("y1:{}".format(y1))
        print("y2:{}".format(y2))
        print("Distancia:{}".format(total))
        return render_template("formDistancia.html", form = alumn_form, total = total)
    return render_template("formDistancia.html", form = alumn_form)

if __name__ == "__main__":
    app.run(debug=True)