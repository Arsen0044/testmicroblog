from selenium.webdriver.common.by import By


class DashboardPageLocator:

    post_input_field = (By.XPATH, '//*[@name="input_value"]')
    submit_button = (By.XPATH, '//button[@type="submit"]')
