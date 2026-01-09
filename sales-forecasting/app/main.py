import streamlit as st

# -------------------------------------------
# App Configuration
# -------------------------------------------
st.set_page_config(
    page_title="AI Retail Forecasting Suite",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------
# Header / Branding
# -------------------------------------------
st.markdown(
    """
    <style>
        .main-title {
            font-size: 38px;
            font-weight: 800;
            color: #1B263B;
            padding-bottom: 0px;
        }
        .sub-title {
            font-size: 16px;
            color: #4F5D75;
            margin-top: -15px;
            padding-bottom: 20px;
        }
        .section-header {
            font-size: 24px;
            font-weight: 700;
            margin-top: 35px;
            color: #1B263B;
        }
        .footer {
            text-align: center;
            color: #7D8597;
            font-size: 13px;
            margin-top: 50px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-title'>AI Retail Forecasting Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>End-to-End Time Series Forecasting • Walmart Weekly Sales Dataset</div>", unsafe_allow_html=True)

# -------------------------------------------
# Introduction
# -------------------------------------------
st.markdown("""
Welcome to the **AI Retail Forecasting Suite**, a production-ready forecasting pipeline designed to 
transform raw transactional data into actionable retail sales predictions.

This tool demonstrates a complete machine learning workflow used in professional analytics teams:
data ingestion, time-series preparation, forecasting model execution, backtesting, and export-ready outputs.
""")

# -------------------------------------------
# Workflow Overview
# -------------------------------------------
st.markdown("<div class='section-header'>📌 Workflow Overview</div>", unsafe_allow_html=True)

st.markdown("""
### **1. Data Ingestion**
Upload the Walmart `train.csv` dataset to initiate automatic validation and preview.

### **2. Time-Series Preparation**
Select a Store and Department to generate a consolidated weekly time series structured for forecasting.

### **3. Forecast Engine**
Run forecasts (4–24 weeks) using:
- **Naive Baseline**
- **Seasonal Naive**
- **Prophet Model** (trend, seasonal, holiday-aware forecasting)

### **4. Performance Evaluation**
Evaluate forecast accuracy using:
- **MAE (Mean Absolute Error)**
- **MAPE (Mean Absolute Percentage Error)**  
with visual comparison of actual vs predicted trends.

### **5. Export & Reporting**
Export forecast tables as downloadable CSV files — ready for analysis, reporting, or client delivery.
""")

# -------------------------------------------
# Navigation Reminder
# -------------------------------------------
st.markdown("<div class='section-header'>🧭 Navigation</div>", unsafe_allow_html=True)

st.markdown("""
Use the **left sidebar** to navigate through each module:
- **Data Upload**
- **Forecasting Engine**
- **Model Evaluation**
- **Export Center**

The system is designed to guide you step-by-step through the full forecasting pipeline.
""")

# -------------------------------------------
# Footer
# -------------------------------------------
st.markdown(
    "<div class='footer'>AI Retail Forecasting Suite • Powered by Streamlit & Prophet</div>",
    unsafe_allow_html=True
)
