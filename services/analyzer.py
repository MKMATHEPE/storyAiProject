from services.ai_engine import generate_ai_suggestion

def analyze_story(story):
    issues = []
    suggestions = []

    # Detect problems
    if story["completion_rate"] < 30:
        issues.append("Low completion rate")

    if story["clicks"] / story["views"] < 0.1:
        issues.append("Low click-through rate")

    # Generate AI-based feedback
    ai_feedback = generate_ai_suggestion(story)

    return {
        "story_id": story["story_id"],
        "title": story["title"],
        "issues": issues,
        "ai_feedback": ai_feedback
    }
