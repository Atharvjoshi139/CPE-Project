from flask import Flask, render_template, request, send_file
import pdfkit

app = Flask(__name__)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    # Assuming marks data comes from a form or database
    marks_data = [
        {"roll": 1, "name": "John Doe", "marks": 85},
        {"roll": 2, "name": "Jane Smith", "marks": 90}
    ]
    rendered = render_template('pdf_template.html', marks=marks_data)
    pdf = pdfkit.from_string(rendered, False)
    response = send_file(pdf, as_attachment=True, download_name='marks.pdf')
    return response
