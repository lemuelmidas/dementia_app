#prediction function
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model_Extra.pkl','rb'))

#@app.route('/')
#def home():
#	return render_template('index.html')


#@app.route('/result',methods=['POST'])



import numpy as np
def ValuePredictor(to_predict_list):
    to_predict=np.array(to_predict_list).reshape(1,12)
    loaded_model=pickle.load(open("model_Extra.pkl", "rb"))
    result=loaded_model.predict(to_predict)
    return result[0]

@app.route('/result', methods=['POST'])

def result():
    if request.method== 'POST':
        to_predict_list=request.form.to_dict()
        to_predict_list= list(to_predict_list.values())
        to_predict_list= list(map(int, to_predict_list))
        result=ValuePredictor(to_predict_list)
        if int(result)==2:
            prediction='Dementia Risk Is High'
        elif int(result)==1:
            prediction='Dementia risk is moderate'
        else:
            prediction='Dementia risk is moderate'

        return render_template("result.html", prediction)