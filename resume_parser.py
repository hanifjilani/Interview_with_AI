import tempfile
from pyresparser import ResumeParser

def parse_resume(uploaded_file):
    # Save the uploaded resume PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Use pyresparser to extract resume data
    data = ResumeParser(tmp_path).get_extracted_data()
    return data