import pandas as pd
import joblib

# Load Model
model = joblib.load("student_model.pkl")

print("===== Student Performance Prediction System =====")

try:

    age = int(input("Enter Age: "))
    gender = int(input("Gender (Male=1, Female=0): "))

    attendance = float(
        input("Attendance Percentage: ")
    )

    study_hours = float(
        input("Study Hours Per Week: ")
    )

    assignment = float(
        input("Assignment Completion Rate: ")
    )

    previous_score = float(
        input("Previous Exam Score: ")
    )

    participation = float(
        input("Participation Score: ")
    )

    extracurricular = int(
        input("Extracurricular Activities (Yes=1, No=0): ")
    )

    internet = int(
        input("Internet Access At Home (Yes=1, No=0): ")
    )

    parent_education = int(
        input(
            "Parent Education (HighSchool=0, Graduate=1, Postgraduate=2): "
        )
    )

    # Create DataFrame

    student_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "AttendancePercentage": [attendance],
        "StudyHoursPerWeek": [study_hours],
        "AssignmentCompletionRate": [assignment],
        "PreviousExamScore": [previous_score],
        "ParticipationScore": [participation],
        "ExtracurricularActivities": [extracurricular],
        "InternetAccessAtHome": [internet],
        "ParentEducationLevel": [parent_education]
    })

    prediction = model.predict(
        student_data
    )[0]

    # Keep score in valid range

    prediction = max(
        0,
        min(
            100,
            prediction
        )
    )

    print("\nPredicted Final Exam Score:")
    print(round(prediction, 2))

except ValueError:

    print(
        "\nError: Please enter valid numeric values."
    )