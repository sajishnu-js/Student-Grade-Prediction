# 🎓 Student Grade Prediction System

A machine learning web application that predicts student grades based on study habits and performance data. Built with CatBoost, FastAPI, and Streamlit.

---


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

---

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