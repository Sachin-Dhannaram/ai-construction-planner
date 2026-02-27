from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate_project
from schedule import generate_schedule
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/app")
def serve_frontend():
    return FileResponse("static/index.html")

class ProjectInput(BaseModel):
    area: float
    floors: int
    timeline: int

@app.get("/")
def home():
    return {"message": "AI Construction Planner Running 🚀"}

@app.post("/calculate")
def calculate(data: ProjectInput):
    cost_data = calculate_project(data.area, data.floors, data.timeline)
    schedule = generate_schedule(data.timeline)

    return {
        "cost_analysis": cost_data,
        "schedule": schedule
    }
API_KEY = "AIzaSyANkkycdaEmDz9unfa4qgzd8rPoYD7dJ5A"

@app.post("/explain")
def explain_project(data: ProjectInput):

    result = calculate_project(data.area, data.floors, data.timeline)

    prompt = f"""
You are a senior construction planning consultant.

Analyze the following project and generate a structured professional report.

Project Details:
- Area per Floor: {data.area} sq.ft
- Number of Floors: {data.floors}
- Timeline: {data.timeline} days
- Estimated Cost: ₹{result['total_cost']}

Respond clearly using these exact sections:

## Executive Summary
## Cost Analysis
## Timeline Risk Assessment
## Resource Efficiency Insight
## Optimization Recommendation

Keep it concise, practical, and under 700 words.
Avoid unnecessary filler sentences.
"""

    url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "maxOutputTokens": 1400,
            "temperature": 0.6
        }
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        return {"error": response.text}

    result_json = response.json()

    try:
        ai_text = result_json["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return {"error": "Unexpected AI response format"}

    return {"ai_explanation": ai_text}