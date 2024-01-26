from flask import Flask, request, render_template

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
  



@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        return  '''
                    <h1>La multiplicacion de: {} x {} = {}</h1>
                '''.format(num1, num2, (num1*num2))
    else:
        return  '''
                <form action="/multiplica" method="POST">
                    <label>N1: </label>
                    <input type="text" name="n1"/>
                    <label>N2: </label>
                    <input type="text" name="n2"/>
                    <input type="submit">
                </form>

                '''

if __name__ == "__main__":
    app.run(debug=True)