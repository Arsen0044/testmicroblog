import allure
from Logs.Logger import Logger


@allure.suite("Microblog tests")
@allure.sub_suite("Test Microblog")
class TestMicroblog:

    @allure.title("Add new post to blog")
    @allure.description("Login to account, add new post, verify post added")
    def test_add_new_post(self, get_dashboard_with_login_class):
        message = "TestPost"
        with allure.step("Login in system"):
            Logger.log.info("Do login")
            dashboard = get_dashboard_with_login_class

        with allure.step("Add new post to blog"):
            Logger.log.info("Add new post")
            dashboard.add_new_post(message)

        with allure.step("Verify new post added"):
            Logger.log.info("Verify new post added")
            dashboard.check_text_presence_in_page(message)
