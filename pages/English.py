import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Editable Resume", layout="wide")
st.title("📝 Resume AI Friendly – Resume Editor")

st.write("Wait a moment! This page is under construction. Please check back later.")

# # === Basic Info ===
# st.header("Basic Information")
# full_name = st.text_input("Full Name")
# location = st.text_input("City – State")
# phone = st.text_input("Phone")
# email = st.text_input("Email")
# linkedin = st.text_input("LinkedIn")
# github = st.text_input("GitHub (optional)")

# # === Summary ===
# st.header("Professional Summary")
# summary = st.text_area("Summary", "Backend Developer with X years of experience building APIs...")

# # === Experience ===
# st.header("Professional Experience")

# def experience_input(role, default_company="", default_desc=""):
#     company = st.text_input(f"{role} – Company Name", value=default_company)
#     location = st.text_input(f"{role} – Location (City, State)")
#     date_range = st.text_input(f"{role} – Period (e.g., Jan 2022 – Present)")
#     desc = st.text_area(f"{role} – Responsibilities", value=default_desc)
#     return company, location, date_range, desc

# company1, loc1, date1, desc1 = experience_input("Backend Developer")
# company2, loc2, date2, desc2 = experience_input("Fullstack Developer")

# # === Education ===
# st.header("Education")
# education = st.text_input("Degree (e.g., Bachelor's Degree)")
# institution = st.text_input("Institution Name")
# grad_year = st.text_input("Graduation Year")

# # === Skills ===
# st.header("Technical Skills")
# skills = st.text_area("List of Skills", "Python, Django, Flask, PostgreSQL, Docker, Git...")

# # === Certifications ===
# st.header("Certifications (Optional)")
# certs = st.text_area("Certifications", "- XYZ Certification – Institution – Year")

# # === Languages ===
# st.header("Languages (Optional)")
# languages = st.text_area("Languages", "- Portuguese: Native\n- English: Fluent")

# # === Output ===
# st.markdown("---")
# st.subheader("📄 Resume Preview")

# resume = f"""
# **{full_name}**  
# {location} | {phone} | {email} | {linkedin}{" | " + github if github else ""}

# ---

# ### PROFESSIONAL SUMMARY  
# {summary}

# ---

# ### PROFESSIONAL EXPERIENCE  

# **Backend Developer**  
# {company1} – {loc1}  
# {date1}  
# {desc1}

# **Fullstack Developer**  
# {company2} – {loc2}  
# {date2}  
# {desc2}

# ---

# ### EDUCATION  
# {education} – {institution}  
# {grad_year}

# ---

# ### TECHNICAL SKILLS  
# {skills}

# """

# if certs.strip():
#     resume += f"\n---\n### CERTIFICATIONS\n{certs}\n"

# if languages.strip():
#     resume += f"\n---\n### LANGUAGES\n{languages}\n"

# st.code(resume, language="markdown")