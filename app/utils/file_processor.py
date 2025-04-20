import os
import PyMuPDF
from docx import Document
import re

def process_file(filepath):
    """Process PDF or DOCX file and extract text"""
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    
    try:
        if ext == '.pdf':
            return extract_text_from_pdf(filepath)
        elif ext == '.docx':
            return extract_text_from_docx(filepath)
    except Exception as e:
        raise Exception(f"Error processing file: {str(e)}")
    
    return None

def extract_text_from_pdf(filepath):
    """Extract text from PDF using PyMuPDF"""
    text = ""
    with open(filepath, 'rb') as file:
        doc = PyMuPDF.open(file)
        for page in doc:
            text += page.get_text()
    return clean_text(text)

def extract_text_from_docx(filepath):
    """Extract text from DOCX"""
    doc = Document(filepath)
    text = "\n".join([para.text for para in doc.paragraphs])
    return clean_text(text)

def clean_text(text):
    """Clean extracted text"""
    # Remove multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    return text