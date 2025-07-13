from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
from prompt_templates import base_prompt, jd_based_prompt


def generate_questions_from_resume(text):
    response = client.chat.completions.create(model="gpt-4o",
    messages=[{"role": "user", "content": base_prompt(text)}],
    temperature=0.7)
    return response.choices[0].message.content

def generate_questions_from_jd(text):
    response = client.chat.completions.create(model="gpt-4o",
    messages=[{"role": "user", "content": jd_based_prompt(text)}],
    temperature=0.7)
    return response.choices[0].message.content
