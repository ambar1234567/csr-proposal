import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the AI model (will auto-download on first run)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def analyze_proposal(text):
    """
    Analyzes CSR proposals using free HuggingFace models
    Returns scores (0-20 per category) and feedback
    """
    
    # Define what a good proposal should contain
    quality_aspects = [
        "Professional language with clear grammar and structure",
        "Recent and reliable data sources with proper citations",
        "Detailed risk assessment with practical mitigation plans",
        "Comprehensive budget breakdown with justification",
        "Strong alignment with CSR objectives and impact metrics"
    ]
    
    # Convert text and aspects to numerical vectors
    text_vector = model.encode([text])
    aspect_vectors = model.encode(quality_aspects)
    
    # Calculate similarity scores (0-1)
    similarity_scores = cosine_similarity(text_vector, aspect_vectors)[0]
    
    # Prepare results
    results = {
        "scores": {
            "Language": round(similarity_scores[0] * 20, 1),
            "Literature Review": round(similarity_scores[1] * 20, 1),
            "Risk Mitigation": round(similarity_scores[2] * 20, 1),
            "Budget": round(similarity_scores[3] * 20, 1),
            "Objective Alignment": round(similarity_scores[4] * 20, 1)
        },
        "total_score": round(sum(similarity_scores) * 20, 1),  # 0-100 scale
        "feedback": generate_feedback(quality_aspects, similarity_scores)
    }
    
    return results

def generate_feedback(aspects, scores):
    """Generates simple strength/improvement feedback"""
    feedback = {"Strengths": [], "Improvements": []}
    
    for i, score in enumerate(scores):
        if score >= 0.7:  # High similarity
            feedback["Strengths"].append(aspects[i])
        elif score <= 0.4:  # Low similarity
            feedback["Improvements"].append(aspects[i])
    
    # Default message if no strong matches
    if not feedback["Strengths"]:
        feedback["Strengths"].append("Clear project vision")
    if not feedback["Improvements"]:
        feedback["Improvements"].append("Could benefit from more detailed implementation plan")
    
    return feedback
