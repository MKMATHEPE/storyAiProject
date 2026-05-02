from services.ai_engine import generate_ai_suggestion


def calculate_priority(story):
    score = 0

    completion_rate = story.get("completion_rate", 0)
    views = story.get("views", 0)
    clicks = story.get("clicks", 0)

    # Low completion = big problem
    if completion_rate < 30:
        score += 50

    # Low CTR (avoid division by zero)
    if views > 0:
        ctr = clicks / views
        if ctr < 0.1:
            score += 30

    # Low views (less urgent)
    if views < 600:
        score += 20

    return score


def analyze_story(story):
    issues = []

    completion_rate = story.get("completion_rate", 0)
    views = story.get("views", 0)
    clicks = story.get("clicks", 0)

    # Detect problems
    if completion_rate < 30:
        issues.append("Low completion rate")

    if views > 0 and (clicks / views) < 0.1:
        issues.append("Low click-through rate")

    if views < 600:
        issues.append("Low visibility")

    # Calculate priority score
    priority_score = calculate_priority(story)

    # Generate AI-based feedback
    ai_feedback = generate_ai_suggestion(story)

    return {
        "story_id": story.get("story_id"),
        "title": story.get("title"),
        "issues": issues,
        "priority_score": priority_score,
        "ai_feedback": ai_feedback
    }
