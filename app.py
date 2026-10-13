import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
app = Flask(__name__)

def create_fitness_plan(goal, level, days, equipment, minutes):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return (
            "Your AI key is not configured yet.\n\n"
            "1. Copy .env.example to a file named .env\n"
            "2. Add your Groq API key after GROQ_API_KEY=\n"
            "3. Restart the app and generate your plan again.\n\n"
            "Safety: Start gently, warm up, drink water, and stop if you feel "
            "pain, dizziness, or unwell. This app provides general fitness "
            "information, not medical advice."
        )

    prompt = f"""
Create a practical, beginner-safe general fitness plan.
Goal: {goal}
Fitness level: {level}
Days per week: {days}
Available equipment: {equipment}
Time per session: {minutes} minutes

Format the response with:
1. A short warm-up
2. A day-by-day weekly plan, with exercises and sets/reps or time
3. Rest/recovery guidance
4. Simple general hydration and balanced-food reminders
5. A short cool-down

Keep it realistic and encouraging. Include easier alternatives.
Do not recommend extreme exercise, restrictive dieting, supplements,
or exercising through pain. Mention that this is general information,
not medical advice, and that users with health concerns should ask a
qualified healthcare professional before starting.
"""
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a careful, supportive general fitness planning assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=1200,
        )
        return response.choices[0].message.content
    except Exception as exc:
        app.logger.exception("Fitness plan generation failed")
        return (
            "Sorry, the plan could not be generated right now. Check that your "
            "GROQ_API_KEY is valid and that your internet connection is working. "
            "Please try again later."
        )

@app.route("/", methods=["GET", "POST"])
def index():
    plan = None
    error = None
    if request.method == "POST":
        goal = request.form.get("goal", "General fitness")
        level = request.form.get("level", "Beginner")
        days = request.form.get("days", "3")
        equipment = request.form.get("equipment", "No equipment")
        minutes = request.form.get("minutes", "20")
        try:
            if int(days) not in range(1, 8):
                raise ValueError
            if int(minutes) not in (10, 15, 20, 30, 45, 60):
                raise ValueError
        except ValueError:
            error = "Please choose a valid number of days and session duration."
        else:
            plan = create_fitness_plan(goal, level, days, equipment, minutes)
    return render_template("index.html", plan=plan, error=error)

if __name__ == "__main__":
    app.run(debug=True)
