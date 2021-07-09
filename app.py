from flask import Flask, render_template, request
from werkzeug.utils import redirect
from linear_model import*
from KM import *
from KNN import*
app = Flask(__name__,template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')
###################################################
@app.route('/KMean')
def Kmean():
    return render_template('KM_index.html')

@app.route('/KM_step', methods=['GET', 'POST'])
def KM_step():
    data= to2Darray(request.form['datapoint'])
    for i in data:
        print(i)
    K=request.form['K']
    if(len(data)==0 or K==0):
        return redirect("/KMean")
    print(K)
    kmeans.set_init(int(K), data)
    ret=kmeans.points_with_centroids()
    print(ret)
    return render_template(
        'KM_step.html',hh="heading", 
        inn=ret[0], 
        centroid=ret[1]
        )

@app.route('/KM_draw', methods=['GET', 'POST'])
def KM_draw():
    if(request.form['clear']=="yes"):
        return redirect("/KMean")
    if(request.form['random']=="yes"):
        kmeans.random()
    else:
        kmeans.step()
    ret=kmeans.points_with_centroids()
    return render_template(
        'KM_step.html',hh="heading", 
        inn=ret[0], 
        centroid=ret[1]
        )
###################################################
@app.route('/Linear')
def Linear():
    return render_template('LN_index.html')

@app.route('/LN_step', methods=['GET', 'POST'])
def LN_step():
    data= to2Darray(request.form['datapoint'])
    if len(data)==0:
        return redirect("/Linear")
    alpha=float(request.form['alpha'])
    linear_model.set_init(data)
    linear_model.set_alpha(alpha)
    return render_template(
        'LN_step.html',hh="heading", 
        inn=linear_model.datapoint.tolist(), 
        line=linear_model.point2draw_line(),
        alpha=linear_model.alpha
        )

@app.route('/LN_draw', methods=['GET', 'POST'])
def LN_draw():
    if request.form['clear']=="yes":
        return redirect("/Linear")
    linear_model.set_alpha(float(request.form['alpha']))
    linear_model.step()
    return render_template(
        'LN_step.html',hh="heading", 
        inn=linear_model.datapoint.tolist(), 
        line=linear_model.point2draw_line(),
        mse=linear_model.mse(),
        alpha=linear_model.alpha
        )
####################################################
@app.route('/KNN')
def KNN():
    return render_template('KNN_index.html')

@app.route('/KNN_step', methods=['GET', 'POST'])
def KNN_step():
    if request.method=='POST':
        datapoint=to2Darray(request.form['datapoint'])
        labels=np.array(json.loads(request.form['labels'])).astype('int')
        if (len(datapoint)==0):
            return redirect("/")
        K=int(request.form['K'])
        print(datapoint,labels, K)
        knn_classifier.set_init(K=K, datapoint=datapoint, labels=labels)

    return render_template('KNN_drawnpredict.html',
    hh="heading", 
    inn=knn_classifier.datapoint.tolist(), 
    labels=knn_classifier.labels.tolist()
    )

@app.route('/KNN_draw', methods=['GET', 'POST'])
def KNN_draw():
    ret={
            'main_label':0,
            'point':[0,0],
            'color_lines':[0],
            'nearest_points':[0,0]
        }
    if request.form['clear']=="yes":
        return redirect("/")
    if request.method=='POST':
        point=json.loads(request.form['point'])
        if(len(point)==0):
            return render_template('KNN_drawnpredict.html',
                hh="heading", 
                inn=knn_classifier.datapoint.tolist(), 
                labels=knn_classifier.labels.tolist()
            )
        ret=knn_classifier.ret_visualize_value(point)
    return render_template('KNN_drawnpredict.html',
        hh="heading", 
        inn=knn_classifier.datapoint.tolist(), 
        labels=knn_classifier.labels.tolist(),
        predicted="yes",
        main_label=ret['main_label'],
        point=ret['point'],
        color_lines=ret['color_lines'],
        nearest_points=ret['nearest_points']
    )

if __name__ == '__main__':
    app.run(debug=True)


