from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from locators import PlaceLocators
from data import PlaceServiceTestData


class TestGoToPersonalAccount:
    def test_personal_account_driver_transferred(self, driver):
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
            expected_conditions.element_to_be_clickable(
                PlaceLocators.BUTTON_EXIT
            )
        )
        assert '/profile' in driver.current_url
