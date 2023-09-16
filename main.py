from flask import Flask,render_template,redirect,request,url_for
import pickle

# load the model
with open("./random_forest.pkl","rb") as file:
    model_rf = pickle.load(file)

app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    # sends the file car_price_prediction.html from templates directory

    return render_template("aqi_prediction.html")

@app.route('/predict',methods=["GET"])
def predict():
    try:
        print(request.args)
# get values from request
        pm2 = float(request.args.get("pm2.5"))
        pm10 = float(request.args.get("pm10"))
        no = float(request.args.get("no"))
        no2 = float(request.args.get("no2"))
        co = float(request.args.get("co"))
        so2 = float(request.args.get("so2"))
        o3 = float(request.args.get("o3"))

        prediction = model_rf.predict([[pm2, pm10, no, no2, co, so2, o3 ]])
        aqi_predictions = "{:.2f}".format(prediction[0])

        return render_template("result.html" ,predictions= aqi_predictions)
    except:
        return f"<h1>It seems you have not selected the required inputs...Please try again !!</h1>"


if __name__ == '__main__':
    app.run(host='localhost',port=4500,debug=True)
