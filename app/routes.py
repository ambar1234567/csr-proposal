from flask import current_app as app, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from app.utils.file_processor import process_file
from app.utils.ai_analyzer import analyze_proposal

def init_app(flask_app):
    """Initialize all routes with the Flask app"""
    
    @flask_app.route('/')
    def index():
        """Render the main upload page"""
        return render_template('index.html')

    @flask_app.route('/analyze', methods=['POST'])
    def analyze():
        """
        Handle file upload and analysis
        Returns: HTML response or JSON error
        """
        # Validate file exists in request
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
            
        file = request.files['file']
        
        # Validate filename
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        try:
            # Secure filename and create upload directory
            filename = secure_filename(file.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{datetime.now().timestamp()}_{filename}")
            
            # Save file
            file.save(filepath)
            
            # Process and analyze
            text = process_file(filepath)
            analysis = analyze_proposal(text)
            
            # Cleanup - remove file after processing
            if os.path.exists(filepath):
                os.remove(filepath)
                
            return render_template('results.html', result=analysis)
            
        except Exception as e:
            # Cleanup if error occurs
            if 'filepath' in locals() and os.path.exists(filepath):
                os.remove(filepath)
                
            app.logger.error(f"Analysis error: {str(e)}")
            return jsonify({
                "error": "Analysis failed",
                "details": str(e)
            }), 500

    @flask_app.route('/health')
    def health_check():
        """Health check endpoint for Render"""
        return jsonify({"status": "healthy"}), 200

    # Add more routes here as needed
