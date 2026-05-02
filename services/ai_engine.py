import os
from openai import OpenAI


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return None  # 🔥 allows fallback instead of crashing

    return OpenAI(api_key=api_key)


def generate_ai_suggestion(story):
    client = get_client()

    # If no API key → use fallback immediately
    if client is None:
        return fallback_suggestion(story)

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
            messages=[{"role": "user", "content": prompt}],
            timeout=10
        )

        if response and response.choices:
            return response.choices[0].message.content

        return fallback_suggestion(story)

    except Exception as e:
        print(f"⚠️ AI Error: {e}")
        return fallback_suggestion(story)


def fallback_suggestion(story):
    issues = []

    completion_rate = story.get("completion_rate", 0)
    views = story.get("views", 0)
    clicks = story.get("clicks", 0)

    if completion_rate < 30:
        issues.append("Users are dropping off early")

    if views > 0 and (clicks / views) < 0.1:
        issues.append("Low engagement with call-to-action")

    if views < 600:
        issues.append("Low visibility")

    if not issues:
        return "Story is performing well with no major issues detected."

    return " | ".join(issues) + ". Consider improving structure, hook, and engagement strategy."
