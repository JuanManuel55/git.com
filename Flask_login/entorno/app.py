from flask import Flask;
from flask import render_template;

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('archivo.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
   app.run(debug=True)