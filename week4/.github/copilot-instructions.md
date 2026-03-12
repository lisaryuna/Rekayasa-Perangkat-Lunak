# Project Rules for Developer Command Center
- Environment: Python 3.13, Conda env `cs146s`.
- OS: Windows (Always suggest PowerShell commands).

## Automation Commands:
- Run Tests: `$env:PYTHONPATH="."; python -m pytest`
- Run App: `$env:PYTHONPATH="."; python -m uvicorn backend.app.main:app --reload`
- Fix Pydantic: Refactor class-based `Config` to `model_config = ConfigDict(from_attributes=True)`.

## Critical Fixes:
- Always use `engine.dispose()` before `os.unlink(db_path)` in `conftest.py` to avoid WinError 32.