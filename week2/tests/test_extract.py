import pytest
from unittest.mock import patch

from ..app.services.extract import extract_action_items, extract_action_items_llm


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_bullets(mock_chat):
    text = """
    Meeting notes:
    - Set up CI pipeline
    - Review pull requests
    """.strip()

    mock_chat.return_value = {
        "message": {
            "content": '["Set up CI pipeline", "Review pull requests"]',
        }
    }

    items = extract_action_items_llm(text)

    assert items == ["Set up CI pipeline", "Review pull requests"]
    mock_chat.assert_called_once()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_keyword_prefixes(mock_chat):
    text = """
    TODO: write documentation for the API
    Action: schedule follow-up meeting
    """.strip()

    mock_chat.return_value = {
        "message": {
            "content": """
            ```json
            ["write documentation for the API", "schedule follow-up meeting"]
            ```
            """.strip(),
        }
    }

    items = extract_action_items_llm(text)

    assert "write documentation for the API" in items
    assert "schedule follow-up meeting" in items
    mock_chat.assert_called_once()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_empty_input(mock_chat):
    items = extract_action_items_llm("")

    assert items == []
    mock_chat.assert_not_called()
