from services.ai_engine import generate_ai_suggestion

def debug_story(story):
    explanation = generate_ai_suggestion(story)

    return {
        "story_id": story["story_id"],
        "title": story["title"],
        "diagnosis": explanation
    }
