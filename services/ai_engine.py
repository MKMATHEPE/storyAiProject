import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_suggestion(story):
    prompt = f"""
    Analyze this story performance:

    Title: {story.get('title')}
    Views: {story.get('views')}
    Clicks: {story.get('clicks')}
    Completion Rate: {story.get('completion_rate')}%

    Explain what is wrong and suggest improvements.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception:
        # 🔥 fallback logic if API fails
        return fallback_suggestion(story)


def fallback_suggestion(story):
    issues = []

    completion_rate = story.get("completion_rate", 0)
    views = story.get("views", 0)
    clicks = story.get("clicks", 0)

    if completion_rate < 30:
        issues.append("Users are dropping off early")

    if views > 0 and (clicks / views) < 0.1:
        issues.append("Low engagement with CTA")

    if views < 600:
        issues.append("Low visibility")

    if not issues:
        return "Story is performing well"

    return " | ".join(issues) + ". Consider improving structure and engagement."
