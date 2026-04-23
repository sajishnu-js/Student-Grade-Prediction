# 🎓 Student Grade Prediction System

A machine learning web application that predicts student grades based on study habits and performance data. Built with CatBoost, FastAPI, and Streamlit.


## 📊 Dataset

- **Source:** Kaggle — Student Performance Dataset
- **Size:** 1,000,000 rows
- **Target:** Student Grade (A, B, C, D, F)

## 🤖 Models

Three models were trained and compared:

| Model | Type |
|---|---|
| CatBoost | Gradient Boosting |
| XGBoost | Gradient Boosting |
| PyTorch | Neural Network |

**CatBoost was selected as the final model** for deployment due to its superior performance.

## 🖥️ Application Features

The Streamlit frontend provides a simple and interactive interface with the following features:

- **Grade Prediction** — Enter student details and instantly predict the grade using the trained CatBoost model
- **Prediction History** — View all previously predicted grades in a structured table during the session
- **Clear History** — Reset and clear all predictions with a single click

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13.9 |
| Backend | FastAPI |
| Frontend | Streamlit |
| ML Framework | CatBoost, XGBoost, PyTorch |
| Data Processing | Pandas, NumPy, Scikit-learn |
| Visualization | Matplotlib, Seaborn |

---