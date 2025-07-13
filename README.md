# 🤖 AI-Powered Interview Question Generator


A smart and production-ready AI tool that analyzes resumes or job descriptions and generates tailored technical and behavioral interview questions using OpenAI's GPT models.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/OpenAI-GPT4o-brightgreen" />
  <img src="https://img.shields.io/badge/Streamlit-ready-orange" />
</div>

## 📌 What This Project Does

This app lets users:

1. **Upload a resume (.pdf) or Provide Job Description**
2. **Automatically extract key information** using a custom parser (no broken dependencies!)
3. **Send the structured info to GPT-4o**
4. **Generate 3 technical + 3 behavioral interview questions**, customized to your skills and experiences

## ✨ Features

✅ Custom resume parser (uses `spaCy`, `fitz`, `regex`)  
✅ Dynamic skill extraction from `skills.txt`  
✅ Degree & organization detection (medical, law, tech, etc.)  
✅ GPT-powered interview question generation  
✅ Streamlit-ready interface  
✅ Modular, extensible code structure  

---
## 🚀 Setup Instructions

### 🔹 1. Clone the repo

```bash
git clone https://github.com/yourusername/ai-interview-question-generator.git
cd ai-interview-question-generator
```
### 🔹 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
# OR
venv\Scripts\activate         # On Windows
```
### 🔹 3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
### 🔹 4. Add your OpenAI API key
```bash
Create .streamlit/secrets.toml file and then add
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
### 🔹 4. Run the Application
```bash
streamlit run app.py
```

<h2>🧪 Example Output</h2>
From the Uploaded Resume, extracts the following
<details>
  <summary>🧠 From the Uploaded Resume, extracts the following information. Click to view!</summary>

```json
{
  "name": "Hanif Jilani",
  "email": "hanif@umich.edu",
  "phone": "734-596-6393",
  "skills": [
    "entrepreneurship",
    "aws",
    "sql",
    "python",
    "c",
    "mysql",
    "react",
    "django",
    "javascript",
    "node.js",
    "flask",
    "git"
  ],
  "degree": [
    "Bachelor of Science in Engineering"
  ],
  "organizations": [
    "Comparators",
    "Learning Management Systems",
    "India •",
    "Google/Bing",
    "MI • Optimized",
    "Figma",
    "LMS",
    "SEO",
    "CSS",
    "University of Michigan Ann Arbor",
    "Danish Institute for Study Abroad Copenhagen",
    "Madoop",
    "Magento",
    "C/C++",
    "Github Private Repo",
    "Education University",
    "HTML/CSS Frameworks",
    "Google",
    "MapReduce",
    "Data-Driven Web Applications",
    "India • Built",
    "Projects LC2K Simulator & Assembler",
    "Denmark • Founded",
    "Present University of Michigan Ann Arbor",
    "Hafa Math Academy Chennai",
    "MI • Integrated",
    "Swagger.io",
    "HTML",
    "University Honors",
    "MS Project, MS Office"
  ],
  "experience": [
    "Education University of Michigan - College of Engineering Ann Arbor, MI Bachelor of Science in Engineering, Computer Science GPA:",
    "Awards: Engineering Dean’s List (Fall 2022, Spring 2024), University Honors (Fall 2022) •",
    "Courses: Web Systems, Data-Driven Web Applications, Discrete Math, Computational Linear Algebra Experience Backend Developer Intern at CLUES",
    "Entrepreneurship Study/Internship Abroad May 2023 – July 2023 Danish Institute for Study Abroad Copenhagen, Denmark • Founded Gro-share-ies, simulated ride-share grocery startup targeting college students.",
    "Backend Developer Intern May 2021 – Sep. 2021 Hafa Math Academy Chennai, India •",
    "Web Developer Intern Apr 2021 – Apr 2021",
    "Engineered a segmented inverted index using a MapReduce pipeline, optimizing search efficiency.",
    "SQL Clone | Github Private Repo | C++ Feb 2024 – March 2024 • Engineered a relational database system supporting insert, remove, select, print, index, and join queries.",
    "Technical Skills Languages: Python, C/C++, MySQL, JavaScript, HTML/CSS Frameworks: Flask, Django, Node.js, React, Dialogflow Developer Tools: Git, Google Cloud Platform, VS Code, Figma, MS Project, MS Office"
  ]
}
```

</details>
➡️ The app generates:

🔧 Technical Questions:

How would you integrate Google Calendar API with a backend to manage billing?

What are some challenges in deploying Flask apps on AWS?

Explain how you would structure a web app using React and Flask.

💬 Behavioral Questions:

Tell me about a time you had to deliver a project with tight deadlines.

How did you approach building accessible tech for underprivileged users?

Describe a time you worked across a cross-functional team.

<h2>📄 License</h2>
MIT License © Hanif Jilani
Crafted with 💙 for students, job seekers, and AI tinkerers.
