# Selenium Demo (Python + Pytest)

A tiny, beginner-friendly Selenium test automation project using Python, Pytest, pytest-html, and webdriver-manager. It demonstrates the Page Object Model (POM), a reusable Chrome WebDriver fixture, and a couple of practical tests.

## Prerequisites
- Python 3.9+
- Google Chrome installed

## Setup
```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\\Scripts\\activate

# 2) Install dependencies
pip install -r requirements.txt
```

## Run Tests
Basic run (generates an HTML report):
```bash
pytest -q --html=report.html --self-contained-html
```

Headless mode (useful in CI or servers without a display):
```bash
pytest -q --html=report.html --self-contained-html --headless
```

## Project Structure
```
selenium-demo/
├── tests/
│   ├── test_login.py
│   ├── test_search.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── search_page.py
├── conftest.py
├── requirements.txt
├── README.md
```

## What the tests do
- Login test opens `https://the-internet.herokuapp.com/login`, attempts a valid and invalid login, and checks the resulting flash message.
- Search test opens `https://www.python.org/`, searches for a keyword, and asserts that results are displayed.

## Notes
- WebDriver binaries are managed automatically by `webdriver-manager` — no manual download needed.
- If Chrome is not on your PATH or you use Chromium, you can set `GOOGLE_CHROME_SHIM` or adjust options in `conftest.py`.
- To run headed (visible browser) locally, omit `--headless` and ensure `HEADLESS=false` in your environment.
