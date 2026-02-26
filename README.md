## CS146S – The Modern Software Developer Assignments

This repository contains the assignments for [CS146S: The Modern Software Developer](https://themodernsoftware.dev), taught at Stanford University (Fall 2025).

The root of the repository holds shared tooling and configuration (e.g., `pyproject.toml`). Individual assignments live in subdirectories such as `week2/`.

---

## Week 2 – Action Item Extractor (FastAPI + Ollama)

### Overview

The Week 2 project, located in `week2/`, is an **Action Item Extractor** web application built with:

- **FastAPI** for the backend API.
- **SQLite** for persistent storage of notes and extracted action items.
- **Ollama** running a local **`llama3.2`** model for LLM-powered extraction.
- A minimal **HTML/JS frontend** served by FastAPI.

Users paste free-form meeting notes into the frontend, and the backend:

- Extracts actionable tasks using a combination of heuristics and an LLM (`extract_action_items_llm`).
- Stores notes and action items in a SQLite database.
- Lets you list saved notes and their associated action items.

---

## Environment and Tooling Setup

These steps assume **Python 3.12** and an OS where you can install Conda and Poetry.

### 1. Install Anaconda (for Conda)

- Download and install: [Anaconda Individual Edition](https://www.anaconda.com/download).
- Open a new terminal so `conda` is on your `PATH`.

### 2. Create and activate a Conda environment

```bash
conda create -n cs146s python=3.12 -y
conda activate cs146s
```

### 3. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python -
```

Make sure Poetry is on your `PATH` (you may need to restart the terminal or follow the installer’s instructions).

### 4. Install project dependencies with Poetry

From the **repository root** (where `pyproject.toml` lives):

```bash
poetry install --no-interaction
```

This installs:

- `fastapi`, `uvicorn`
- `pydantic`
- `python-dotenv`
- `ollama`
- Dev tools such as `pytest`, `black`, `ruff`, etc.

### 5. Install and configure Ollama + model

1. Install **Ollama** from the official site (`https://ollama.com`).
2. Start the Ollama service (usually automatic after install).
3. Pull the **`llama3.2`** model:

   ```bash
   ollama pull llama3.2
   ```

4. (Optional) Set an environment variable to override the default model name:

   ```bash
   # If you want to use a different local model name
   set OLLAMA_MODEL=llama3.2  # Windows (PowerShell: $env:OLLAMA_MODEL="llama3.2")
   # or
   export OLLAMA_MODEL=llama3.2  # macOS/Linux
   ```

If `OLLAMA_MODEL` is not set, the backend defaults to `llama3.2`.

---

## Running the Week 2 Application

1. **Activate the Conda environment**:

   ```bash
   conda activate cs146s
   ```

2. **Start the backend with Uvicorn via Poetry**:

   From the **repository root**:

   ```bash
   cd week2
   poetry run uvicorn app.main:app --reload
   ```

   This will:

   - Initialize the SQLite database under `week2/data/app.db`.
   - Start FastAPI with hot reload on `http://127.0.0.1:8000`.

3. **Open the frontend**:

   - Navigate to `http://127.0.0.1:8000/` in your browser.
   - You’ll see a simple UI with:
     - A textarea for notes.
     - A “Save as note” checkbox.
     - An **Extract** button.
     - A **List All Saved Notes** button.
     - A live-updating list of extracted action items and note history.

---

## API Overview

The FastAPI application for Week 2 is defined in `week2/app/main.py`, with route modules in `week2/app/routers/`.

Below is a summary of all relevant endpoints.

### 1. Root and Static Assets

- **GET `/`**
  - **Description**: Serves the main HTML frontend (`frontend/index.html`).
  - **Response**: Raw HTML.

- **Static files**: `/static`
  - **Description**: Mounted static directory (`frontend/`), not typically used directly in this assignment but available for assets.

### 2. Notes API (`/notes` router + main-level listing)

#### POST `/notes`

- **Description**: Create a new note.
- **Request body** (`NoteCreate`):

  ```json
  {
    "content": "Free-form note text..."
  }
  ```

- **Responses**:
  - `201` (FastAPI will respond with `200` by default unless configured otherwise):
    - Body (`NoteResponse`):

      ```json
      {
        "id": 1,
        "content": "Free-form note text...",
        "created_at": "2025-01-01T12:34:56"
      }
      ```

  - `400`:
    - Occurs if `content` is empty / only whitespace.
    - Body:

      ```json
      { "detail": "content is required" }
      ```

#### GET `/notes/{note_id}`

- **Description**: Retrieve a single note by ID.
- **Path parameters**:
  - `note_id` (int): ID of the note.
- **Responses**:
  - `200` – `NoteResponse` as above.
  - `404` – Note not found:

    ```json
    { "detail": "note not found" }
    ```

#### GET `/notes` (main app endpoint – list notes with items)

- **Description**: List **all notes along with their extracted action items**.
- **Implementation**:
  - Defined in `app.main:list_notes`.
  - Uses the `NoteWithItemsResponse` schema:

    ```json
    [
      {
        "id": 1,
        "content": "Some note text",
        "created_at": "2025-01-01T12:34:56",
        "items": [
          {
            "id": 10,
            "note_id": 1,
            "text": "Set up database",
            "done": false,
            "created_at": "2025-01-01T12:35:00"
          }
        ]
      }
    ]
    ```

- **Responses**:
  - `200` – JSON array (possibly empty).

> **Note**: The assignment text refers to a “new `/notes` endpoint”; that is this **list-all** endpoint, distinct from the `/notes/{note_id}` GET.

### 3. Action Item Extraction API (`/action-items` router)

#### POST `/action-items/extract`

- **Description**:
  - Extracts action items from free-form text.
  - Optionally saves the original text as a note.
  - Uses LLM-powered extraction via `extract_action_items_llm` (Ollama + `llama3.2`), with a heuristic fallback.

- **Request body** (`ActionItemsExtractRequest`):

  ```json
  {
    "text": "Meeting notes here...",
    "save_note": true
  }
  ```

  - `text`: Required note body.
  - `save_note`: Optional boolean, defaults to `false`. If `true`, the note is stored in the `notes` table and linked to the created action items.

- **Responses**:
  - `200` – `ActionItemsExtractResponse`:

    ```json
    {
      "note_id": 1,
      "items": [
        {
          "id": 10,
          "note_id": 1,
          "text": "Set up CI pipeline",
          "done": false,
          "created_at": "2025-01-01T12:35:00"
        },
        {
          "id": 11,
          "note_id": 1,
          "text": "Review pull requests",
          "done": false,
          "created_at": "2025-01-01T12:35:05"
        }
      ]
    }
    ```

  - `400` – Missing text:

    ```json
    { "detail": "text is required" }
    ```

  - `500` – LLM extraction failed:

    ```json
    { "detail": "Failed to extract action items" }
    ```

> **About `/extract-llm` vs `/action-items/extract`**  
> The assignment wording mentions a `/extract-llm` endpoint. In the actual implementation, LLM-based extraction is exposed via **`POST /action-items/extract`**. That route internally uses `extract_action_items_llm` (Ollama + `llama3.2`) and falls back to heuristics if the LLM call fails or returns invalid JSON.

#### GET `/action-items`

- **Description**: List all action items, optionally filtered by `note_id`.
- **Query parameters**:
  - `note_id` (optional, int): If provided, only action items for that note are returned.
- **Responses**:
  - `200` – List of `ActionItemResponse`:

    ```json
    [
      {
        "id": 10,
        "note_id": 1,
        "text": "Set up CI pipeline",
        "done": false,
        "created_at": "2025-01-01T12:35:00"
      }
    ]
    ```

#### POST `/action-items/{action_item_id}/done`

- **Description**: Mark an action item as done/undone.
- **Path parameters**:
  - `action_item_id` (int): The ID of the action item.
- **Request body** (`ActionItemDoneRequest`):

  ```json
  {
    "done": true
  }
  ```

  - `done` defaults to `true` if omitted.

- **Responses**:
  - `200`:

    ```json
    {
      "id": 10,
      "done": true
    }
    ```

  - `500`:
    - If updating the action item fails for any reason:

      ```json
      { "detail": "Failed to update action item" }
      ```

---

## Frontend Behaviour (`frontend/index.html`)

The frontend is a simple HTML page with inline JavaScript:

- **Extract flow**:
  - Reads text from `#text`.
  - Sends `POST /action-items/extract` with `{ text, save_note }`.
  - Renders checkboxes for each returned action item.
  - When checkboxes are toggled, sends `POST /action-items/{id}/done` with `{ done: true/false }`.

- **List All Saved Notes flow**:
  - Clicking the **“List All Saved Notes”** button triggers:
    - `GET /notes` (the main-list endpoint).
    - Renders each note in the `#note-history` div:
      - Note metadata: ID and `created_at`.
      - Original note content.
      - Bullet list of extracted action items (or a message if none).
  - All updates are dynamic; the page is never reloaded.

---

## Running the Test Suite (pytest)

The Week 2 tests live under `week2/tests/`. They primarily validate:

- The heuristic and LLM-based extraction logic (`extract_action_items` and `extract_action_items_llm`).
- The LLM client is mocked using `unittest.mock.patch` so that tests do **not** require a running Ollama model.

### From the repository root

1. Ensure the Conda environment is active:

   ```bash
   conda activate cs146s
   ```

2. Run tests via Poetry:

   ```bash
   poetry run pytest week2
   ```

   This will:

   - Discover tests in `week2/tests/`.
   - Run them with the installed dependencies from `pyproject.toml`.

You can also run all tests for the entire repo (if future weeks add more):

```bash
poetry run pytest
```

---

## Directory Structure (Week 2)

Key files for the Week 2 project:

- `week2/app/main.py` – FastAPI app factory, root routes, and the `/notes` list endpoint.
- `week2/app/schemas.py` – Pydantic models for requests and responses.
- `week2/app/db.py` – SQLite database helpers (init, CRUD for notes and action items).
- `week2/app/services/extract.py` – Heuristic and LLM-based action item extraction logic.
- `week2/app/routers/notes.py` – `/notes` create/get endpoints.
- `week2/app/routers/action_items.py` – `/action-items` extraction and status endpoints.
- `week2/frontend/index.html` – Minimal HTML+JS frontend.
- `week2/tests/test_extract.py` – pytest tests for extraction logic.

This README should give you everything you need to set up the environment, run the app, understand the available APIs (including the LLM-powered extraction and `/notes` listing), and execute the test suite.***