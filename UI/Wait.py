from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement

from Logs.Logger import Logger


class Wait:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.identify_locator = ''

    def __wait(self, timeout):
        return WebDriverWait(self.driver, timeout, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                 ElementNotSelectableException, ElementClickInterceptedException])

    def element_to_be_clickable(self, identify_locator: tuple[str, str], timeout=5):
        self.identify_locator = identify_locator
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until(EC.element_to_be_clickable(identify_locator)))

    def element_not_to_be_clickable(self, identify_locator: tuple[str, str], timeout=5):
        self.identify_locator = identify_locator
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until_not(EC.element_to_be_clickable(identify_locator)))

    def presence_of_element_located(self, identify_locator: tuple[str, str], timeout=5):
        self.identify_locator = identify_locator
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until(EC.presence_of_element_located(identify_locator)))

    def not_presence_of_element_located(self, identify_locator: tuple[str, str], timeout=5):
        self.identify_locator = identify_locator
        return self.__is_the_condition_approve(lambda:  self.__wait(timeout)
                                               .until_not(EC.presence_of_element_located(identify_locator)))

    def visibility_of_element_located(self, identify_locator: tuple[str, str], timeout=5):
        self.identify_locator = identify_locator
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until(EC.visibility_of_element_located(identify_locator)))

    def not_visibility_of_element_located(self, identify_locator: tuple[str, str], timeout=5):
        self.identify_locator = identify_locator
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until_not(EC.visibility_of_all_elements_located(identify_locator)))

    def element_to_be_selected(self, element: WebElement, timeout=5):
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until(EC.element_to_be_selected(element)))

    def element_not_to_be_selected(self, element: WebElement, timeout=5):
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until_not(EC.element_to_be_selected(element)))

    def text_to_be_present_in_element(self, identify_locator: tuple[str, str], text, timeout=5):
        self.identify_locator = identify_locator
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until(EC.text_to_be_present_in_element(identify_locator, text)))

    def text_not_be_present_in_element(self, identify_locator: tuple[str, str], text, timeout=5):
        self.identify_locator = identify_locator
        return self.__is_the_condition_approve(lambda: self.__wait(timeout)
                                               .until_not(EC.text_to_be_present_in_element(identify_locator, text)))

    def alert_is_present(self, timeout=5):
        return self.__is_the_condition_approve(lambda: self.__wait(timeout).until(EC.alert_is_present()))

    def alert_is_not_present(self, timeout=5):
        return self.__is_the_condition_approve(lambda: self.__wait(timeout).until_not(EC.alert_is_present()))

    def __is_the_condition_approve(self, condition):
        try:
            condition()
            return True
        except:
            Logger.log.debug(f'The locator {self.identify_locator} has returned False')
            return False
