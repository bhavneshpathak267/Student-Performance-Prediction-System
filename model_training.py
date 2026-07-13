import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import joblib

# Load Dataset
df = pd.read_csv(
    "cleaned_student_performance_dataset.csv"
)

# Encode Categorical Columns
label_encoder = LabelEncoder()

df["Gender"] = label_encoder.fit_transform(
    df["Gender"]
)

df["ExtracurricularActivities"] = label_encoder.fit_transform(
    df["ExtracurricularActivities"]
)

df["InternetAccessAtHome"] = label_encoder.fit_transform(
    df["InternetAccessAtHome"]
)

df["ParentEducationLevel"] = label_encoder.fit_transform(
    df["ParentEducationLevel"]
)

# Features
X = df.drop(
    ["StudentID", "FinalExamScore"],
    axis=1
)

# Target
y = df["FinalExamScore"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = LinearRegression()

# Training
model.fit(
    X_train,
    y_train
)

# Prediction
predictions = model.predict(
    X_test
)

# Evaluation Metrics
mae = mean_absolute_error(
    y_test,
    predictions
)

mse = mean_squared_error(
    y_test,
    predictions
)

rmse = np.sqrt(
    mse
)

r2 = r2_score(
    y_test,
    predictions
)

# Results
print("\n========== MODEL TRAINING COMPLETE ==========")

print("\nMean Absolute Error (MAE):")
print(round(mae, 4))

print("\nMean Squared Error (MSE):")
print(round(mse, 4))

print("\nRoot Mean Squared Error (RMSE):")
print(round(rmse, 4))

print("\nR2 Score:")
print(round(r2, 4))

# Save Model
joblib.dump(
    model,
    "student_model.pkl"
)

print("\nModel Saved Successfully!")