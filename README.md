# Bangalore House Price Predictor 🏠

A machine learning-based web application that predicts residential real estate prices in Bengaluru, India, based on location, square footage, number of bathrooms, and BHK.

## 📌 Project Overview
Buying a home in a tier-1 city like Bengaluru can be daunting due to fluctuating prices. This project uses a **Ridge Regression** model to provide users with an estimated price based on historical data. 

The application is built with a **Flask** backend and a responsive **Bootstrap** frontend.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Machine Learning:** Pandas, NumPy, Scikit-learn
* **Web Framework:** Flask
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Deployment:** (e.g., Localhost / Render / Heroku)

## 📊 Dataset & Model
* **Data Source:** The model was trained on a cleaned version of the "Bengaluru House Price Data" from Kaggle.
* **Preprocessing:** Handled missing values, removed outliers using business logic (e.g., price per sqft), and applied One-Hot Encoding to categorical locations.
* **Model:** A Linear Regression variant (**Ridge**) was used to prevent overfitting, achieving an R² score of approximately **0.84**.

## 🚀 Installation & Setup
Follow these steps to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/amaanbkn/bangalore-house-price-predictor.git](https://github.com/amaanbkn/bangalore-house-price-predictor.git)
   cd bangalore-house-price-predictor
