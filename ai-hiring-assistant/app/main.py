import sys
import os

# Add project root to sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st

from app.services.parsing import parse_resume
from app.core.scoring import rank_resumes

st.set_page_config(page_title="AI Hiring Assistant", page_icon="🧠", layout="wide")

st.title("🧠 AI Hiring Assistant (Resume Shortlisting)")
st.caption("Upload multiple resumes, paste a job description, and get ranked matches with scores.")

job_desc = st.text_area("📌 Paste Job Description", height=200, placeholder="Paste the job description here...")

uploaded = st.file_uploader(
    "📄 Upload Resumes (PDF, DOCX, or TXT) — multiple files allowed",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

col1, col2 = st.columns([1, 1])
with col1:
    top_k = st.number_input("How many top candidates to shortlist?", min_value=1, max_value=50, value=5, step=1)
with col2:
    threshold = st.slider("Shortlist score threshold (%)", min_value=0, max_value=100, value=60, step=1)

run_btn = st.button("🚀 Analyze Resumes", type="primary")

if run_btn:
    if not job_desc.strip():
        st.error("Please paste a Job Description first.")
        st.stop()
    if not uploaded:
        st.error("Please upload at least 1 resume.")
        st.stop()

    resumes = []
    for f in uploaded:
        text = parse_resume(f.name, f.read())
        resumes.append((f.name, text))

    results = rank_resumes(resumes, job_desc)

    st.subheader("📊 Ranked Results")
    st.dataframe(results, use_container_width=True)

    shortlist = [r for r in results if r["score"] >= threshold][: int(top_k)]

    st.subheader("✅ Shortlist")
    if shortlist:
        st.success(f"{len(shortlist)} candidates shortlisted.")
        st.dataframe(shortlist, use_container_width=True)
    else:
        st.warning("No candidate meets the shortlist threshold. Try lowering the threshold.")

    # CSV download (without pandas)
    import csv
    from io import StringIO

    def to_csv(rows):
        if not rows:
            return ""
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
        return output.getvalue()

    st.download_button(
        "⬇️ Download ranked results CSV",
        data=to_csv(results),
        file_name="ranked_results.csv",
        mime="text/csv",
    )
