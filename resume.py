import re
import spacy
import fitz  # PyMuPDF

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load dynamic skill set from file
def load_skills(filepath="skills.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f if line.strip())

# Extract skills with strict match (avoiding partial overlaps)
def extract_skills(text, skills_set):
    text_lower = text.lower()
    matched = set()
    for skill in skills_set:
        if re.search(r"\b" + re.escape(skill) + r"\b", text_lower):
            matched.add(skill)
    return list(matched)

# Extract degrees with stricter patterns and post-process
def extract_degrees(text):
    degree_patterns = [
        r"(Bachelor(?:'s)? of [A-Za-z\s]+)",
        r"(Master(?:'s)? of [A-Za-z\s]+)",
        r"(Ph\.?D\.?|Doctorate of [A-Za-z\s]+|D\.Phil)",
        r"(B\.?S\.?|B\.?Tech|M\.?Tech|M\.?S\.?|MBA|B\.?E\.?|M\.?E\.?) in [A-Za-z\s]+",
        r"(M\.?D\.?|Doctor of Medicine)",
        r"(B\.?Pharm|M\.?Pharm|Pharm\.?D)",
        r"(LLB|LL\.?M\.?|Bachelor of Law)",
        r"(Bachelor of Public Health|Master of Public Health|B\.?P\.?H\.?|M\.?P\.?H\.?)",
    ]
    found = set()
    for pattern in degree_patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                match = " ".join([m for m in match if m])
            match = match.strip()
            if len(match) > 3 and not match.islower():
                found.add(match)
    return list(found)

# Clean noisy orgs using skill list filter
def extract_organizations(doc, skill_set):
    raw_orgs = set(ent.text.strip() for ent in doc.ents if ent.label_ == "ORG")
    filtered_orgs = [
        org for org in raw_orgs
        if org.lower() not in skill_set and not re.search(r'[{}<>@]', org) and len(org.strip()) > 2
    ]
    return filtered_orgs

# Get experience lines with better heuristics
def extract_experience(doc):
    return [
        sent.text.strip() for sent in doc.sents
        if any(x in sent.text.lower() for x in ["experience", "intern", "developer", "engineer", "worked"])
    ][:10]

# Extract email and phone using regex
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r"\+?\d[\d\-\s]{8,15}\d", text)
    return match.group() if match else None

# Remove numbers and extra symbols from name
def clean_name(name):
    return re.sub(r"[^a-zA-Z\s]", "", name).strip() if name else None

# Main parsing function
def parse_resume(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    raw = "\n".join(page.get_text() for page in doc)
    text = re.sub(r'\s+', ' ', raw).strip()  # 🧼 clean text
    spacy_doc = nlp(text)
    skill_set = load_skills()

    name = next((ent.text for ent in spacy_doc.ents if ent.label_ == "PERSON"), None)

    return {
        "name": clean_name(name),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text, skill_set),
        "degree": extract_degrees(text),
        "organizations": extract_organizations(spacy_doc, skill_set),
        "experience": extract_experience(spacy_doc),
    }