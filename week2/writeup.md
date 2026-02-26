# Week 2 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **Noor Khalisa** \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **3** hours to do. 


## YOUR RESPONSES
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.

### Exercise 1: Scaffold a New Feature
Prompt: 
```
I need to implement the extract_action_items_llm(text: str) function in app/services/extract.py. Please use the ollama Python client to generate the extraction. The prompt should instruct the LLM to extract actionable tasks from the text and output strictly as a structured JSON array of strings. Handle potential JSON parsing errors and edge cases like empty strings. Assume I am using the 'llama3.2' model locally.
``` 

Generated Code Snippets:
```
- app/services/extract.py: Lines 92-149 (Function `extract_action_items_llm` and its helper `_parse_json_array`)
```

### Exercise 2: Add Unit Tests
Prompt: 
```
Write pytest unit tests for the `extract_action_items_llm` function in `tests/test_extract.py`. Please use `unittest.mock.patch` to mock the `ollama.chat` API response so the tests run deterministically without needing the actual model running. Include test cases for: 1) A text with standard bullet points, 2) A text with keyword-prefixed lines (e.g., 'TODO:', 'Action:'), and 3) An empty input string.
``` 

Generated Code Snippets:
```
- tests/test_extract.py: (Fungsi test_extract_action_items_llm dengan implementasi unittest.mock.patch)
```

### Exercise 3: Refactor Existing Code for Clarity
Prompt: 
```
Refactor the backend code in the `app` directory for better maintainability:
1. Create a new file `app/schemas.py` and move all Pydantic models there (e.g., NoteCreate, ActionItemResponse).
2. Update `app/main.py` to import and use these schemas for all request/response bodies.
3. Fix the "Import could not be resolved" errors for fastapi and other modules in `app/main.py`.
4. Implement proper error handling using FastAPI's `HTTPException` (e.g., return a 404 if a note is not found, or a 500 if the LLM extraction fails).
``` 

Generated/Modified Code Snippets:
```
- app/schemas.py: (File baru berisi model Pydantic: NoteCreate, ActionItemResponse)
- app/main.py: (Integrasi schemas, perbaikan import FastAPI, dan penanganan HTTPException)
```


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt: 
```
I need to add a feature to list all saved notes from the database:
1. In `app/main.py`, create a new GET endpoint `/notes` that retrieves all notes from the database. Use the `ActionItemResponse` schema to return the data as a list.
2. In `frontend/index.html`, add a new button labeled 'List All Saved Notes' below the existing Extract button.
3. Update the JavaScript in `index.html` to fetch data from the new `/notes` endpoint and display each note's text along with its extracted action items in a new <div> section called 'note-history'. 
4. Ensure the UI updates dynamically without refreshing the page.
``` 

Generated Code Snippets:
```
- app/main.py: (Endpoint GET /notes untuk mengambil riwayat catatan)
- frontend/index.html: (Tombol 'List All Saved Notes' dan logika JavaScript fetch)
```


### Exercise 5: Generate a README from the Codebase
Prompt: 
```
@Codebase Analyze this entire project and generate a comprehensive README.md file. It must include:
1. A brief overview of the project (Action Item Extractor using FastAPI and Ollama).
2. Step-by-step instructions on how to set up and run the project (mentioning conda, poetry, and uvicorn).
3. Detailed documentation of all API endpoints, including the new /extract-llm and /notes endpoints.
4. Instructions for running the pytest suite.
``` 

Generated Code Snippets:
```
- README.md: (Seluruh dokumentasi proyek yang dihasilkan secara otomatis oleh AI Cursor)
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope. 