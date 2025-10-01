from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def open_login(self) -> None:
        self.open(self.URL)

    def enter_username(self, username: str) -> None:
        self.type(*self.USERNAME_INPUT, text=username)

    def enter_password(self, password: str) -> None:
        self.type(*self.PASSWORD_INPUT, text=password)

    def click_login(self) -> None:
        self.click(*self.LOGIN_BUTTON)

    def get_flash_message(self) -> str:
        return self.text_of(*self.FLASH_MESSAGE)
