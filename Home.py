import streamlit as st
from io import BytesIO


st.title("Welcome to Resume Friendly")
st.caption("Developed by Fábio A. Carvalho, 2025")


st.write("Resume AI Friendly helps you quickly and efficiently tailor your résumé to any job opening, following ATS best practices to maximize your chances of being seen.")

st.header("How ATS works")

st.write("ATS (Applicant Tracking System) is software used by companies to automate the recruitment process. It filters, ranks, and organizes résumés based on keywords and job criteria. Its goal is to streamline candidate screening. That’s why it’s essential to have a résumé optimized to pass through these systems.")

with open("./assets/img/ats.svg", "r") as f:
    ats_svg = f.read()

st.markdown(ats_svg, unsafe_allow_html=True)

st.header("How to Beat It")

st.write("When you apply for a job online, your résumé often goes through an ATS (Applicant Tracking System) before a human ever sees it. The ATS scans your résumé to check if it matches the job description, looking for specific keywords, skills, and formats.")

with open("./assets/img/ai-agent.svg", "r") as f:
    ai_agent_svg = f.read()

st.markdown(ai_agent_svg, unsafe_allow_html=True)

st.write("If your résumé isn’t aligned with what the ATS is looking for, it may get rejected automatically — even if you’re a great fit.")

content1 = """
To increase your chances: \n
	•	Use clear, standard formatting (avoid fancy designs or tables)
	•	Include keywords and skills from the job posting
	•	Write job titles and experiences that reflect the language used in the job description
	•	Avoid images or charts — the ATS can’t read them

Optimizing your résumé for ATS means making sure it speaks the same language as the job you want.
"""
st.write(content1)

with open("./assets/img/file-search.svg", "r") as f:
    found_svg = f.read()

st.markdown(found_svg, unsafe_allow_html=True)