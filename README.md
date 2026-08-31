# Task-03: Decision Tree Classifier (Bank Marketing Dataset)

## 📌 Overview
This task focuses on building a **Decision Tree Classifier** to predict whether a customer will subscribe to a bank term deposit based on demographic, behavioral, and socio-economic data.  
The dataset used is the **Bank Marketing dataset** from the UCI Machine Learning Repository, enriched with social and economic indicators.

---

## 🛠️ Steps Performed
1. **Data Preparation**
   - Loaded dataset (`bank-additional.csv` for testing, `bank-additional-full.csv` for final analysis).
   - Dropped the `duration` column (leaks target information).
   - Handled categorical variables using one-hot encoding.

2. **Model Training**
   - Split data into training (80%) and testing (20%).
   - Trained a Decision Tree Classifier (`max_depth=5`).

3. **Evaluation**
   - Calculated accuracy score.
   - Generated classification report (precision, recall, F1-score).
   - Created confusion matrix to analyze predictions.

4. **Visualization**
   - Exported decision tree structure as PNG.
   - Saved evaluation results in text files for reporting.

---

## 📊 Outputs
Generated files include:
- `task3_small_results.txt` → results on sample dataset (4,119 rows).
- `task3_full_results.txt` → results on full dataset (41,188 rows).
- `task3_small_decision_tree.png` → decision tree visualization (sample dataset).
- `task3_full_decision_tree.png` → decision tree visualization (full dataset).

---

## 🔑 Key Insights
- The dataset is **imbalanced** (majority of clients did not subscribe).  
- Decision Tree achieved reasonable accuracy but struggled with recall for the minority class (`yes`).  
- Socio-economic indicators (e.g., `euribor3m`, `nr.employed`) and client attributes (`age`, `job`, `marital`) strongly influenced predictions.  
- Removing `duration` ensures the model is realistic, as duration is only known after a call.

---

## 📂 Files
- `bank-additional-full.csv` → complete dataset (41,188 rows).  
- `bank-additional.csv` → sample dataset (4,119 rows).  
- `bank-additional-names.txt` → dataset description and citation.  
- `task3_decision_tree.py` → Python script for training & evaluation.  
- Results (`.txt`) and visualizations (`.png`).  

---

## 🚀 Tools Used
- **Python**  
- **pandas** for data manipulation  
- **scikit-learn** for model building & evaluation  
- **matplotlib** for visualization  

---

## 📌 Citation
Please cite the dataset as:  
> [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. *A Data‑Driven Approach to Predict the Success of Bank Telemarketing*. Decision Support Systems, 2014. doi:10.1016/j.dss.2014.03.001

---

## 📝 Author
Manasvi — B.Tech CSE student, Data Science Intern at Prodigy InfoTech
