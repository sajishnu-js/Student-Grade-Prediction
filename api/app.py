import threading
import uvicorn
import requests
import numpy as np
import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel
from catboost import CatBoostClassifier

# ── Model ──────────────────────────────────────────────────
model = CatBoostClassifier()
model.load_model("catboost_model.cbm")
grade_mapping = {0: "A", 1: "B", 2: "C", 3: "D", 4: "F"}

# ── FastAPI ────────────────────────────────────────────────
api = FastAPI()

class StudentData(BaseModel):
    weekly_self_study_hours: float
    attendance_percentage: float
    class_participation: float
    total_score: float

@api.post("/predict")
def predict(data: StudentData):
    input_data = [[data.weekly_self_study_hours, data.attendance_percentage,
                   data.class_participation, data.total_score]]
    predicted_class = int(np.array(model.predict(input_data)).flatten()[0])
    return {"predicted_grade": grade_mapping[predicted_class]}

# Start FastAPI once in background
if "api_started" not in st.session_state:
    threading.Thread(target=lambda: uvicorn.run(api, host="0.0.0.0", port=8000), daemon=True).start()
    st.session_state.api_started = True

# ── Streamlit ──────────────────────────────────────────────
st.title("Student Grade Prediction")

study_hours   = st.number_input("Weekly Self Study Hours", min_value=0.0, max_value=40.0,  value=15.0)
attendance    = st.number_input("Attendance Percentage",   min_value=0.0, max_value=100.0, value=85.0)
participation = st.number_input("Class Participation",     min_value=0.0, max_value=10.0,  value=5.0)
total_score   = st.number_input("Total Score",             min_value=0.0, max_value=100.0, value=75.0)

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Predict Grade"):
    payload = {"weekly_self_study_hours": study_hours, "attendance_percentage": attendance,
               "class_participation": participation, "total_score": total_score}
    result = requests.post("http://localhost:8000/predict", json=payload).json()
    st.success(f"Predicted Grade: **{result['predicted_grade']}**")
    st.session_state.history.append({**payload, **result})

if st.button("Show All Predictions"):
    if st.session_state.history:
        st.dataframe(st.session_state.history)
    else:
        st.warning("No predictions yet!")

if st.button("Clear"):
    st.session_state.history = []
    st.success("Cleared!")