# 🤖 AI-Powered Interview Question Generator


A smart and production-ready AI tool that analyzes resumes or job descriptions and generates tailored technical and behavioral interview questions using OpenAI's GPT models.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/OpenAI-GPT4o-brightgreen" />
  <img src="https://img.shields.io/badge/Streamlit-ready-orange" />
</div>

## 🎬 Demo

<p align="center">
  <img src="demo.gif"/>
</p>


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
<details>
  <summary>📄 Extracted information from uploaded resume — click to view</summary>

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

<h3>🔧 Technical Questions:</h3>

<h4>1. Django and Flask:</h4>
<p>Can you walk us through a project where you used Django or Flask? How did you decide which framework to use, and what challenges did you face during the development process?</p>
<h4>2. React and Node.js:</h4>
<p>Describe a project where you integrated React with a Node.js backend. How did you manage state and data flow between the front end and back end?</p>
<h4>3. SQL and MapReduce:</h4>
<p>You've mentioned engineering a segmented inverted index using a MapReduce pipeline. Can you explain what this project entailed and how you utilized SQL and MapReduce to optimize search efficiency?</p>

<h3>💬 Behavioral Questions:</h3>

<h4>1. Entrepreneurship:</h4>
<p>During your time at the Danish Institute for Study Abroad, you founded a simulated ride-share grocery startup. Can you describe a challenge you encountered in this project and how you overcame it?</p>
<h4>2. Teamwork and Collaboration:</h4>
<p>As a Backend Developer Intern at CLUES, how did you ensure effective collaboration with your team, especially when working on complex projects?</p>
<h4>3. Adaptability:</h4>
<p>You've had experience working in different countries and environments, such as the Danish Institute for Study Abroad and Hafa Math Academy in India. How did you adapt to these varying work cultures, and what did you learn from these experiences?</p>

<h2>📄 License</h2>
MIT License © Hanif Jilani <br>
Developed to empower learners, job seekers, and researchers with practical AI-driven tools.
