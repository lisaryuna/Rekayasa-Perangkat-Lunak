# Week 7 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **Noor Khalisa** \
SUNet ID: **TODO** \
Citations: **Gemini AI & Blackbox AI for code generation and debugging assistance.**

This assignment took me about **3** hours to do. 


## Task 1: Add more endpoints and validations
a. Links to relevant commits/issues
> https://app.graphite.com/github/pr/lisaryuna/Rekayasa-Perangkat-Lunak/1

b. PR Description
> Added missing CRUD endpoints for Action Items and Notes (GET by ID, DELETE, PATCH). Implemented strict Pydantic validation using Field with min_length=1 and max_length constraints to prevent empty or oversized entries. Improved database reliability by using db.commit() for persistence.

c. Graphite Diamond generated code review
> Diamond successfully identified a missing min_length validation on the description field in the ActionItemPatch schema, ensuring that updates cannot bypass the original creation rules.

## Task 2: Extend extraction logic
a. Links to relevant commits/issues
> https://app.graphite.com/github/pr/lisaryuna/Rekayasa-Perangkat-Lunak/2

b. PR Description
> Enhanced the extraction logic using Python's re module to recognize multiple task formats: TODO:, Action Item:, and Markdown syntax (- [ ], * [ ]). Retained the fallback for lines ending with "!".

c. Graphite Diamond generated code review
> The AI suggested refining the Regular Expression to handle leading/trailing whitespace more robustly, ensuring that tasks are captured even with non-standard indentation.

## Task 3: Try adding a new model and relationships
a. Links to relevant commits/issues
> https://app.graphite.com/github/pr/lisaryuna/Rekayasa-Perangkat-Lunak/3

b. PR Description
>  Introduced a Category entity with a Many-to-One relationship to Note. Added a dedicated router for categories and updated the Note schema to include nested category information.

c. Graphite Diamond generated code review
> Diamond noted an ImportError risk regarding typing.list vs list in Python 3.13, which helped me fix a crash in the categories router before deployment.

## Task 4: Improve tests for pagination and sorting
a. Links to relevant commits/issues
> https://app.graphite.com/github/pr/lisaryuna/Rekayasa-Perangkat-Lunak/4

b. PR Description
> Added a comprehensive test suite test_notes_pagination_and_sorting. Verified that limit, skip, and sort parameters work correctly, especially concerning the backend's default -created_at ordering.

c. Graphite Diamond generated code review
> Diamond suggested using more descriptive test data (e.g., 'Alpha', 'Bravo') to make sorting failures easier to diagnose, which I implemented to verify alphabetical order.

## Brief Reflection 
a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).
> I focused on correctness (checking if the DB actually updated), API shape (ensuring field names matched the frontend's expectations), and test gaps (catching why tests failed on Windows). 

b. A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.
> My comments were broader, focusing on how the code integrated with the whole system. Graphite’s comments were "micro-focused", it was much better at catching tiny validation omissions and PEP8 style inconsistencies that I usually overlook.

c. When the AI reviews were better/worse than yours (cite specific examples)
> Better: In Task 1, catching the missing min_length in a Patch schema.
> Worse: In Task 2, Blackbox initially generated a Regex that was too clean, stripping the TODO: prefix and causing existing unit tests to fail. I had to manually adjust the capture groups to keep the prefix as required by the tests.

d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.
>I feel comfortable trusting AI for boilerplate and security validation (like schemas). However, for logic that depends on existing tests, I rely on a "Verify then Trust" heuristic—running the tests immediately after applying AI suggestions to ensure no regressions. 



