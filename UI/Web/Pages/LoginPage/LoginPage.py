from selenium import webdriver
from UI.BasePage import BasePage
from UI.Web.Utilities.read_config import Constants
from UI.Web.Pages.DashboardPage.DashboardPage import DashboardPage
from UI.Web.Pages.LoginPage.LoginPageLocators import LoginPageLocator


class LoginPage(BasePage):

    def __init__(self, driver: webdriver, navigate: bool = True):
        super().__init__(driver)
        if navigate:
            self.navigate(Constants.logout_url)
            self.wait_for_page_load()
        self.locators = LoginPageLocator()

    def do_login(self, username, password):
        self.send_keys(self.locators.username_field, username)
        self.send_keys(self.locators.password_field, password)
        self.click_element(self.locators.submit_button)
        self.wait_for_page_load()
        return DashboardPage(self.driver)