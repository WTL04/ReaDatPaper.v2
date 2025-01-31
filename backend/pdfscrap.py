import fitz
import re
import torch
from transformers import pipeline

def fetch_pdf_content(pdf):
    with fitz.open(pdf) as doc:
        text = "\n".join([page.get_text() for page in doc])
    return text

# removes extra spaces or line breaks
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# Load summarization model from Hugging Face
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# Function to summarize text
def summarize_text(text):

    # using BART
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']


# -------testing scrapper---------

if __name__ == "__main__":
    test_pdf =   "test2.pdf"
    content = fetch_pdf_content(test_pdf)
    print(content)

'''
"CS Resume v.3.pdf"
"test1.pdf"
 "testarticle.pdf"
 "test2.pdf"
 '''
