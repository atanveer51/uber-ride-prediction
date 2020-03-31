import numpy as np
from flask import Flask,render_template,request,jsonify
import pickle
import math
app=Flask(__name__)
model=pickle.load(open('taxi.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['post'])
def predict():
    int_feature=[int(x) for x in request.form.values()]
    final_feature=[np.array(int_feature)]
    prediction=model.predict(final_feature)
    output=round(prediction[0],2)
    return render_template('index.html',prediction_text="number of weekly ride should be {}".format(math.floor(output)))
if __name__=='__main__':
    app.run(debug=True)