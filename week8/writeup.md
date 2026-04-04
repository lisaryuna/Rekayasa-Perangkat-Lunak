# Week 8 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **Noor Khalisa** \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **TODO** hours to do. 


## App Concept 
```
TODO: Provide a brief, high-level overview of your app, highlighting its main features. This overview should be the same across all three app versions.
```


## Version #1 Description
```
APP DETAILS:
===============
Folder name: stack1-bolt
AI app generation platform: Bolt.new
Tech Stack: React (Frontend) + Node.js environment
Persistence: Local state / In-memory
Frameworks/Libraries Used: React, Vite, Tailwind CSS, Lucide React (for icons)
(Optional but recommended) Screenshots of core flows: TODO

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them: Finding the export/download button in the new Bolt.new UI was slightly confusing as it was hidden behind the code view. Resolved this by switching to the < > (Code) mode to locate the file structure and utilizing the GitHub sync feature to safely pull the generated code to my local machine.

b. Prompting (e.g. what required additional guidance; what worked poorly/wel): Providing a very detailed initial prompt ("Build a full-stack DevTask Tracker application... The primary resource is 'Tasks'...") worked extremely well. Bolt understood the assignment scope immediately and generated a clean, responsive UI with full CRUD capabilities in a single shot without needing major follow-up corrections.

c. Approximate time-to-first-run and time-to-feature metrics: 
ime-to-first-run (preview in browser): ~2 minutes.
Time-to-feature (fully working CRUD): ~5 minutes.
```

## Version #2 Description
```
APP DETAILS:
===============
Folder name: stack2-fastapi-react
AI app generation platform: N/A - Built locally with AI Chat Assistant (Gemini)
Tech Stack: Python (Backend) + JavaScript (Frontend)
Persistence: File-based storage (tasks.json)
Frameworks/Libraries Used: FastAPI, Uvicorn, Pydantic (Backend); React, Vite, Axios (Frontend)
(Optional but recommended) Screenshots of core flows: TODO

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them: Managing multiple terminals for the backend and frontend simultaneously on Windows caused some pathing issues (e.g., Cannot find path...). Resolved by systematically navigating to the correct directories (cd week8/stack2-fastapi-react) before running the server commands. Also encountered a 404 error when visiting 127.0.0.1:8000/, which was resolved by navigating to the specific /tasks API endpoint.

b. Prompting (e.g. what required additional guidance; what worked poorly/wel): I had to ask the AI for step-by-step local setup instructions since Bolt.new does not natively support running full Python backend servers (like FastAPI) efficiently. The AI provided precise terminal commands for Windows PowerShell to set up the virtual environment (venv) and bridge the FastAPI backend with the React frontend using CORS.

c. Approximate time-to-first-run and time-to-feature metrics: 
Time-to-first-run: ~15 minutes (due to manual environment setup).
Time-to-feature: ~20 minutes.
```

## Version #3 Description
```
APP DETAILS:
===============
Folder name: stack3-flask-vanilla
AI app generation platform: N/A - Built locally with AI Chat Assistant (Gemini)
Tech Stack: Python (Backend) + HTML/Vanilla JS (Frontend)
Persistence: Relational Database (SQLite)
Frameworks/Libraries Used: Flask, SQLite3, Vanilla JavaScript (Fetch API)
(Optional but recommended) Screenshots of core flows: TODO

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them: Encountered an [Errno 2] No such file or directory error when trying to run the Flask server. Resolved this by checking my working directory in the terminal; I was in the parent week8 folder instead of the stack3-flask-vanilla folder where app.py was located. Moving to the correct folder fixed the execution.

b. Prompting (e.g. what required additional guidance; what worked poorly/wel): I specifically prompted for a distinct architecture to contrast with the decoupled Frontend/Backend approach of Stack 1 and Stack 2. The AI guided me to build a Monolith architecture where Flask serves a single HTML template, and Vanilla JS handles the asynchronous DOM updates. This satisfied the distinct stack requirement perfectly.

c. Approximate time-to-first-run and time-to-feature metrics: 
Time-to-first-run: ~10 minutes.
Time-to-feature: ~15 minutes.
```
