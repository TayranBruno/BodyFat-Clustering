import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('./bodyfat.csv')

X = data[['Density', 'BodyFat', 'Age', 'Weight', 'Height', 'Neck', 'Chest', 'Abdomen', 'Hip', 'Thigh', 'Knee', 'Ankle', 'Biceps', 'Forearm', 'Wrist']]
print(data.columns)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=2)
kmeans.fit(X_scaled)

data['Cluster'] = kmeans.labels_


plt.scatter(data['Weight'], data['Height'], c=data['Cluster'])
plt.xlabel('Peso')
plt.ylabel('Altura')
plt.show()


plt.scatter(data['Chest'], data['Abdomen'], c=data['Cluster'])
plt.xlabel('Torax')
plt.ylabel('Abdomen')
plt.show()
