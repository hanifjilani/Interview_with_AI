def base_prompt(resume_text):
    return f"""
You are a helpful AI HR assistant.

Below is a candidate's resume:
\"\"\"
{resume_text}
\"\"\"

Generate 5 technical and 5 behavioral interview questions for this candidate. Keep questions clear, and tailored to the resume.
"""

def jd_based_prompt(job_description):
    return f"""
You are an expert recruiter.

Based on the following job description:
\"\"\"
{job_description}
\"\"\"

Generate 5 technical and 5 behavioral questions that test core competencies, technologies, and behavioral fit.
"""