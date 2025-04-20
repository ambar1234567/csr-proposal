def calculate_scores(analysis):
    """Calculate scores based on AI analysis"""
    if "error" in analysis:
        return {
            "Language": 0,
            "Literature Review": 0,
            "Presentation": 0,
            "Risk Mitigation": 0,
            "Budget": 0,
            "Total Score": 0
        }
    
    # This is a simplified scoring - you might want to make it more sophisticated
    # based on the actual analysis content
    scores = {
        "Language": score_from_feedback(analysis.get("language_analysis", "")),
        "Literature Review": score_from_feedback(analysis.get("literature_review_analysis", "")),
        "Presentation": score_from_feedback(analysis.get("presentation_analysis", "")),
        "Risk Mitigation": score_from_feedback(analysis.get("risk_mitigation_analysis", "")),
        "Budget": score_from_feedback(analysis.get("budget_analysis", ""))
    }
    
    total_score = sum(scores.values())
    scores["Total Score"] = total_score
    
    return scores

def score_from_feedback(feedback):
    """Convert feedback text to a score (0-20)"""
    positive_words = ["excellent", "strong", "good", "well", "comprehensive", "detailed", "clear"]
    negative_words = ["weak", "poor", "lacking", "missing", "unclear", "needs improvement"]
    
    positive_count = sum(1 for word in positive_words if word.lower() in feedback.lower())
    negative_count = sum(1 for word in negative_words if word.lower() in feedback.lower())
    
    base_score = 10  # Average score
    score = base_score + (positive_count * 2) - (negative_count * 2)
    
    # Ensure score is between 0 and 20
    return max(0, min(20, score))