import pandas as pd
import numpy as np

# Reproducible random data
np.random.seed(42)

num_students = 2500

student_ids = range(1, num_students + 1)

ages = np.random.randint(18, 25, num_students)

genders = np.random.choice(
    ['Male', 'Female'],
    num_students
)

attendance = np.random.randint(
    50,
    101,
    num_students
)

study_hours = np.random.randint(
    1,
    31,
    num_students
)

assignment_completion = np.random.randint(
    40,
    101,
    num_students
)

previous_exam_score = np.random.randint(
    35,
    101,
    num_students
)

participation_score = np.random.randint(
    1,
    11,
    num_students
)

extracurricular = np.random.choice(
    ['Yes', 'No'],
    num_students
)

internet_access = np.random.choice(
    ['Yes', 'No'],
    num_students
)

parent_education = np.random.choice(
    [
        'High School',
        'Graduate',
        'Postgraduate'
    ],
    num_students
)

# Realistic Final Score Calculation

final_exam_score = (
    attendance * 0.20
    + study_hours * 1.2
    + assignment_completion * 0.15
    + previous_exam_score * 0.45
    + participation_score * 1.5
)

# Add random noise

final_exam_score = (
    final_exam_score
    + np.random.normal(
        0,
        5,
        num_students
    )
)

# Limit score between 0 and 100

final_exam_score = np.clip(
    final_exam_score,
    0,
    100
)

df = pd.DataFrame({

    'StudentID': student_ids,

    'Age': ages,

    'Gender': genders,

    'AttendancePercentage': attendance,

    'StudyHoursPerWeek': study_hours,

    'AssignmentCompletionRate':
        assignment_completion,

    'PreviousExamScore':
        previous_exam_score,

    'ParticipationScore':
        participation_score,

    'ExtracurricularActivities':
        extracurricular,

    'InternetAccessAtHome':
        internet_access,

    'ParentEducationLevel':
        parent_education,

    'FinalExamScore':
        np.round(final_exam_score, 2)

})

df.to_csv(
    'student_performance_dataset.csv',
    index=False
)

print("\nDataset Created Successfully!")
print(df.head())
print("\nTotal Records:", len(df))