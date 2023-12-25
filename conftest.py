import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage
from pages.alerts_page import AlertsPage

@pytest.fixture(scope="function")
def browser() -> webdriver:
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function", autouse=True)
def authorized_user(browser):
    link = "https://test-hg.isi-technology.com/"
    login_page = LoginPage(browser, link)
    login_page.login_in_as_authorized_user()

@pytest.fixture(scope="function")
def teardown_new_alert(browser):
    yield
    print("\nTeardown of new added alert is beginning..")
    link = "https://test-hg.isi-technology.com/#!/alert"
    alerts_page = AlertsPage(browser, link)
    alerts_page.open()
    alerts_page.remove_alert(isChanged=False)

@pytest.fixture(scope="function")
def teardown_existing_alert(browser):
    yield
    print("\nTeardown of existing alert is beginning..")
    link = "https://test-hg.isi-technology.com/#!/alert"
    alerts_page = AlertsPage(browser, link)
    alerts_page.open()
    alerts_page.remove_alert(isChanged=True)
