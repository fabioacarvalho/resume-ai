import streamlit as st
from utils import generate_docx, generate_pdf, generate_docx_v2
from datetime import datetime

st.set_page_config(page_title="Resume AI Friendly", layout="wide")
st.title("💼 Resume AI Friendly")
st.write("Preencha os campos abaixo para gerar seu currículo otimizado para ATS.")

# Informacoes Pessoais
st.header("Informações Pessoais")
full_name = st.text_input("Nome completo")
location = st.text_input("Cidade - Estado")
phone = st.text_input("Telefone")
email = st.text_input("Email")
linkedin = st.text_input("LinkedIn")
github = st.text_input("GitHub (opcional)")

# Resumo
st.header("Resumo Profissional")
summary = st.text_area("Resumo profissional", height=100)

# Experiencias
st.header("Experiências Profissionais")
experiences = []
num_exp = st.number_input("Quantas experiências deseja adicionar?", min_value=1, max_value=10, value=1, step=1)
for i in range(num_exp):
    st.subheader(f"Experiência {i+1}")
    role = st.text_input(f"Cargo {i+1}", key=f"role_{i}")
    company = st.text_input(f"Empresa {i+1}", key=f"company_{i}")
    period = st.text_input(f"Período (ex: Jan/2020 - Dez/2022) {i+1}", key=f"period_{i}")
    description = st.text_area(f"Descrição das atividades {i+1}", key=f"desc_{i}")
    experiences.append({"role": role, "company": company, "period": period, "description": description})

# Educacao
st.header("Formação Acadêmica")
education = []
num_edu = st.number_input("Quantos cursos deseja adicionar?", min_value=1, max_value=5, value=1, step=1)
for i in range(num_edu):
    st.subheader(f"Formação {i+1}")
    degree = st.text_input(f"Curso {i+1}", key=f"degree_{i}")
    institution = st.text_input(f"Instituição {i+1}", key=f"inst_{i}")
    year = st.text_input(f"Ano de conclusão {i+1}", key=f"year_{i}")
    education.append({"degree": degree, "institution": institution, "year": year})

# Skills, Certificacoes, Idiomas
st.header("Outras Seções")
skills = st.text_area("Habilidades técnicas (separadas por vírgula)")
certifications = st.text_area("Certificações (opcional)")
languages = st.text_area("Idiomas (ex: Português: Nativo, Inglês: Avançado)")

# Organizar dados
data = {
    "full_name": full_name,
    "location": location,
    "phone": phone,
    "email": email,
    "linkedin": linkedin,
    "github": github,
    "summary": summary,
    "experiences": experiences,
    "education": education,
    "skills": skills,
    "certifications": certifications,
    "languages": languages
}

# Preview
st.header("🔍 Visualização do Currículo")
st.markdown(f"## {full_name}")
st.markdown(f"Cidade: {location} | Celular: {phone} | E-mail:  {email}")
st.markdown(f"LinkedIn: {linkedin} {(f'| GitHub: {github}' if github else '')}")
st.header("Resumo Profissional")
st.write(summary)

st.header("Experiências")
for exp in experiences:
    st.markdown(f"#### {exp['role']} - {exp['company']} ({exp['period']})")
    st.write(exp['description'])

st.header("Formação")
for edu in education:
    st.markdown(f"{edu['degree']} - {edu['institution']} ({edu['year']})")

st.header("Habilidades Técnicas")
st.write(skills)
if certifications.strip():
    st.header("Certificações")
    st.write(certifications)
if languages.strip():
    st.header("Idiomas")
    st.write(languages)

# Exportacao
st.header("📤 Exportar Currículo")
col1, col2 = st.columns(2)
with col1:

    if st.button("📄 Exportar como DOCX"):
        docx_path = generate_docx_v2(data)
        with open(docx_path, "rb") as f:
            st.download_button(
                label="Baixar DOCX",
                data=f,
                file_name="curriculo.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

with col2:
    st.write("Clique no botão ao lado para baixar o currículo em DOCX.")
    # if st.button("🔖 Exportar como PDF"):
    #     pdf_file = generate_pdf(data)
    #     st.download_button(label="Baixar PDF", data=pdf_file, file_name="curriculo.pdf")
