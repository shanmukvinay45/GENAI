import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from Gemini
def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

# Function to extract text from a PDF
def extract_text_from_pdf(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ''.join(page.extract_text() for page in reader.pages)
    return text

# Prompt template for Gemini API
prompt_template = """
Hey, act like a skilled ATS (Applicant Tracking System) expert with knowledge in tech, software engineering, data science, data analysis, and big data. Evaluate the resume based on the given job description, providing suggestions for improvement. Match percentage should be based on JD and highlight missing keywords accurately.

Resume: {resume_text}
Job Description: {jd_text}

Expected response format:
{{"JD Match":"%", "MissingKeywords":[], "Profile Summary":""}}
"""

# Streamlit app
st.title("Smart ATS")
st.text("Optimize Your Resume for ATS")

# Job description input
jd_text = st.text_area("Paste the Job Description")

# PDF resume upload
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Upload your resume as a PDF")

# Submit button
if st.button("Submit") and uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    input_text = prompt_template.format(resume_text=resume_text, jd_text=jd_text)
    response = get_gemini_response(input_text)
    st.subheader("ATS Evaluation Results")
    st.write(response)
