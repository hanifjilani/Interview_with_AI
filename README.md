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
Experience: - Backend Intern at HafaWorks: Automated billing with Google Calendar API - Web Dev at Amaanat NGO: Built websites for women-led businesses Skills: Python, Flask, SQL, AWS, React
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
