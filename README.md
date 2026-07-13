# 🎓 Student Performance Prediction System

A Machine Learning project that predicts a student's **Final Exam Score** using academic records, attendance, study habits, classroom participation, and extracurricular activities.

This project was developed as part of the **Machine Learning Internship Program** at **Infobharat Interns (IBI)**.

---

## 📖 Project Overview

Educational institutions generate large amounts of academic data every semester. Analyzing this data helps identify the factors that influence student performance and enables educators to make informed decisions.

This project develops a Machine Learning-based prediction system that estimates a student's Final Exam Score using historical academic and behavioral data.

The project demonstrates the complete Machine Learning workflow, including:

- Synthetic Dataset Generation
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- Interactive Prediction System

---

## 🎯 Objective

The objective of this project is to build a Student Performance Prediction System capable of accurately predicting students' final examination scores based on multiple academic and personal factors.

The system demonstrates practical applications of Machine Learning in Educational Analytics and Predictive Modeling.

---

## ✨ Features

- Generate Synthetic Student Dataset
- Data Cleaning & Validation
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Encoding
- Machine Learning Model Training
- Performance Evaluation
- Interactive Prediction System
- Input Validation
- Error Handling

---

## 📂 Dataset Information

The project uses a synthetic dataset consisting of approximately **2500 student records**.

### Dataset Features

| Feature | Description |
|---------|-------------|
| StudentID | Unique Student Identifier |
| Age | Student Age |
| Gender | Male / Female |
| AttendancePercentage | Attendance Percentage |
| StudyHoursPerWeek | Weekly Study Hours |
| AssignmentCompletionRate | Assignment Completion Percentage |
| PreviousExamScore | Previous Exam Score |
| ParticipationScore | Classroom Participation Score |
| ExtracurricularActivities | Yes / No |
| InternetAccessAtHome | Yes / No |
| ParentEducationLevel | High School / Graduate / Postgraduate |
| FinalExamScore | Target Variable |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Attendance vs Final Exam Score
- Previous Exam Score vs Final Exam Score
- Parent Education Level Analysis
- Score Distribution
- Correlation Heatmap

The analysis helped identify the factors that significantly influence student performance.
---

# 🤖 Machine Learning Model

The prediction system is built using **Linear Regression**, a supervised machine learning algorithm suitable for predicting continuous numerical values.

The dataset was divided into **Training** and **Testing** sets before model training to evaluate the model's performance on unseen data.

---

# 📈 Model Performance

The trained Linear Regression model achieved the following performance:

| Metric | Value |
|---------|-------|
| Mean Absolute Error (MAE) | **3.746** |
| Mean Squared Error (MSE) | **23.0145** |
| Root Mean Squared Error (RMSE) | **4.7973** |
| R² Score | **0.8794** |

The model explains approximately **87.94%** of the variance in student performance, indicating strong predictive capability.

---

# 🔄 Project Workflow

```text
Student Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Prediction System
```

---

# 📁 Project Structure

```text
Student-Performance-Prediction-System
│
├── data/
│   ├── student_performance_dataset.csv
│   └── cleaned_student_performance_dataset.csv
│
├── images/
│   ├── attendance_vs_score.png
│   ├── correlation_heatmap.png
│   ├── parent_education_score.png
│   ├── previous_vs_final.png
│   └── score_distribution.png
│
├── model/
│   └── student_model.pkl
│
├── src/
│   ├── dataset_generator.py
│   ├── preprocessing.py
│   ├── eda.py
│   ├── model_training.py
│   └── prediction.py
│
├── Student_Performance_Prediction.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/bhavneshpathak267/Student-Performance-Prediction-System.git
```

Navigate to the project directory:

```bash
cd Student-Performance-Prediction-System
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Generate the dataset:

```bash
python src/dataset_generator.py
```

Preprocess the dataset:

```bash
python src/preprocessing.py
```

Perform Exploratory Data Analysis:

```bash
python src/eda.py
```

Train the Machine Learning model:

```bash
python src/model_training.py
```

Run the prediction system:

```bash
python src/prediction.py
```

---

# 💻 Sample Prediction

```text
Enter Attendance Percentage: 92

Enter Study Hours Per Week: 15

Enter Assignment Completion Rate: 90

Enter Previous Exam Score: 84

Enter Participation Score: 80

Enter Parent Education Level: Graduate

Predicted Final Exam Score: 87.6%
```

---

# 🚀 Future Improvements

- Compare Multiple Machine Learning Models
- Random Forest Regression
- Gradient Boosting Regression
- XGBoost Regression
- Hyperparameter Tuning
- Feature Importance Analysis
- Streamlit Web Application
- Interactive Dashboard
- Cloud Deployment

---

# 📚 Learning Outcomes

This project provided hands-on experience in:

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Machine Learning Model Development
- Model Evaluation
- Python Programming
- Predictive Analytics

---

# 👨‍💻 Author

**Bhavnesh Pathak**

B.Tech (Artificial Intelligence & Machine Learning)

Machine Learning Intern – Infobharat Interns (IBI)

---

## ⭐ If you found this project helpful, consider giving it a Star on GitHub.