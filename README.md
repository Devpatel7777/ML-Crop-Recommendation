#  Crop Recommendation System using Machine Learning

> **An end-to-end Machine Learning application that recommends the most suitable crop based on soil nutrients and environmental conditions using a trained classification model and an interactive Streamlit web application.**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Table of Contents

* Project Overview
* Problem Statement
* Features
* Dataset
* Machine Learning Pipeline
* Model Development
* Tech Stack
* Project Structure
* Installation
* Usage
* Results
* Future Enhancements
* Author
* License

---

#  Project Overview

Agriculture plays a vital role in food production and economic growth. Choosing the appropriate crop based on soil nutrients and climatic conditions is essential for maximizing agricultural productivity.

This project leverages **Machine Learning** to recommend the most suitable crop by analyzing seven environmental and soil-related parameters. A trained classification model is integrated with a **Streamlit** web application, allowing users to receive real-time crop recommendations through a simple and intuitive interface.

---

#  Problem Statement

Farmers often struggle to determine which crop is most suitable for cultivation under specific soil and weather conditions.

This project aims to solve that problem by developing a predictive system that recommends the optimal crop using historical agricultural data and supervised machine learning techniques.

---

#  Features

*  Predicts the most suitable crop
*  Interactive Streamlit dashboard
*  Machine Learning-based prediction
*  Fast real-time inference
*  Clean and scalable prediction pipeline
*  Pre-trained model using Pickle
*  Feature scaling using MinMaxScaler
*  Supports 22 crop categories

---

#  Dataset

The model uses seven agricultural features:

| Feature        | Description                |
| -------------- | -------------------------- |
| Nitrogen (N)   | Nitrogen content in soil   |
| Phosphorus (P) | Phosphorus content in soil |
| Potassium (K)  | Potassium content in soil  |
| Temperature    | Average temperature (°C)   |
| Humidity       | Relative humidity (%)      |
| pH             | Soil pH value              |
| Rainfall       | Rainfall (mm)              |

---

#  Supported Crops

The application can recommend the following crops:

* Rice
* Maize
* Jute
* Cotton
* Coconut
* Papaya
* Orange
* Apple
* Muskmelon
* Watermelon
* Grapes
* Mango
* Banana
* Pomegranate
* Lentil
* Blackgram
* Mungbean
* Mothbeans
* Pigeonpeas
* Kidneybeans
* Chickpea
* Coffee

---

#  Machine Learning Pipeline

The project follows a complete Machine Learning workflow:

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Data Splitting
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Model Selection
10. Model Serialization
11. Streamlit Deployment

---

#  Model Development

The notebook evaluates multiple supervised learning algorithms before selecting the final model.

Models explored include:

* Logistic Regression
* Gaussian Naive Bayes
* K-Nearest Neighbors (KNN)

The selected model is saved as:

* `model.pkl`
* `scaler.pkl`

These files are loaded directly into the Streamlit application for real-time prediction.

---

#  Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Pickle

### Development Environment

* Jupyter Notebook
* VS Code

---

#  Project Structure

```text
Crop-Recommendation-System/
│
├── app.py
├── model.ipynb
├── model.pkl
├── scaler.pkl
├── Crop_recommendation.csv
├── requirements.txt
├── README.md
├── screenshots/
│   ├── home.png
│   ├── prediction.png
│   └── result.png
└── LICENSE
```

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/Crop-Recommendation-System.git
```

## Navigate to the Project

```bash
cd Crop-Recommendation-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

---

# 💻 Usage

1. Launch the Streamlit application.
2. Enter the required soil nutrient values.
3. Provide weather-related parameters.
4. Click **Predict**.
5. View the recommended crop instantly.

---

# 📊 Results

The trained Machine Learning model successfully predicts the most appropriate crop based on user-provided agricultural parameters.

The deployment through Streamlit enables quick and user-friendly predictions suitable for demonstration, educational purposes, and portfolio presentation.

---

# 📸 Screenshots

Add screenshots after deployment.

```
screenshots/
├── home.png
<img width="1907" height="916" alt="Screenshot 2026-08-02 202921" src="https://github.com/user-attachments/assets/903a9c1d-afd5-438f-8ad3-e5ee4d6d8494" />
├── input_form.png
├── prediction_result.png
```

---

# 🔮 Future Enhancements

* Fertilizer Recommendation System
* Weather API Integration
* Crop Yield Prediction
* Soil Health Monitoring
* Disease Detection
* Deep Learning Models
* Mobile Application
* Cloud Deployment (AWS, Azure, Render)


#  Author

## Dev Patel

**Aspiring Data Analyst | Machine Learning Engineer | Generative AI Enthusiast**



