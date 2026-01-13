import streamlit as st
from src.anomaly import detect_anomalies_zscore, detect_anomalies_prophet
from src.plots import plot_anomalies

st.header("🚨 Anomaly Detection")

if "ts" not in st.session_state:
    st.error("Please upload and process data first.")
    st.stop()

ts = st.session_state["ts"]

method = st.selectbox(
    "Select Anomaly Detection Method",
    ["Z-Score Method", "Prophet Residual Method"]
)

if method == "Z-Score Method":
    threshold = st.slider("Z-Score Threshold", 1.5, 4.0, 2.5)
    processed, anomalies = detect_anomalies_zscore(ts, threshold)

else:
    threshold = st.slider("Deviation Threshold (%)", 10, 50, 25)
    threshold = threshold / 100
    processed, anomalies = detect_anomalies_prophet(ts, threshold)

st.subheader("Detected Anomalies")
st.dataframe(anomalies)

st.subheader("Anomaly Visualization")
st.pyplot(plot_anomalies(processed))

st.success(f"{len(anomalies)} anomalies detected.")
