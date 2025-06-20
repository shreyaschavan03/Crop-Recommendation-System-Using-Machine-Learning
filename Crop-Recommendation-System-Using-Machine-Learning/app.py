# from flask import Flask,request,render_template
# import numpy as np
# import pandas
# import sklearn
# import pickle

# # importing model
# model = pickle.load(open('model.pkl','rb'))
# sc = pickle.load(open('standscaler.pkl','rb'))
# ms = pickle.load(open('minmaxscaler.pkl','rb'))

# # creating flask app
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route("/predict",methods=['POST'])
# def predict():
#     N = request.form['Nitrogen']
#     P = request.form['Phosporus']
#     K = request.form['Potassium']
#     temp = request.form['Temperature']
#     humidity = request.form['Humidity']
#     ph = request.form['Ph']
#     rainfall = request.form['Rainfall']

#     feature_list = [N, P, K, temp, humidity, ph, rainfall]
#     single_pred = np.array(feature_list).reshape(1, -1)

#     scaled_features = ms.transform(single_pred)
#     final_features = sc.transform(scaled_features)
#     prediction = model.predict(final_features)

#     crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
#                  8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
#                  14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
#                  19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

#     if prediction[0] in crop_dict:
#         crop = crop_dict[prediction[0]]
#         result = "{} is the best crop to be cultivated right there".format(crop)
#     else:
#         result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
#     return render_template('index.html',result = result)




# # python main
# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, request, render_template
import numpy as np
import pickle
import os

print("📂 Current Directory:", os.getcwd())
print("📂 Files in Directory:", os.listdir())

# Load model and scalers safely
try:
    model = pickle.load(open('model.pkl', 'rb'))
    sc = pickle.load(open('standscaler.pkl', 'rb'))
    ms = pickle.load(open('minmaxscaler.pkl', 'rb'))
except Exception as e:
    print("Error loading model or scalers:", e)
    model, sc, ms = None, None, None

# Create Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Extract input values
        N = request.form.get('Nitrogen')
        P = request.form.get('Phosporus')
        K = request.form.get('Potassium')
        temp = request.form.get('Temperature')
        humidity = request.form.get('Humidity')
        ph = request.form.get('Ph')
        rainfall = request.form.get('Rainfall')

        # Print inputs to debug
        print("Received Values from Form:", N, P, K, temp, humidity, ph, rainfall)

        # Convert to float
        feature_list = [float(N), float(P), float(K), float(temp), float(humidity), float(ph), float(rainfall)]
        print("Converted to Float:", feature_list)

        # Reshape the data for prediction
        single_pred = np.array(feature_list).reshape(1, -1)

        # Apply MinMaxScaler and StandardScaler
        scaled_features = ms.transform(single_pred)
        final_features = sc.transform(scaled_features)

        # Make prediction
        prediction = model.predict(final_features)
        print("Raw Prediction Output:", prediction)

        # Crop dictionary mapping model output to crop name
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 
            6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 
            11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 
            16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 
            20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        # Get the crop name
        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = f"{crop} is the best crop to be cultivated right there"
        else:
            result = "Sorry, we could not determine the best crop."

        return render_template('index.html', result=result)

    except Exception as e:
        print("Error:", e)
        return render_template('index.html', result="Error in processing request.")


if __name__ == '__main__':
    app.run(debug=True, port=5500)

print("✅ Model Loaded Successfully:", type(model))
