# ResumeMatch - ATS Score Checker

ResumeMatch is a web application that analyzes resumes against job descriptions to provide an ATS (Applicant Tracking System) score. This score indicates how well the resume matches the job description, helping job seekers improve their resumes to better fit specific job postings.

## Features

- Upload resumes in PDF or DOCX format.
- Input job descriptions directly into the application.
- Get a detailed analysis and ATS score for the resume.
- User-friendly interface.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **AI**: OpenAI GPT-3
- **File Processing**: PyPDF2, docx2txt

## Installation

To get a local copy up and running, follow these steps.

### Prerequisites

- Python
- Flask
- OpenAI API key

### Installation Steps

1. Clone the repository
    ```sh
    git clone https://github.com/its-sushant/resumematch.git
    cd resumematch
    ```

2. Create and activate a virtual environment
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API key
    ```sh
    export OPENAI_API_KEY=<Your Api Key>
    ```

## Usage

1. Start the Flask application
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`

3. Use the application:
    - Input the job description in the provided text area.
    - Upload your resume in PDF or DOCX format.
    - Click "Analyze" to get the ATS score and detailed analysis.

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request