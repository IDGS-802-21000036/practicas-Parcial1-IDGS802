from flask import Flask, request, render_template
import distancia_form

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