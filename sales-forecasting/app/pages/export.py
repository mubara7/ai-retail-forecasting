import streamlit as st

st.header("⬇ Export Forecast")

if "forecast" not in st.session_state:
    st.error("Create a forecast first.")
    st.stop()

fc = st.session_state["forecast"]

csv = fc.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download forecast.csv",
    data=csv,
    file_name="forecast.csv",
    mime="text/csv"
)
st.success("Downloaded!")
