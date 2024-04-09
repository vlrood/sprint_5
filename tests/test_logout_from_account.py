from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from locators import PlaceLocators
from data import PlaceServiceTestData


class TestLogoutFromAccount:
    def test_exit_driver_should_come_out(self, driver):
        driver.get(settings.URL + 'login')
        email = driver.find_element(*PlaceLocators.LOGIN_EMAIL_INPUT)
        email.send_keys(PlaceServiceTestData.AUTH_EMAIL)
        password = driver.find_element(*PlaceLocators.LOGIN_PASSWORD_INPUT)
        password.send_keys(PlaceServiceTestData.AUTH_PASSWORD)
        login_to = driver.find_element(*PlaceLocators.LOGIN_SUBMIT)
        login_to.click()
        personal_account = driver.find_element(*PlaceLocators.BUTTON_PERSONAL_ACCOUNT)
        personal_account.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                PlaceLocators.BUTTON_EXIT
            )
        )
        exit_button = driver.find_element(*PlaceLocators.BUTTON_EXIT)
        exit_button.click()
        WebDriverWait(driver, 8).until(
            expected_conditions.element_to_be_clickable(
                PlaceLocators.LOGIN_SUBMIT
            )
        )
        assert '/login' in driver.current_url
