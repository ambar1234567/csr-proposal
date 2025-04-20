import openai
from config import Config
import json

def analyze_proposal(text):
    """Analyze proposal text using OpenAI API"""
    try:
        openai.api_key = Config.OPENAI_API_KEY
        
        prompt = f"""
        Analyze this CSR project proposal based on the following quality parameters:
        1. Language (Grammar, writing style, alignment with objectives)
        2. Literature Review (Relevant data, source reliability, timeliness of data)
        3. Presentation (Graphical presentation, formatting)
        4. Risk Mitigation (Identification of risks and solutions to address them)
        5. Budget (Detailed breakdown of accurate budget)
        
        Provide detailed feedback for each parameter and an overall assessment.
        The proposal text is:
        {text[:12000]}  # Limiting to 12k tokens
        
        Return the response in JSON format with these keys:
        - "language_analysis"
        - "literature_review_analysis"
        - "presentation_analysis"
        - "risk_mitigation_analysis"
        - "budget_analysis"
        - "overall_feedback"
        - "strengths"
        - "weaknesses"
        - "recommendations"
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a CSR proposal expert analyzing project proposals for quality."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2000
        )
        
        analysis = response.choices[0].message.content
        return json.loads(analysis)
    
    except Exception as e:
        return {
            "error": str(e),
            "feedback": {
                "language_analysis": "Could not analyze due to error",
                "literature_review_analysis": "Could not analyze due to error",
                "presentation_analysis": "Could not analyze due to error",
                "risk_mitigation_analysis": "Could not analyze due to error",
                "budget_analysis": "Could not analyze due to error",
                "overall_feedback": "Analysis failed due to technical error"
            }
        }