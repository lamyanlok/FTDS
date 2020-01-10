from flask import Flask, render_template, request
import pickle
import numpy as np

app=Flask(__name__)

cls_model = pickle.load(open("fifa19-prediction.pkl","rb"))
reg_model = pickle.load(open("fifa_val_model.pkl","rb"))

@app.route('/')
def home():
    return render_template("home.html")

def ValuePredictor(to_predict_list):
    result=[]
    to_predict = np.array(to_predict_list).reshape(1,-1)   
    cls_val = to_predict[0][4:].reshape(1,-1)
    result.append(cls_model.predict(cls_val))
    result.append(np.round(reg_model.predict(to_predict),2))
    return result

@app.route('/result',methods = ['POST'])
def result():
    prediction=''
    if request.method == 'POST':

        to_predict_list = request.form.to_dict()
        print(to_predict_list.values())
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        print("Before sending to model", to_predict_list)
        result = ValuePredictor(to_predict_list)
        print("result from model", result)
        prediction=result
        # if result[0]=='FW':
        #     prediction='Forward'
        # elif result[0]=='MF':
        #     prediction='Midfielder'
        # elif result[0]=='DF':
        #     prediction='Defender'
        # else:
        #     prediction='GoalKeeper'
        print(prediction)
        return render_template("result.html",prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
