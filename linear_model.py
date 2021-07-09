import numpy as np
from sklearn.preprocessing import MinMaxScaler
import json

def to2Darray(x):
    list=json.loads(x)
    return np.array(list).reshape(int(len(list)/2),2).tolist()
class Linear_Reg():
    def __init__(self):
        self.datapoint=[]
        self.line=[]
        self.theta=np.array([[0],[0]])
        self.X=[]
        self.y=[]
        self.scaler_X = MinMaxScaler()
        self.scaler_y = MinMaxScaler()
        self.X_=[]
        self.y_=[]
        self.alpha=0.1
    def set_init(self, datapoint):
        self.datapoint=datapoint
        self.X,self.y=[[x[0]] for x in datapoint],[[x[1]] for x in datapoint]
        self.X_=self.scaler_X.fit_transform(self.X)
        self.X_=np.array([[x[0],1]for x in self.X_])
        self.y_=self.scaler_y.fit_transform(self.y)
        self.line=[0,1000]
        self.theta=np.array([[0],[0]])
    def step(self):
        f_diff=2*np.dot(self.X_.transpose(),(np.dot (self.X_, self.theta)-self.y_))
        self.theta=self.theta-f_diff*self.alpha
    def predict(self,X):
        X_=self.scaler_X.transform(X)
        X_=np.array([[x[0],1]for x in X_])
        y_=np.dot(X_, self.theta)
        return self.scaler_y.inverse_transform(y_).astype('int')
    def point2draw_line(self):
        return [[x,self.predict([[x]]).max()] for x in self.line]
    def set_alpha(self,a):
        self.alpha=a
    def mse(self):
        return((np.dot(self.X_,self.theta)-self.y_)**2).mean()

linear_model=Linear_Reg()