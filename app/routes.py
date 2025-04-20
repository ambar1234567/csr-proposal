from flask import current_app as app, request, render_template
from werkzeug.utils import secure_filename
import os
from app.utils.file_processor import process_file
from app.utils.ai_analyzer import analyze_proposal

def init_app(flask_app):
    @flask_app.route('/')
    def index():
        return render_template('index.html')

    @flask_app.route('/analyze', methods=['POST'])
    def analyze():
        if 'file' not in request.files:
            return "No file uploaded", 400
            
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            text = process_file(filepath)
            analysis = analyze_proposal(text)
            return render_template('results.html', result=analysis)
        except Exception as e:
            return f"Error processing file: {str(e)}", 500
