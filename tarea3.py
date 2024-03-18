from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1><center>Hello Word.com</center><h1>"

@app.route('/calculadora/<operation>/<int:n1>/<int:n2>/<int:n3>/<int:n4>')
def calculadora(n1,n2,n3,n4,operation):
    if operation == "+":
        return f" La suma de como resultado: {n1 + n2 + n3 + n4}"
    elif operation == "-":
        return f" La resta da como resultado: {n1 - n2 - n3 - n4}"
    elif operation == "*":
        return f" La multiplicacion da como resultado: {n1 * n2 * n3 * n4}"
    elif operation == "/":
        return f" La divicion de como resultado: {n1 / n2 / n3 / n4}"
    elif operation == "**":
        return f" La elevacion da como resultado: {n1 ** n2 ** n3 ** n4}"
    

if __name__ == '__main__':
    app.run(port=5500 , debug=True)