from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from services.analyzer import analyze_story
from services.debugger import debug_story

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    results.sort(key=lambda x: x["priority_score"], reverse=True)
    return {"results": results}


@app.get("/summary")
def summary():
    stories = load_stories()
    results = [analyze_story(story) for story in stories]

    total = len(results)
    low_completion = sum(1 for r in results if "Low completion rate" in r["issues"])
    low_ctr = sum(1 for r in results if "Low click-through rate" in r["issues"])

    return {
        "total_stories": total,
        "low_completion_stories": low_completion,
        "low_ctr_stories": low_ctr,
        "insight": f"{low_completion} stories have low completion rates, which is the main engagement issue."
    }


@app.get("/debug/{story_id}")
def debug(story_id: int):
    stories = load_stories()
    story = next((s for s in stories if s.get("story_id") == story_id), None)

    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    return debug_story(story)
