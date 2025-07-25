import streamlit as st
from resume import parse_resume
from question_generator import generate_questions_from_resume, generate_questions_from_jd


st.set_page_config(page_title="AI Interview Question Generator", page_icon="🎯", layout="centered")

st.title("🎯 AI Interview Question Generator")

st.markdown("🚀 Upload a resume and generate smart, tailored interview questions.")

with st.expander("ℹ️ How this works"):
    st.markdown("This app parses your Resume or Job Description and uses OpenAI to generate technical and behavioral questions.")

option = st.radio("Choose Input Type:", ["Upload Resume", "Paste Job Description"])

if option == "Upload Resume":
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
    if uploaded_file:
        resume_json = parse_resume(uploaded_file)
        # st.text("Extracted Resume Text")
        # st.json(resume_json)
        resume_text = "\n".join([f"{k}: {v}" for k, v in resume_json.items() if v])
        # st.text_area("Extracted Resume Text", resume_text, height=200)
        if st.button("Generate Questions"):
            with st.spinner("Generating..."):
                output = generate_questions_from_resume(resume_text)
            st.markdown("### ✅ Suggested Questions")
            st.write(output)

else:
    jd_text = st.text_area("Paste Job Description", height=200)
    if jd_text and st.button("Generate Questions"):
        with st.spinner("Generating..."):
            output = generate_questions_from_jd(jd_text)
        st.markdown("### ✅ Suggested Questions")
        st.write(output)
