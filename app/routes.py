from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from app import app
from app.utils.file_processor import process_file
from app.utils.ai_analyzer import analyze_proposal
from app.utils.scoring import calculate_scores
import json

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            try:
                # Process the file and extract text
                text = process_file(filepath)
                if not text:
                    flash('Could not extract text from the file')
                    return redirect(request.url)
                
                # Analyze the proposal using AI
                ai_analysis = analyze_proposal(text)
                
                # Calculate scores based on quality parameters
                scores = calculate_scores(ai_analysis)
                
                # Save results to display
                result = {
                    "filename": filename,
                    "text_preview": text[:1500] + "..." if len(text) > 1500 else text,
                    "scores": scores,
                    "feedback": ai_analysis.get("feedback", {}),
                    "ai_insights": ai_analysis.get("insights", "")
                }
                
                return render_template('results.html', result=result)
            
            except Exception as e:
                flash(f'Error processing file: {str(e)}')
                return redirect(request.url)
    
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']