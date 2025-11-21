import google.generativeai as genai

# IMPORTANT: put your API key here
genai.configure(api_key="AIzaSyARztgD7P6RC53lj5oNWQuHgnQE61w6Sbw")

model = genai.GenerativeModel("models/gemini-1.0-pro")

def analyze_with_llm(routines):
    if len(routines) == 0:
        return {"error": "No routines logged"}

    # Convert routines to structured text
    text = "Here are the student's routine logs:\n\n"
    for r in routines:
        text += f"- Activity: {r.activity}, Duration: {r.duration} min, Time: {r.timestamp}\n"

    prompt = f"""
You are an AI productivity coach. Analyze the following student routine logs:

{text}

Your task:
1. Identify the student's most productive hours
2. Detect patterns (focus time, screen overuse, study trends)
3. Give actionable productivity suggestions
4. Keep the explanation simple and clear

Return output in JSON with this format:

{{
  "summary": "...",
  "best_study_time": "...",
  "warnings": ["..."],
  "recommendations": ["...", "..."]
}}
"""

    # Call Gemini
    response = model.generate_content(prompt)

    return response.text
