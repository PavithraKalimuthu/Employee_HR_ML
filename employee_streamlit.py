import streamlit as st
import pandas as pd
import pickle

# Load Attrition model and columns
with open("xgb_model.pkl", "rb") as f:
    attrition_model = pickle.load(f)

with open("xgb_model_columns.pkl", "rb") as f:
    attrition_columns = pickle.load(f)

# Load Promotion model and columns
with open("promotion_lr_model.pkl", "rb") as f:
    promotion_model = pickle.load(f)

with open("promotion_lr_columns.pkl", "rb") as f:
    promotion_columns = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="HR Predictions", layout="wide")

st.title("HR Employee Insights App")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpaperaccess.com/full/2053097.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["🚪 Attrition Prediction", "📈 Promotion Likelihood"])

# ----------------------- TAB 1: Attrition -----------------------
with tab1:
    st.subheader("Attrition Prediction")

    col1, col2 = st.columns(2)

    with col1:
        Age = st.slider("Age", 18, 60, 30)
        DistanceFromHome = st.slider("Distance From Home", 1, 30, 10)
        Education = st.selectbox("Education (1=Below College, 2=College, 3=Bachelor, 4=Master, 5=Doctor)", [1, 2, 3, 4, 5])
        EnvironmentSatisfaction = st.selectbox("Environment Satisfaction (1-4)", [1, 2, 3, 4])
        Gender = st.selectbox("Gender", ['Male', 'Female'])
        JobInvolvement = st.selectbox("Job Involvement (1-4)", [1, 2, 3, 4])
        JobLevel = st.selectbox("Job Level (1-5)", [1, 2, 3, 4, 5])
        JobSatisfaction = st.selectbox("Job Satisfaction (1-4)", [1, 2, 3, 4])
        OverTime = st.selectbox("OverTime", ['Yes', 'No'])
        MonthlyIncome = st.number_input("Monthly Income", 1000, 50000, 15000, step=500)

    with col2:
        TotalWorkingYears = st.slider("Total Working Years", 0, 40, 10)
        YearsAtCompany = st.slider("Years at Company", 0, 40, 5)
        YearsInCurrentRole = st.slider("Years in Current Role", 0, 18, 3)
        YearsSinceLastPromotion = st.slider("Years Since Last Promotion", 0, 15, 1)
        YearsWithCurrManager = st.slider("Years with Current Manager", 0, 17, 2)
        BusinessTravel = st.selectbox("Business Travel", ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
        Department = st.selectbox("Department", ['Research & Development', 'Sales', 'Human Resources'])
        EducationField = st.selectbox("Education Field", ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'])
        JobRole = st.selectbox("Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director',
                                            'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
        MaritalStatus = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced'])

    if st.button("🔍 Predict Attrition"):
        input_data = {
            'Age': Age,
            'DistanceFromHome': DistanceFromHome,
            'Education': Education,
            'EnvironmentSatisfaction': EnvironmentSatisfaction,
            'Gender': 1 if Gender == 'Male' else 0,
            'JobInvolvement': JobInvolvement,
            'JobLevel': JobLevel,
            'JobSatisfaction': JobSatisfaction,
            'MonthlyIncome': MonthlyIncome,
            'OverTime': 1 if OverTime == 'Yes' else 0,
            'TotalWorkingYears': TotalWorkingYears,
            'YearsAtCompany': YearsAtCompany,
            'YearsInCurrentRole': YearsInCurrentRole,
            'YearsSinceLastPromotion': YearsSinceLastPromotion,
            'YearsWithCurrManager': YearsWithCurrManager,
            'BusinessTravel_Travel_Frequently': 1 if BusinessTravel == 'Travel_Frequently' else 0,
            'BusinessTravel_Travel_Rarely': 1 if BusinessTravel == 'Travel_Rarely' else 0,
            'Department_Research & Development': 1 if Department == 'Research & Development' else 0,
            'Department_Sales': 1 if Department == 'Sales' else 0,
            'EducationField_Life Sciences': 1 if EducationField == 'Life Sciences' else 0,
            'EducationField_Marketing': 1 if EducationField == 'Marketing' else 0,
            'EducationField_Medical': 1 if EducationField == 'Medical' else 0,
            'EducationField_Other': 1 if EducationField == 'Other' else 0,
            'EducationField_Technical Degree': 1 if EducationField == 'Technical Degree' else 0,
            'JobRole_Healthcare Representative': 1 if JobRole == 'Healthcare Representative' else 0,
            'JobRole_Human Resources': 1 if JobRole == 'Human Resources' else 0,
            'JobRole_Laboratory Technician': 1 if JobRole == 'Laboratory Technician' else 0,
            'JobRole_Manager': 1 if JobRole == 'Manager' else 0,
            'JobRole_Manufacturing Director': 1 if JobRole == 'Manufacturing Director' else 0,
            'JobRole_Research Director': 1 if JobRole == 'Research Director' else 0,
            'JobRole_Research Scientist': 1 if JobRole == 'Research Scientist' else 0,
            'JobRole_Sales Executive': 1 if JobRole == 'Sales Executive' else 0,
            'JobRole_Sales Representative': 1 if JobRole == 'Sales Representative' else 0,
            'MaritalStatus_Married': 1 if MaritalStatus == 'Married' else 0,
            'MaritalStatus_Single': 1 if MaritalStatus == 'Single' else 0
        }

        input_df = pd.DataFrame([input_data], columns=attrition_columns)
        prediction = attrition_model.predict(input_df)[0]
        st.success("Prediction: " + ("🔴 Likely to Leave" if prediction == 1 else "🟢 Likely to Stay"))

# ----------------------- TAB 2: Promotion -----------------------

with tab2:
    st.subheader("Promotion Likelihood (Years Since Last Promotion)")

    c1, c2 = st.columns(2)

    with c1:
        JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5], key="promo_joblevel")
        TotalWorkingYears = st.slider("Total Working Years", 0, 40, 10, key="promo_totalwork")
        YearsInCurrentRole = st.slider("Years in Current Role", 0, 18, 3, key="promo_yearscurrole")
        PerformanceRating = st.selectbox("Performance Rating (1–4)", [1, 2, 3, 4], key="promo_perf")
        Education = st.selectbox("Education Level (1–5)", [1, 2, 3, 4, 5], key="promo_education")
        JobInvolvement = st.selectbox("Job Involvement (1-4)", [1, 2, 3, 4], key="promo_jobinvolve")
        YearsAtCompany = st.slider("Years at Company", 0, 40, 5, key="promo_yearsatcompany")
        WorkLifeBalance = st.selectbox("Work-Life Balance (1-4)", [1, 2, 3, 4], key="promo_worklife")
        EnvironmentSatisfaction = st.selectbox("Environment Satisfaction (1-4)", [1, 2, 3, 4], key="promo_envsat")
        NumCompaniesWorked = st.slider("Number of Companies Worked", 0, 10, 2, key="promo_numcomp")

    if st.button("📊 Predict Promotion Delay"):
        promo_data = {
            'JobLevel': JobLevel,
            'TotalWorkingYears': TotalWorkingYears,
            'YearsInCurrentRole': YearsInCurrentRole,
            'PerformanceRating': PerformanceRating,
            'Education': Education,
            'JobInvolvement': JobInvolvement,
            'YearsAtCompany': YearsAtCompany,
            'WorkLifeBalance': WorkLifeBalance,
            'EnvironmentSatisfaction': EnvironmentSatisfaction,
            'NumCompaniesWorked': NumCompaniesWorked
        }

        promo_df = pd.DataFrame([promo_data], columns=promotion_columns)
        promo_pred = promotion_model.predict(promo_df)[0]
        st.success(f"Estimated Years Until Next Promotion: 📅 {round(promo_pred, 2)} years")
