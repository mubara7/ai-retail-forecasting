## 🔗 Live Demo

Try the live deployed version of the app here:

👉 **https://projects-saoyz9dknac3eo9khxi7bz.streamlit.app/**

# 🧠 AI Hiring Assistant (Resume Shortlisting App)

An AI-powered web application that helps recruiters and HR teams automatically
analyze, rank, and shortlist resumes against a given job description.

This tool reduces manual screening time and provides transparent, keyword-based,
explainable matching results.

---

## 🚀 Features

- Upload multiple resumes (PDF, DOCX, TXT)
- Paste any job description
- Automatically rank resumes by relevance
- Adjustable shortlist threshold
- Clear decision labels (Strong / Moderate / Low match)
- Download ranked results as CSV
- Transparent keyword-based explainable scoring
- Simple, clean, HR-friendly UI

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** (Web UI)
- **PyPDF2 / python-docx** (Resume Parsing)
- **Custom scoring logic (keyword + similarity)**
- **Ubuntu + VS Code**

---

## 📂 Project Structure

ai-hiring-assistant/
├── app/
│ ├── main.py
│ ├── core/
│ │ ├── scoring.py
│ │ └── utils.py
│ └── services/
│ └── parsing.py
├── sample_data/
│ ├── sample_job_description.txt
│ └── sample_resumes/
├── screenshots/
│ ├── ui_empty.png
│ ├── ui_results.png
├── requirements.txt
├── .gitignore
└── README.md

---

## ▶️ How to Run the App

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the Streamlit app
PYTHONPATH=. streamlit run app/main.py
Open in browser:
👉 http://localhost:8501

⚙️ How It Works

Job description is cleaned and tokenized

Resume text is extracted from PDF/DOCX/TXT

Matching keywords are identified

A relevance score (0–100%) is calculated

Candidates are ranked

Based on threshold → a shortlist is created

HR can download results as CSV

📸 Screenshots
🔹 UI (Before Analysis)

🔹 Results (After Analysis)

🧩 Product Thinking

This app is designed from a recruiter’s perspective:

HR uploads resumes + JD

Instantly receives ranked results

Transparent scoring shows why a resume matches

Adjustable threshold helps in different hiring stages

Export to CSV supports collaboration with hiring managers

Hiring Flow:
Resume Upload → AI Scoring → Ranked List → Shortlist → CSV Download



🔮 Future Improvements

Replace keyword logic with embeddings / LLM scoring

End-to-end hiring automation using Make.com or n8n

Recruiter dashboard + analytics

Add semantic skill extraction & match heatmaps

👩‍💻 Author

Built as part of an AI Product Engineering portfolio with an end-to-end
focus on usability, automation, and transparent scoring.