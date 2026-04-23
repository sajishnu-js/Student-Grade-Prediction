from fastapi import FastAPI
from pydantic import BaseModel
from catboost import CatBoostClassifier
import numpy as np

app = FastAPI(title="Student Grade Prediction API")

model = CatBoostClassifier()
model.load_model('catboost_model.cbm')

class StudentData(BaseModel):
    weekly_self_study_hours : float
    attendance_percentage   : float
    class_participation     : float
    total_score             : float

grade_mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'F'}

@app.get("/")
def home():
    return {"message": "Student Grade Prediction API is running!"}

@app.post("/predict")
def predict(data: StudentData):
    input_data = [[
        data.weekly_self_study_hours,
        data.attendance_percentage,
        data.class_participation,
        data.total_score
    ]]
    prediction = model.predict(input_data)
    predicted_class = int(np.array(prediction).flatten()[0])
    grade = grade_mapping[predicted_class]
    return {
        "study_hours"     : data.weekly_self_study_hours,
        "attendance"      : data.attendance_percentage,
        "participation"   : data.class_participation,
        "total_score"     : data.total_score,
        "predicted_grade" : grade
    }
