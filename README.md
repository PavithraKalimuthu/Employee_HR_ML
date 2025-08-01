# Employee Insights Prediction App

This Streamlit web application helps HR professionals analyze and predict employee-related outcomes using Machine Learning models. It consists of two predictive modules:
### 🛠️ Tools & Libraries:
  - Python 
  - Pandas
  - NumPy
  - Scikit-learn
  - XGBoost
  - Streamlit
  - Imbalanced-learn (SMOTE)

### 🔍 1. Employee Attrition Prediction
- **Goal**: Predict whether an employee is likely to leave the company.
- **Model Used**: XGBoost Classifier
- **Key Features**: 
  - Job Involvement
  - Job Level
  - Education
  - Work Life Balance
  - Monthly Income
  - Years At Company
  - Years In Current Role

### 📈 2. Promotion Likelihood Prediction
- **Goal**: Predict how many years since the last promotion, i.e., estimate likelihood for the next promotion.
- **Model Used**: Linear Regression
- **Key Features**:
  - Job Level
  - Total Working Years
  - Years In Current Role
  - Performance Rating
  - Education

---

## 🧪 Preprocessing Summary

- **Label Encoding** for binary columns (e.g., Attrition)
- **One-hot Encoding** for categorical features like Department, EducationField, etc.
- **Outlier capping** based on IQR method
- **SMOTE** for class balancing (for Attrition prediction)
- **Feature scaling** only where necessary (e.g., for regression)
  
---

## 📦 Files Included

- `xgb_model.pkl` — Model for Attrition prediction
- `promotion_lr_model.pkl` — Model for Promotion prediction
- `xgb_model_columns.pkl`, `promotion_lr_columns.pkl` — Corresponding input feature orders
- `employee_streamlit.py` — Main Streamlit dashboard


---

## ▶️ How to Run


```bash
streamlit run employee_streamlit.py






```bash
streamlit run streamlit_app.py
