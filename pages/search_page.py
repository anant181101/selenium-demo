from selenium.webdriver.common.by import By
from .base_page import BasePage


class PythonOrgSearchPage(BasePage):
    URL = "https://www.python.org/"

    SEARCH_INPUT = (By.ID, "id-search-field")
    SEARCH_BUTTON = (By.ID, "submit")
    RESULTS = (By.CSS_SELECTOR, "ul.list-recent-events.menu li")

    def open_home(self) -> None:
        self.open(self.URL)

    def enter_query(self, query: str) -> None:
        self.type(*self.SEARCH_INPUT, text=query)

    def submit_search(self) -> None:
        self.click(*self.SEARCH_BUTTON)

    def has_results(self) -> bool:
        elements = self.driver.find_elements(*self.RESULTS)
        return len(elements) > 0
