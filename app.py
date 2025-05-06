from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/proyectos', methods=['GET'])
def obtener_datos():
    archivo_excel = r"A:\Python\Proyectos\proyecto de dasboard\Libro1.xlsx"
    df = pd.read_excel(archivo_excel)
    return jsonify(df.to_dict(orient='records'))

@app.route('/', methods=['GET'])
def home():
    return "✅ API funcionando correctamente", 200

if __name__ == '__main__':
    app.run(debug=True)
