from selenium.webdriver.common.by import By


class LoginPageLocator:

    username_field = (By.XPATH, '//*[@id="username"]')
    password_field = (By.XPATH, '//*[@id="password"]')
    submit_button = (By.XPATH, '//*[@id="submit"]')
