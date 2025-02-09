import pytest
from Logs.Logger import Logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from UI.Web.Pages.LoginPage.LoginPage import LoginPage
from UI.Web.Utilities.read_config import Constants


def __get_driver():
    Logger.log.debug('Get local driver')
    options = Options()
    options.add_argument('--window-size=1920,3000')
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    _driver.maximize_window()
    win_size_dic = _driver.get_window_size()
    Logger.log.info('screen width: ' + str(win_size_dic['width']))
    Logger.log.info('screen height: ' + str(win_size_dic['height']))
    _driver.implicitly_wait(1)
    return _driver

@pytest.fixture(scope='class')
def get_dashboard_with_login_class():
    Logger.log.info('Do log in to dashboard')
    driver = __get_driver()
    login_page = LoginPage(driver, navigate=True)
    dashboard_page = login_page.do_login(Constants.user_name, Constants.password)
    dashboard_page.wait_for_page_load()
    yield dashboard_page
    Logger.log.info('FIXTURE teardown get_dashboard_with_login')

