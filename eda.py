import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("cleaned_student_performance_dataset.csv")

# Graph 1
plt.figure(figsize=(8,5))
sns.scatterplot(
    x=df["AttendancePercentage"],
    y=df["FinalExamScore"]
)
plt.title("Attendance vs Final Exam Score")
plt.savefig("attendance_vs_score.png")
plt.show()

# Graph 2
plt.figure(figsize=(8,5))
sns.scatterplot(
    x=df["StudyHoursPerWeek"],
    y=df["FinalExamScore"]
)
plt.title("Study Hours vs Final Exam Score")
plt.savefig("study_hours_vs_score.png")
plt.show()

# Graph 3
plt.figure(figsize=(8,5))
sns.scatterplot(
    x=df["PreviousExamScore"],
    y=df["FinalExamScore"]
)
plt.title("Previous Score vs Final Score")
plt.savefig("previous_vs_final.png")
plt.show()

# Heatmap
numeric_df = df.select_dtypes(include=['int64','float64'])

plt.figure(figsize=(10,6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

# Graph 4 - Parent Education Level vs Average Score

plt.figure(figsize=(8,5))

parent_score = df.groupby(
    "ParentEducationLevel"
)["FinalExamScore"].mean()

sns.barplot(
    x=parent_score.index,
    y=parent_score.values
)

plt.title("Average Score by Parent Education Level")
plt.ylabel("Average Final Exam Score")
plt.savefig("parent_education_score.png")
plt.show()

# Graph 5 - Score Distribution

plt.figure(figsize=(8,5))

sns.histplot(
    df["FinalExamScore"],
    bins=20,
    kde=True
)

plt.title("Final Exam Score Distribution")
plt.xlabel("Final Exam Score")
plt.ylabel("Count")

plt.savefig("score_distribution.png")
plt.show()

print("Graphs Created Successfully!")