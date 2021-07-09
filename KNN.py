import json
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def to2Darray(x):
    list=json.loads(x)
    return np.array(list).reshape(int(len(list)/2),2)

class KNN_Classifier():
    def __init__(self):
        self.datapoint=[]
        self.labels=[]
        self.neigh = KNeighborsClassifier()
        self.K=1
        self.input=[]
    def set_init(self, K, datapoint, labels):
        self.datapoint=datapoint
        self.labels=labels
        self.K=K
        self.neigh = KNeighborsClassifier(n_neighbors=K)
        self.neigh.fit(datapoint, labels)
    def ret_visualize_value(self,point):
        self.input=point
        color_lines=self.neigh.kneighbors([point])[1][0].tolist()
        nearest_points=[]
        for i in color_lines:
            nearest_points.append(self.datapoint[i].tolist())
        color_lines=[self.labels[x] for x in color_lines]
        return {
            'main_label':self.neigh.predict([point]).max(),
            'point':point,
            'color_lines': color_lines,
            'nearest_points':nearest_points
        }

knn_classifier=KNN_Classifier()