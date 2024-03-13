from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1><center>Hello Word.com</center><h1>"

@app.route('/calculadora/<operation>/<int:num1>/<int:num2>/<int:num3>')
def calculadora(n1,n2,n3,operation):
    if operation == "+":
        return f" La suma de como resultado: {n1 + n2 + n3}"
    elif operation == "-":
        return f" La resta da como resultado: {n1 - n2 - n3}"
    elif operation == "*":
        return f" La multiplicacion da como resultado: {n1 * n2  *n3}"
    elif operation == "/":
        return f" La divicion de como resultado: {n1 / n2 / n3}"
    elif operation == "**":
        return f" La elevacion da como resultado: {n1 ** n2 **n3}"
    

if __name__ == '__main__':
    app.run(port=5500 , debug=True)