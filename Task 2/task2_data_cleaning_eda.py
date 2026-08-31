# ============================
# Task-02: Data Cleaning + EDA
# ============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
gender_submission = pd.read_csv("gender_submission.csv")

# ----------------------------
# Step 1: Data Cleaning
# ----------------------------
train['Age'].fillna(train['Age'].median(), inplace=True)
test['Age'].fillna(test['Age'].median(), inplace=True)

train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)
test['Fare'].fillna(test['Fare'].median(), inplace=True)

train.drop(columns=['Cabin'], inplace=True)
test.drop(columns=['Cabin'], inplace=True)

# ----------------------------
# Step 2: EDA + Save Outputs
# ----------------------------

# Survival Count
sns.countplot(x='Survived', data=train)
plt.title("Survival Count")
plt.savefig("task2_survival_count.png")
plt.show()

# Survival by Gender
sns.countplot(x='Sex', hue='Survived', data=train)
plt.title("Survival by Gender")
plt.savefig("task2_survival_by_gender.png")
plt.show()

# Survival by Class
sns.countplot(x='Pclass', hue='Survived', data=train)
plt.title("Survival by Passenger Class")
plt.savefig("task2_survival_by_class.png")
plt.show()

# Age Distribution
sns.histplot(train['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.savefig("task2_age_distribution.png")
plt.show()

# Survival by Age
plt.figure(figsize=(10, 6))
survived = train[train['Survived'] == 1]['Age']
not_survived = train[train['Survived'] == 0]['Age']
sns.histplot(survived, bins=30, color='green', label='Survived', kde=True)
sns.histplot(not_survived, bins=30, color='red', label='Not Survived',
             kde=True)
plt.legend()
plt.title("Survival by Age")
plt.savefig("task2_survival_by_age.png")
plt.show()

# Survival by Embarked
sns.countplot(x='Embarked', hue='Survived', data=train)
plt.title("Survival by Embarked Port")
plt.savefig("task2_survival_by_embarked.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(train.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("task2_correlation_heatmap.png")
plt.show()
