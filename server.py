from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

data = pd.read_csv('bodyfat.csv')
X = data[['Weight', 'Height', 'Chest', 'Abdomen', 'Age']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

@app.route('/clusterizar', methods=['POST'])
def clusterizar():
    dados = request.get_json()
    ponto = np.array([[dados['Weight'], dados['Height'], dados['Chest'], dados['Abdomen'], dados['Age']]])
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X_scaled)
    resultado = int(kmeans.predict(ponto)[0])  # Converter para int
    response = jsonify({'cluster': resultado})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
