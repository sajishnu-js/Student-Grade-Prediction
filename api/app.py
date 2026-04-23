import streamlit as st
import requests

st.title("Student Grade Prediction")
st.write("Enter student details below to predict the grade.")

#Input Fields
study_hours    = st.number_input("Weekly Self Study Hours", min_value=0.0, max_value=40.0, value=15.0)
attendance     = st.number_input("Attendance Percentage",   min_value=0.0, max_value=100.0, value=85.0)
participation  = st.number_input("Class Participation",     min_value=0.0, max_value=10.0, value=5.0)
total_score    = st.number_input("Total Score",             min_value=0.0, max_value=100.0, value=75.0)

#Session state to store history
if "history" not in st.session_state:
    st.session_state.history = []

#Predict Button
if st.button("Predict Grade"):
    payload = {
        "weekly_self_study_hours" : study_hours,
        "attendance_percentage"   : attendance,
        "class_participation"     : participation,
        "total_score"             : total_score
    }
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    
    if response.status_code == 200:
        result = response.json()
        grade  = result["predicted_grade"]
        st.success(f"Predicted Grade: **{grade}**")
        st.session_state.history.append(result)
    else:
        st.error("Something went wrong. Make sure FastAPI is running!")

#Show All Button
if st.button("Show All Predictions"):
    if st.session_state.history:
        st.dataframe(st.session_state.history)
    else:
        st.warning("No predictions yet!")

#Clear Button
if st.button("Clear"):
    st.session_state.history = []
    st.success("Cleared!")