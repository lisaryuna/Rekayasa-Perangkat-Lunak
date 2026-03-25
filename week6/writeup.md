# Week 6 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **Noor Khalisa** \
SUNet ID: **TODO** \
Citations: **Gemini AI (used as the AI coding tool for code refactoring and mitigation explanations)**

This assignment took me about **2** hours to do. 


## Brief findings overview 
> Based on the Semgrep scan (using `p/default` and `p/secrets` rulesets locally), the tool reported **6 SAST (Code) findings**. No hardcoded secrets were found. The SCA (Supply Chain) scan was skipped because the CLI was run in local/offline mode.

## Fix #1
a. File and line(s)
> `week6/backend/app/main.py`, Line 24

b. Rule/category Semgrep flagged
> `python.fastapi.security.wildcard-cors.wildcard-cors` (SAST)

c. Brief risk description
> Using a wildcard (`*`) for CORS allows any origin to access the API. This is insecure as it opens the application up to Cross-Origin attacks, allowing malicious third-party websites to make unauthorized requests on behalf of authenticated users.

d. Your change (short code diff or explanation, AI coding tool usage)
> AI Usage: I prompted Gemini AI with: *"Semgrep flagged `allow_origins=["*"]` as insecure CORS in FastAPI. How do I fix this to only allow my local frontend on port 3000?"*
> Change: I replaced the wildcard with specific trusted origins.
> Before: `allow_origins=["*"],`
> After: `allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],`

e. Why this mitigates the issue
> This mitigates the risk by enforcing a strict CORS policy. The API will now explicitly reject cross-origin requests from unrecognized domains, only trusting the explicitly defined local frontend addresses.

## Fix #2
a. File and line(s)
> `week6/backend/app/routers/notes.py`, Lines 71-81

b. Rule/category Semgrep flagged
> `python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text` (SAST)

c. Brief risk description
> The code used Python f-strings to inject the user-controlled `q` variable directly into the `sqlalchemy.text()` function. This creates a critical SQL Injection vulnerability, allowing attackers to input malicious SQL payloads to read or modify the database.

d. Your change (short code diff or explanation, AI coding tool usage)
> AI Usage: I provided the raw SQL query to Gemini and asked: "Refactor this SQLAlchemy text() query to use parameterized queries to prevent SQL injection."
> Change: I removed the f-string interpolation and used named parameters instead.
> Before: `WHERE title LIKE '%{q}%' OR content LIKE '%{q}%'` and `db.execute(sql)`
> After: `WHERE title LIKE :search OR content LIKE :search` and `db.execute(sql, {"search": f"%{q}%"})`

e. Why this mitigates the issue
> By using parameterized queries, the database driver treats the user input strictly as literal data rather than executable SQL commands. Any malicious SQL syntax injected by the user will be safely escaped and ignored by the database engine.

## Fix #3
a. File and line(s)
> `week6/frontend/app.js`, Line 14

b. Rule/category Semgrep flagged
> `javascript.browser.security.insecure-document-method.insecure-document-method` (SAST)

c. Brief risk description
> Unvalidated user data (`n.title` and `n.content`) was being written directly into the DOM using the `innerHTML` property. This creates a DOM-based Cross-Site Scripting (XSS) vulnerability, allowing an attacker to execute malicious JavaScript in the victim's browser.

d. Your change (short code diff or explanation, AI coding tool usage)
> AI Usage: I provided the JS line to Gemini and asked: "Semgrep flagged `li.innerHTML` as an XSS vulnerability. Rewrite this using secure DOM manipulation methods."
> Change: I replaced `innerHTML` with `document.createElement()` and `textContent`.
> Before: `li.innerHTML = "<strong>${n.title}</strong>: ${n.content}";`
> After: > ```javascript
> const strong = document.createElement('strong');
> strong.textContent = n.title;
> li.appendChild(strong);
> li.appendChild(document.createTextNode(`: ${n.content}`));
> ```

e. Why this mitigates the issue
> The `textContent` property and `createTextNode` method automatically sanitize and encode HTML characters. If an attacker inputs a `<script>` tag, the browser will render it safely as plain text on the screen rather than executing it as code.