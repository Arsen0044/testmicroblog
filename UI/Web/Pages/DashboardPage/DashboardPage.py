from selenium import webdriver
from UI.BasePage import BasePage
from UI.Web.Pages.DashboardPage.DashboardPageLocators import DashboardPageLocator


class DashboardPage(BasePage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.locators = DashboardPageLocator()

    def add_new_post(self, message: str) -> None:
        self.fill_in_message_field(message)
        self.click_submit_button()

    def fill_in_message_field(self, message: str) -> None:
        self.presence_of_element_located(self.locators.post_input_field)
        self.send_keys(self.locators.post_input_field, message)

    def click_submit_button(self) -> None:
        self.presence_of_element_located(self.locators.submit_button)
        self.element_to_be_clickable(self.locators.submit_button)
        self.click_element(self.locators.submit_button)
