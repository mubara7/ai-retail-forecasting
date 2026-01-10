📊 AI Retail Sales Forecasting App
🔗 Live Demo:
https://ai-retail-forecasting-f6aryhg3cdg5uz6a4lkkgs.streamlit.app/


A production-style Retail Forecasting Dashboard that transforms Walmart’s weekly sales data into actionable predictions using multiple forecasting models.
This app demonstrates a fully functional end-to-end ML pipeline used in real data-science teams:
data ingestion → cleaning → time-series preparation → forecasting → evaluation → export.
🚀 Features
🔹 1. Data Ingestion

Upload Walmart train.csv

Automatic validation & preview

Store and Department filters

Aggregation (sum)

🔹 2. Time-Series Preparation

Converts raw data into weekly time series

Handles multiple departments

Generates clean dataset for forecasting

🔹 3. Forecast Engine
Models included:

Model	Description
Naive	Last value repeats forward
Seasonal Naive	Last season’s pattern repeats
Prophet	Advanced trend + seasonal forecasting

Forecast 4–24 weeks

Prophet automatically handles trend + seasonality

🔹 4. Performance Evaluation

Sliding-window backtesting

Metrics:

MAE – Mean Absolute Error

MAPE – Mean Absolute Percentage Error

Visual comparison: Actual vs Predicted

🔹 5. Export
ownload forecast results as CSV

Ready for Excel / BI dashboards / client delivery

🛠 Tech Stack

Python 3

Streamlit

Prophet

Pandas / Numpy

Matplotlib

Clean modular pipeline architecture
📂 Project Structure
sales-forecasting/
│
├── app/
│   ├── main.py
│   ├── pages/
│   │   ├── data_upload.py
│   │   ├── forecasting.py
│   │   ├── evaluation.py
│   │   └── export.py
│
├── src/
│   ├── loader.py
│   ├── preprocess.py
│   ├── models.py
│   ├── metrics.py
│   └── plots.py
│
├── screenshots/
│   ├── home.png
│   ├── upload.png
│   ├── forecasting.png
│   ├── evaluation.png
│   └── export.png
│
├── data/
│   └── train.csv
│
├── requirements.txt
└── README.md
📸 Screenshots
🏠 Home

📤 Data Upload

🔮 Forecasting (Prophet Example)

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

This project uses the Walmart Recruiting – Store Sales Forecasting dataset from Kaggle.
You can download the dataset from the official competition page:

👉 https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting

⚠️ Note: Due to licensing restrictions, the raw dataset (train.csv) is not included in this repository.
Please download it manually from Kaggle and place it in the data/ folder when running the app locally.
👩‍💻 Author

Mubara Khaqan
AI/ML Engineer | Retail Forecasting | Applied Machine Learning
