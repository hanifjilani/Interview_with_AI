import spacy
import fitz  # PyMuPDF
import re

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "Python", "Java", "Flask", "Django", "React", "SQL", "TensorFlow", "Pandas",
    "NumPy", "OpenCV", "Docker", "Kubernetes", "Git", "REST", "AWS", "GCP", "FastAPI"
]

def parse_resume(uploaded_file):
    # Save uploaded file to temp path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Use pyresparser to extract resume data
    data = ResumeParser(tmp_path).get_extracted_data()
    return data