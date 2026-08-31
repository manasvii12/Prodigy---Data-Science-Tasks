# Task-02: Data Cleaning & Exploratory Data Analysis (Titanic Dataset)

## 📌 Overview
This task focuses on cleaning the Titanic dataset and performing Exploratory Data Analysis (EDA) to uncover survival patterns.  
The analysis was done using **Python (pandas, seaborn, matplotlib)** to preprocess data, handle missing values, and generate visual insights.

---

## 🛠️ Steps Performed
1. **Data Cleaning**
   - Filled missing values in `Age` and `Fare` with median values.
   - Filled missing values in `Embarked` with the mode.
   - Dropped the `Cabin` column due to excessive missing data.

2. **Exploratory Data Analysis (EDA)**
   - Survival count distribution.
   - Survival by gender.
   - Survival by passenger class.
   - Age distribution of passengers.
   - Survival by age groups.
   - Survival by embarkation port.
   - Correlation heatmap of numerical features.

---

## 📊 Visualizations
Saved plots (PNG files) are included in this folder:
- `task2_survival_count.png`
- `task2_survival_by_gender.png`
- `task2_survival_by_class.png`
- `task2_age_distribution.png`
- `task2_survival_by_age.png`
- `task2_survival_by_embarked.png`
- `task2_correlation_heatmap.png`

---

## 🔑 Key Insights
- Women had a significantly higher survival rate compared to men.
- 1st class passengers had better survival chances than 3rd class passengers.
- Children had higher survival rates compared to adults.
- Passengers embarking from port **C** showed slightly better survival chances.
- Strong correlation observed between `Pclass` and survival.

---

## 📂 Files
- `train.csv`, `test.csv`, `gender_submission.csv` → datasets
- `task2_data_cleaning_eda.py` → Python script for cleaning + EDA
- PNG files → saved charts for reporting

---

## 🚀 Tools Used
- **Python**  
- **pandas** for data manipulation  
- **seaborn** & **matplotlib** for visualization  

---

## 📝 Author
Manasvi — B.Tech CSE student, Data Science Intern at Prodigy InfoTech
