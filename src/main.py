from flask import Flask,render_template,request,redirect,url_for
import joblib 

app=Flask(__name__)
model=joblib.load('car_price_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect')
def detect_page():
    return render_template('detect.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/predict',methods=["POST"])

def predicted_page():
    if request.method=="POST":
        engine_power=int(request.form["ENGINE_POWER"])
        age_in_days	=int(request.form["AGE_IN_DAYS"])
        km=int(request.form["KM"])
        previous_owners=int(request.form["Previous_Owners"])

        model_type=request.form["Model_types"]
        model_lounge,model_pop,model_sport=0,0,0

        if model_type=="lounge":
            model_lounge=1
            
        elif model_type=="pop":
            model_pop=1
           
        else :
            model_sport=1


        input_data=[[engine_power,age_in_days,km,previous_owners,model_lounge,model_pop,model_sport]]
        predicted=model.predict(input_data)
        predicted_price=predicted[0]

    return render_template('result.html',price=predicted_price)


if __name__ == '__main__':
    app.run(debug=True)