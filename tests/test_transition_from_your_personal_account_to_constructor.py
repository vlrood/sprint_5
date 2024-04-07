from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
import pytest
from locators import PlaceLocators


class TestTransitionFromAccountToConstructor:
    @pytest.mark.parametrize('button_locator', [
        PlaceLocators.CONSTRUCTOR,
        PlaceLocators.HEADER_LOGO
    ])
    def test_transition_personal_account_to_button_locator_driver_transferred(self, driver, button_locator):
        driver.get(settings.URL + 'login')
        email = driver.find_element(*PlaceLocators.LOGIN_EMAIL_INPUT)
        email.send_keys('Valeria_Lel_7_123@yandex.ru')
        password = driver.find_element(*PlaceLocators.LOGIN_PASSWORD_INPUT)
        password.send_keys('7654321')
        login_to = driver.find_element(*PlaceLocators.LOGIN_SUBMIT)
        login_to.click()
        personal_account = driver.find_element(*PlaceLocators.BUTTON_PERSONAL_ACCOUNT)
        personal_account.click()
        button = driver.find_element(*button_locator)
        button.click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                PlaceLocators.TEXT_ASSEMBLE_BURGER
            )
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
