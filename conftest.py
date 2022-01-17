import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: fr or ru or es")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    options = Options()
    if language == 'fr':
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': 'fr-FRA, fr'})
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", 'fr-FRA, fr')
        #browser = webdriver.Firefox(firefox_profile=fp)
    elif language == 'ru':
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': 'ru-RUS, ru'})
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", 'ru-RUS, ru')
        #browser = webdriver.Firefox(firefox_profile=fp)
    elif language == 'es':
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': 'es-SPA, es'})
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", 'es-SPA, es')
        #browser = webdriver.Firefox(firefox_profile=fp)
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
