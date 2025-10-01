import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="session")
def chrome() -> webdriver.Chrome:
    options = Options()

    # Honor an explicit Chrome binary if provided (e.g., in containers/CI)
    chrome_bin = os.getenv("CHROME_BIN") or os.getenv("GOOGLE_CHROME_SHIM")
    if chrome_bin:
        options.binary_location = chrome_bin

    # Default to headless unless explicitly disabled
    if os.getenv("CI") or os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes"):
        options.add_argument("--headless=new")

    # Stability flags for headless/CI/containerized environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=1280,1024")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-background-networking")

    # Use Selenium Manager (built into Selenium) to resolve the correct driver.
    # This avoids ChromeDriver/Chrome version mismatch issues.
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode",
    )


@pytest.fixture(autouse=True)
def _apply_headless(pytestconfig):
    if pytestconfig.getoption("--headless"):
        os.environ["HEADLESS"] = "true"
