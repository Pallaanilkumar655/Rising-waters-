# 🌊 Rising Waters – AI Powered Flood Prediction System

## 📌 Project Overview

Rising Waters is a Machine Learning-based Flood Prediction System developed as part of the APSCHE AI/ML & GenAI Internship. The application predicts the likelihood of flooding based on weather and rainfall parameters using a trained Random Forest Classifier. A user-friendly Flask web application allows users to enter weather details and receive an instant flood prediction.

---

## 🎯 Problem Statement

Floods are one of the most destructive natural disasters, causing loss of life and property every year. Traditional forecasting methods may not always provide timely warnings. This project uses Machine Learning to analyze historical weather data and predict flood risk, helping support early awareness and decision-making.

---

## 🎯 Objectives

- Predict flood occurrence using historical weather data.
- Build a Machine Learning model with high prediction accuracy.
- Develop a user-friendly web application using Flask.
- Demonstrate the practical application of AI in disaster management.

---

## ✨ Features

- 🌧 Predicts flood risk from weather data.
- 🤖 Machine Learning-based prediction.
- 🌐 Interactive web interface using Flask.
- ⚡ Instant prediction results.
- 📊 Uses historical rainfall and weather information.

---

## 🛠 Technology Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- OpenPyXL
- HTML
- CSS
- Visual Studio Code
- Git & GitHub

---

## 📂 Project Structure

```
Rising-Waters-Flood-Prediction/
│
├── data/
│   └── flood_dataset.xlsx
├── models/
│   └── flood_model.pkl
├── notebooks/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

Dataset Source:
https://www.kaggle.com/datasets/arbethi/rainfall-dataset

Features Used:
- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall
- Oct-Dec Rainfall
- Average June Rainfall
- Sub Rainfall

Target:
- Flood (Yes/No)

---

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/Pallaanilkumar655/Rising-Waters-Flood-Prediction.git
```

2. Open the project folder

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Train the model

```bash
python train_model.py
```

5. Run the application

```bash
python app.py
```

6. Open in browser

```
http://127.0.0.1:5000
```

---

## 📸 Output

- ✅ No Flood
- ⚠️ Flood Likely

---

## 🔮 Future Scope

- Live weather API integration
- Real-time flood alerts
- GPS-based location prediction
- Mobile application
- Cloud deployment
- Interactive dashboard with charts

---

## 👨‍💻 Team

**Team Leader:**
Anil Kumar Palla

APSCHE AI/ML & GenAI Internship

---

## 📜 License

This project is developed for educational purposes as part of the APSCHE AI/ML & GenAI Internship.

---

## 🙏 Acknowledgements

- APSCHE
- SmartBridge
- Kaggle
- Python Community
- Scikit-learn
- Flask
