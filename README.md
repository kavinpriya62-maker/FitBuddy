# FitBuddy — AI Fitness Plan Generator

A simple Flask web app that creates a general fitness plan using the Groq API.

## Features
- Choose a fitness goal, experience level, weekly schedule, equipment, and session duration.
- Generates a structured plan using an AI model.
- Includes general safety reminders.

## Requirements
- Python 3.10 or newer
- A Groq API key

## Run locally

1. Open a terminal in this project folder.
2. Create a virtual environment:
   - Windows: `python -m venv venv`
   - macOS/Linux: `python3 -m venv venv`
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env`.
6. Open `.env` and put your key after `GROQ_API_KEY=`.
7. Start the app: `python app.py`
8. Open `http://127.0.0.1:5000` in your browser.

## API key safety
Keep `.env` private. Never upload your real API key to GitHub. The `.gitignore`
file excludes it from Git.

## Deployment
Set the environment variable `GROQ_API_KEY` in your hosting provider's dashboard.
Use a production WSGI server for deployment; do not use Flask's debug server
in production.

## Health and safety
Plans are general information, not medical advice. Start at a comfortable level,
allow recovery time, and stop if exercise causes pain, dizziness, or feeling unwell.
Ask a qualified healthcare professional about exercise if you have health concerns.
