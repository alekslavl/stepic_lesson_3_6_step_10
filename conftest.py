import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="ru", help="Set user language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language", default="ru")
    
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    firefox_options = FirefoxOptions()
    firefox_options.set_preference("intl.accept_languages", user_language)
    
    browser_name = request.config.getoption("browser_name")
    browser = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()