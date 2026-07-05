from flask import Flask, render_template, request
from predict import predict_flood

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    values = [
        float(request.form["Temp"]),
        float(request.form["Humidity"]),
        float(request.form["Cloud Cover"]),
        float(request.form["ANNUAL"]),
        float(request.form["Jan-Feb"]),
        float(request.form["Mar-May"]),
        float(request.form["Jun-Sep"]),
        float(request.form["Oct-Dec"]),
        float(request.form["avgjune"]),
        float(request.form["sub"])
    ]

    prediction = predict_flood(values)

    if prediction == 1:
        result = "⚠️ Flood Likely"
    else:
        result = "✅ No Flood"

    return render_template("index.html", prediction=result)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
