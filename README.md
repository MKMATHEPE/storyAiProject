# storyAiDasboard

Story AI Dashboard is a lightweight analytics prototype for analyzing short-form “Stories” content performance.

It goes beyond basic metrics by detecting engagement issues, explaining them, and prioritizing what should be fixed — simulating how a product team investigates and improves user engagement.

✨ Features
	•	📊 Story performance dashboard
	•	⚖️ Priority scoring (what to fix first)
	•	🚨 Issue detection
	•	Low completion rate
	•	Low click-through rate
	•	Low visibility
	•	🤖 AI-generated insights (with fallback support)
	•	🔍 Debug endpoint for deep investigation
	•	🎯 Decision-focused UI (not just analytics)

  🛠 Tech Stack
	•	Python + FastAPI
	•	HTML, CSS, Vanilla JavaScript
	•	OpenAI API (optional, with fallback logic)

  ⚙️ How It Works
  Frontend → FastAPI → Analyzer → AI/Fallback → Insights
  •	/analyze → returns stories with issues + priority
	•	/summary → dashboard-level insights
	•	/debug/{id} → detailed diagnosis for a story

🚀 Getting Started
pip install fastapi uvicorn openai

Optional (for AI insights):
export OPENAI_API_KEY="your_api_key"

Run the backend:
uvicorn main:app --reload

Open:
index.html


  🎯 Purpose

  This project demonstrates how AI can support product workflows:
	•	Detect engagement problems
	•	Prioritize what matters
	•	Explain performance issues
	•	Turn data into actionable decisions
