📊 AI Retail Sales Forecasting Suite

🔗 Live App:
https://ai-retail-forecasting-f6aryhg3cdg5uz6a4lkkgs.streamlit.app/

A production-ready Retail Forecasting Dashboard that transforms Walmart’s weekly sales data into trend-aware, anomaly-aware, actionable predictions.

This project reflects a real enterprise ML workflow:

Data Upload → Time-Series Prep → Forecasting → Anomaly Detection → Model Evaluation → Export

Designed exactly like the tools used by retail analytics & ML engineering teams.

🚀 Key Features
🔹 1. Data Ingestion

Upload Walmart train.csv

Automated validation

Store & Department filtering

Weekly aggregation (group + sum)

Cleaned dataset preview

🔹 2. Time-Series Preparation

Converts raw transactional rows into weekly time-series

Handles multi-department and multi-store data

Generates Prophet-compatible format (ds, y)

Ensures no missing weekly timestamps

🔹 3. Forecast Engine

Supports three forecasting models:

Model	Description
Naive	Last week’s value repeats forward
Seasonal Naive	Previous year’s seasonal pattern repeats
Prophet	Trend + weekly + yearly seasonality, holiday effects

Features:

Forecast horizon: 4–24 weeks

Fully interactive

Clean forecast table

Forecast vs Actual plot

🔹 4. Anomaly Detection (Advanced Analytics Module) — ⭐ NEW ⭐

Detect unusual spikes or drops in weekly sales using two advanced methods.

1) Z-Score Based Detection (Statistical Outliers)

Detects points that deviate from the mean

Ideal for simple spike/drop detection

Threshold: 1–4

1–2: Sensitive

3–4: Strict

Very fast and lightweight

2) Prophet Residual Detection (AI-Based)

Uses Prophet model to compute:
Actual – Predicted = Residual

Flags weeks that violate trend + seasonality

Threshold: 4–10

4–6: Medium anomalies

7–10: Only extreme unusual behavior

Outputs:

✔ Highlighted anomaly points on the graph (red markers)
✔ Full anomaly table
✔ Works with any store/department
✔ Professional visual analytics

This module adds real business value, helping detect stockouts, holiday effects, promotions, or data inconsistencies.

🔹 5. Model Evaluation

Sliding window backtesting

Metrics:

MAE – Mean Absolute Error

MAPE – Mean Absolute Percentage Error

Visual comparison: Actual vs Predicted

🔹 6. Export

Download forecast output as CSV

Ready for Excel, BI dashboards, or reporting

🛠 Tech Stack

Python 3

Streamlit

Prophet

NumPy / Pandas

Matplotlib

Modular ML pipeline (clean architecture)

📂 Project Structure
sales-forecasting/
│
├── app/
│   ├── main.py
│   ├── pages/
│   │   ├── data_upload.py
│   │   ├── forecasting.py
│   │   ├── anomaly.py
│   │   ├── evaluation.py
│   │   └── export.py
│
├── src/
│   ├── loader.py
│   ├── preprocess.py
│   ├── models.py
│   ├── metrics.py
│   ├── plots.py
│   └── anomaly.py
│
├── screenshots/
├── requirements.txt
└── README.md

📸 Screenshots

(Add your own inside /screenshots folder)

🏠 Home

📤 Data Upload

🔮 Forecasting (Prophet)

⚠️ Anomaly Detection

📉 Model Evaluation

📦 Export

▶️ Run Locally
git clone <repository-url>
cd sales-forecasting

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

streamlit run app/main.py

📄 Dataset Source

Walmart Recruiting – Store Sales Forecasting
👉 https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting

⚠️ Dataset NOT included due to licensing.
Download train.csv manually and place inside:

data/train.csv

👩‍💻 Author

Mubara Khaqan
AI/ML Engineer | Applied Machine Learning | Retail Forecasting

