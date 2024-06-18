from flask import Flask, request, render_template, jsonify
import openai
import PyPDF2
import docx2txt
import os

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)

def gpt_analyze_resume(resume_text, job_description):
    prompt = f"Analyze the following resume text for its relevance to the job description provided.\n\nJob Description:\n{job_description}\n\nResume Text:\n{resume_text}\n\nScore the resume out of 100 and provide a brief explanation."
    messages = []
    messages.append({'role': 'user', 'content': f"{prompt}"})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    job_description = request.form['job_description']
    resume_file = request.files['resume_file']
    file_extension = os.path.splitext(resume_file.filename)[1].lower()

    if file_extension == '.pdf':
        resume_text = extract_text_from_pdf(resume_file)
    elif file_extension == '.docx':
        resume_text = extract_text_from_docx(resume_file)
    else:
        return jsonify({'error': 'Unsupported file type'}), 400

    analysis_result = gpt_analyze_resume(resume_text, job_description)
    return jsonify({'analysis': analysis_result})

if __name__ == '__main__':
    app.run(debug=True)
