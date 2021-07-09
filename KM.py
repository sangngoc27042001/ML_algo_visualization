import json
import numpy as np
import random
def to2Darray(x):
    list=json.loads(x)
    return np.array(list).reshape(int(len(list)/2),2)

#the range for this Kmean is between 0-500
class my_Kmeans():
    def __init__(self, K, datapoint):
        self.K=K
        self.datapoint=datapoint
        self.random()
        self.idx_array=self.idx_array=[np.array([np.linalg.norm(point_e-centroid_e) for centroid_e in self.centroid]).argmin()for point_e in self.datapoint]
    def set_init(self, K, datapoint):
        self.K=K
        self.datapoint=datapoint
        self.random()
        self.idx_array=self.idx_array=[np.array([np.linalg.norm(point_e-centroid_e) for centroid_e in self.centroid]).argmin()for point_e in self.datapoint]
    def step(self):
        self.idx_array=[np.array([np.linalg.norm(point_e-centroid_e) for centroid_e in self.centroid]).argmin()for point_e in self.datapoint]
        dum_var=[[] for _ in range(self.K)]
        for (i,x) in enumerate(self.idx_array):
            dum_var[x].append(self.datapoint[i])
        self.centroid=np.array([np.mean(np.array(x),axis=0).astype('int') for x in dum_var])
    def random(self):
        self.idx_array=[]
        while (len(set(self.idx_array))<self.K):
            self.centroid=[]
            X,Y=np.array([x[0] for x in self.datapoint]),np.array([x[1] for x in self.datapoint])
            X_max, X_min, Y_max, Y_min=X.max(), X.min(),Y.max(),Y.min()
            self.centroid=np.array([[random.randint(X_min,X_max),random.randint(Y_min,Y_max)]for _ in range(self.K)])
            self.idx_array=[np.array([np.linalg.norm(point_e-centroid_e) for centroid_e in self.centroid]).argmin()for point_e in self.datapoint]
    def points_with_centroids(self):
        dum_var=[[] for _ in range(self.K)]
        for (i,x) in enumerate(self.idx_array):
            dum_var[x].append(self.datapoint[i].tolist())
        return dum_var,self.centroid.tolist()

kmeans=my_Kmeans(1,np.array([[1,2]]))