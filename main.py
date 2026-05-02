from fastapi import FastAPI, HTTPException
import json
from services.analyzer import analyze_story
from services.debugger import debug_story

app = FastAPI()

def load_stories():
    with open("data/stories.json") as f:
        return json.load(f)


@app.get("/")
def home():
    return {"message": "Story AI Analyzer is running"}


@app.get("/analyze")
def analyze():
    stories = load_stories()
    results = [analyze_story(story) for story in stories]
    return {"results": results}


@app.get("/debug/{story_id}")
def debug(story_id: int):
    stories = load_stories()

    story = next((s for s in stories if s["story_id"] == story_id), None)

    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    return debug_story(story)
