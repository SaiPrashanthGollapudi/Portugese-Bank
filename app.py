import flask
from flask import request, render_template
import joblib

app = flask.Flask(__name__,static_url_path="")

@app.route('/', methods=['GET'])
def sendIndex():
        return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
        age=float(request.form['age'])
        job=float(request.form['job'])
        mar=float(request.form['mar'])
        bal=float(request.form['bal'])
        hous=float(request.form['hous'])
        loan=float(request.form['loan'])
        dur=float(request.form['dur'])
        cmpg=float(request.form['cmpg'])
        pd=float(request.form['pd'])
        X = [[age,job,mar,bal,hous,loan,dur,cmpg,pd]]
        model = joblib.load('portugese_deploy.pkl')
        species = model.predict(X)[0]
        return render_template('predict.html',predict=species)
app.run()