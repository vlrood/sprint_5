import settings
from locators import PlaceLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import PlaceServiceTestData


class TestLoginButton:
    def test_button_login_to_driver_has_entered(self, driver):
        login = driver.find_element(*PlaceLocators.BUTTON_LOGIN_TO)
        login.click()
        email = driver.find_element(*PlaceLocators.LOGIN_EMAIL_INPUT)
        email.send_keys(PlaceServiceTestData.AUTH_EMAIL)
        password = driver.find_element(*PlaceLocators.LOGIN_PASSWORD_INPUT)
        password.send_keys(PlaceServiceTestData.AUTH_PASSWORD)
        button_login_to = driver.find_element(*PlaceLocators.LOGIN_SUBMIT)
        button_login_to.click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                PlaceLocators.TEXT_ASSEMBLE_BURGER
            )
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_button_registration_driver_has_entered(self, driver):
        driver.get(settings.URL + 'register')
        registration = driver.find_element(*PlaceLocators.REGISTRATION_ENTER)
        registration.click()
        email = driver.find_element(*PlaceLocators.LOGIN_EMAIL_INPUT)
        email.send_keys(PlaceServiceTestData.AUTH_EMAIL)
        password = driver.find_element(*PlaceLocators.LOGIN_PASSWORD_INPUT)
        password.send_keys(PlaceServiceTestData.AUTH_PASSWORD)
        button_login_to = driver.find_element(*PlaceLocators.LOGIN_SUBMIT)
        button_login_to.click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                PlaceLocators.TEXT_ASSEMBLE_BURGER
            )
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_recovery_password_driver_has_entered(self, driver):
        driver.get(settings.URL + 'forgot-password')
        recovery_password_enter = driver.find_element(*PlaceLocators.FORGOT_PASSWORD_ENTER)
        recovery_password_enter.click()
        email = driver.find_element(*PlaceLocators.LOGIN_EMAIL_INPUT)
        email.send_keys(PlaceServiceTestData.AUTH_EMAIL)
        password = driver.find_element(*PlaceLocators.LOGIN_PASSWORD_INPUT)
        password.send_keys(PlaceServiceTestData.AUTH_PASSWORD)
        button_login_to = driver.find_element(*PlaceLocators.LOGIN_SUBMIT)
        button_login_to.click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                PlaceLocators.TEXT_ASSEMBLE_BURGER
            )
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_personal_account_driver_has_entered(self, driver):
        personal_account = driver.find_element(*PlaceLocators.BUTTON_PERSONAL_ACCOUNT)
        personal_account.click()
        email = driver.find_element(*PlaceLocators.LOGIN_EMAIL_INPUT)
        email.send_keys(PlaceServiceTestData.AUTH_EMAIL)
        password = driver.find_element(*PlaceLocators.LOGIN_PASSWORD_INPUT)
        password.send_keys(PlaceServiceTestData.AUTH_PASSWORD)
        button_login_to = driver.find_element(*PlaceLocators.LOGIN_SUBMIT)
        button_login_to.click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                PlaceLocators.TEXT_ASSEMBLE_BURGER
            )
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
