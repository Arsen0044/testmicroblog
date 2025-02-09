import time
from UI.Wait import Wait
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Logs.Logger import Logger


class BasePage(Wait):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)

    keys = Keys
    timeout = 5

    def get_element(self, locator: tuple[str, str], timeout=timeout, parent=None):
        if parent is None:
            parent = self.driver
        element = WebDriverWait(parent, timeout).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator: tuple[str, str], timeout=timeout, parent=None):
        if parent is None:
            parent = self.driver
        elements = WebDriverWait(parent, timeout).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_elements_when_present(self, locator: tuple[str, str], timeout=timeout):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def get_element_when_present(self, locator: tuple[str, str], timeout=timeout):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def send_keys(self, locator: tuple[str, str], value: str, timeout=timeout):
        self.visibility_of_element_located(locator, timeout=timeout)
        element = self.get_element(locator, timeout=timeout)
        element.clear()
        element.send_keys(value)

    def click_element(self, locator: tuple[str, str], timeout=timeout):
        self.presence_of_element_located(locator, timeout)
        self.element_to_be_clickable(locator, timeout)
        element = self.get_element_when_present(locator, timeout)
        element.click()

    def navigate(self, url: str) -> None:
        self.wait_for_page_load()
        self.driver.get(url)
        self.wait_for_page_load()

    def wait_for_page_load(self, time_out_sec=10):
        page_state = self.driver.execute_script('return document.readyState;')
        counter = 0
        while page_state != 'complete':
            if counter == time_out_sec * 2:
                break
            page_state = self.driver.execute_script('return document.readyState;')
            time.sleep(0.5)
            counter += 1

    def check_text_presence_in_page(self, txt):
        self.wait_for_page_load()
        page_source = self.driver.page_source
        if txt in page_source:
            return True
        return False


