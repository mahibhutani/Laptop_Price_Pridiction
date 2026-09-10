# 💻 Laptop Price Prediction

A Machine Learning project that predicts laptop prices based on their specifications.

## 📌 Project Overview

This project covers the complete ML workflow, from data cleaning and feature engineering to model training and deployment using Streamlit.

## 🔄 Workflow

Raw Laptop Data
→ Data Cleaning
→ Feature Engineering
→ Data Preprocessing
→ Model Training
→ Model Evaluation
→ Price Prediction

## 🧹 Data Cleaning

The dataset was cleaned using Pandas techniques including:

- Removing unnecessary columns
- Handling and transforming string data
- Removing duplicate/unwanted data
- Processing RAM and Price values
- Extracting information from ScreenResolution
- Categorizing CPU and Operating System
- Cleaning Weight
- Creating PPI-related features

## ⚙️ Feature Engineering & Preprocessing

- Train-Test Split
- OneHotEncoder
- ColumnTransformer
- Pipeline
- Numerical and categorical feature handling

## 🤖 Models Tested

- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- Gradient Boosting Regression
- XGBoost Regression

Gradient Boosting Regression achieved the best R² score in the current experiments.

## 🌐 Web Application

The trained model is integrated with a Streamlit web application where users can enter laptop specifications and get an estimated laptop price.

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py