from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")
    yield driver
    driver.quit()

def test_login_page(browser):
    username_input = browser.find_element_by_name("username")
    password_input = browser.find_element_by_name("password")
    login_button = browser.find_element_by_name("login_button")

    username_input.send_keys("test_user")
    password_input.send_keys("test_password")
    login_button.click()

    assert "Главное окно" in browser.page_source
