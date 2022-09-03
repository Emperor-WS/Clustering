#Importing Libraries
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv("Mall_Customers.csv")
x = dataset.iloc[:, [3, 4]].values

#Using the dendrogram to find the optimal number of clusters
dendrogram = sch.dendrogram(sch.linkage(x, method="ward"))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
plt.show()

#Fitting Hierarchical clustering to the mall dataset
hc = AgglomerativeClustering(n_clusters=5, affinity="euclidean", linkage="ward")
y_hc = hc.fit_predict(x)

#Visualising the clusters
plt.scatter(x[y_hc == 0, 0], x[y_hc == 0, 1], s=20, c="red", label="Careful")
plt.scatter(x[y_hc == 1, 0], x[y_hc == 1, 1], s=20, c="blue", label="Standard")
plt.scatter(x[y_hc == 2, 0], x[y_hc == 2, 1], s=20, c="green", label="Target")
plt.scatter(x[y_hc == 3, 0], x[y_hc == 3, 1], s=20, c="cyan", label="Careless")
plt.scatter(x[y_hc == 4, 0], x[y_hc == 4, 1], s=20, c="magenta", label="Sensible")
plt.title("Cluster of clients")
plt.xlabel("Annual Income(k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
