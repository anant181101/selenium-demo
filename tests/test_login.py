from pages.login_page import LoginPage


def test_successful_login(chrome):
    page = LoginPage(chrome)
    page.open_login()
    page.enter_username("tomsmith")
    page.enter_password("SuperSecretPassword!")
    page.click_login()

    message = page.get_flash_message()
    assert "You logged into a secure area!" in message


def test_unsuccessful_login(chrome):
    page = LoginPage(chrome)
    page.open_login()
    page.enter_username("wrong")
    page.enter_password("creds")
    page.click_login()

    message = page.get_flash_message()
    assert "Your username is invalid!" in message
