import requests
from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas
import sklearn
import pickle

model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

app = Flask(__name__)

API_KEY = "22db195503fe4af99dbba1c59d5258ce"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    city_name = request.form.get("City", "")
    N = request.form.get("Nitrogen", "")
    P = request.form.get("Phosporus", "")
    K = request.form.get("Potassium", "")
    ph = request.form.get("Ph", "")
    rain_fall = request.form.get("Rainfall", "")
    temperature = request.form.get("Temperature", "")  # User input for temperature
    humidity = None

    try:
        params = {
            "q": city_name,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        weather_data = response.json()

        if response.status_code == 200:
            humidity = weather_data["main"]["humidity"]
        else:
            result = "City not found or weather data unavailable!"
            return render_template(
                "index.html",
                result=result,
                city=city_name,
                N=N,
                P=P,
                K=K,
                ph=ph,
                rain_fall=rain_fall,
                temperature=temperature,
            )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if humidity is None:
        result = "Weather data could not be retrieved. Please try again later."
        return render_template(
            "index.html",
            result=result,
            city=city_name,
            N=N,
            P=P,
            K=K,
            ph=ph,
            rain_fall=rain_fall,
            temperature=temperature,
        )

    feature_list = [N, P, K, temperature, humidity, ph, rain_fall]
    single_pred = np.array(feature_list).reshape(1, -1)
    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    crop_dict = {
        1: "Rice",
        2: "Maize",
        3: "Jute",
        4: "Cotton",
        5: "Coconut",
        6: "Papaya",
        7: "Orange",
        8: "Apple",
        9: "Muskmelon",
        10: "Watermelon",
        11: "Grapes",
        12: "Mango",
        13: "Banana",
        14: "Pomegranate",
        15: "Lentil",
        16: "Blackgram",
        17: "Mungbean",
        18: "Mothbeans",
        19: "Pigeonpeas",
        20: "Kidneybeans",
        21: "Chickpea",
        22: "Coffee",
    }

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = f"{crop} is the best crop to be cultivated right there."
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

    return render_template(
        "index.html",
        result=result,
        city=city_name,
        temperature=temperature,
        humidity=humidity,
        N=N,
        P=P,
        K=K,
        ph=ph,
        rain_fall=rain_fall,
    )


if __name__ == "__main__":
    app.run(debug=True)
