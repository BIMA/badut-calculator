from flask import render_template, request, Flask
from calculator import CoupleCalculator

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Displaying the index page accessible at '/' """
    return render_template("index.html")


@app.route("/badut-result", methods=["POST"])
def operation_result():
    """Route where we send calculator form input"""
    calculator = CoupleCalculator()
    name1 = request.form["name1"]
    name2 = request.form["name2"]
    hape1 = request.form["hape1"]
    hape2 = request.form["hape2"]
    if "+" in hape1 or "+" in hape2:
        return render_template("index.html", result="Salah satu nomor handphone kamu salah format")
    result = calculator.calculate(name1, name2, hape1, hape2)
    return render_template("index.html", name1=name1, name2=name2, result=result, calculation_success=True)


if __name__ == "__main__":
    app.debug = True
    app.run()
