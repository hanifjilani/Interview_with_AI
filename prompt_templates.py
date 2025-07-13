def base_prompt(resume_text):
    return f"""
 You are a helpful AI HR assistant.

Below is the structured output from a resume parser. Please note that some information might not be perfectly categorized: skills may appear in the experience section, and organization names might include tool names or locations. Use your judgment to interpret the resume holistically.

Resume Data:
\"\"\"
{resume_text}
\"\"\"

Generate 3 technical and 3 behavioral interview questions for this candidate. Keep questions clear, and tailored to the resume.
"""

def jd_based_prompt(job_description):
    return f"""
You are an expert recruiter.

Based on the following job description:
\"\"\"
{job_description}
\"\"\"

Generate 3 technical and 3 behavioral questions that test core competencies, technologies, and behavioral fit.
"""