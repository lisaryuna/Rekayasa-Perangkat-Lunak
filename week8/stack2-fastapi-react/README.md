```markdown
# DevTask Tracker - Stack 2 (Non-JS Backend)

Versi ini memenuhi syarat penggunaan bahasa pemrograman non-JavaScript untuk sisi backend menggunakan **Python**.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React + Vite (JavaScript)
- **Data Persistence:** JSON File-based (`tasks.json`)

## Prerequisites
- Python 3.9+
- Node.js & npm

## Installation & Set-up

### Backend Setup
1. Masuk ke folder `backend`.
2. Buat virtual environment: `python -m venv venv`.
3. Aktifkan venv: `venv\Scripts\activate` (Windows).
4. Install dependensi:
   ```bash
   pip install fastapi uvicorn pydantic