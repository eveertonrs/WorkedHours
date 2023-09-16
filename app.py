from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__, template_folder="C:/Projeto trabalhos/WorkedHours/templates")
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/admin')
def loginadmin():
    return render_template('LoginAdm.html')

@app.route('/login/driver')
def loginadriver():
    return render_template('LoginDrivers.html')

@app.route('/api/data')
def get_data():
    # Lógica para buscar dados do Flask (exemplo)
    data = {"message": "Dados do Flask!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
