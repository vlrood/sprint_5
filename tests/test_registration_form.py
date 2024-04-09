import random
from faker import Faker
import settings
from locators import PlaceLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFormRegistration:
    def test_registration_driver_should_be_registered(self, driver):
        driver.get(settings.URL + 'register')
        fake = Faker()
        name = driver.find_element(*PlaceLocators.FIELD_NAME)
        name.send_keys(fake.name())
        email = driver.find_element(*PlaceLocators.FIELD_EMAIL)
        email.send_keys(f'{fake.first_name()}_{fake.last_name()}_7_{random.randint(100, 999)}@yandex.ru')
        password = driver.find_element(*PlaceLocators.FIELD_PASSWORD)
        password.send_keys(f'{random.randint(100000, 999999)}')
        register_button = driver.find_element(*PlaceLocators.BUTTON_REGISTER)
        register_button.click()
        WebDriverWait(driver, 8).until(
            expected_conditions.element_to_be_clickable(
                PlaceLocators.LOGIN_SUBMIT
            )
        )
        assert '/login' in driver.current_url

    def test_error_password_driver_is_displayed(self, driver):
        driver.get(settings.URL + 'register')
        name = driver.find_element(*PlaceLocators.FIELD_NAME)
        name.send_keys('Sergey')
        email = driver.find_element(*PlaceLocators.FIELD_EMAIL)
        email.send_keys('Sergey_Sery_9_156@yandex.ru')
        password = driver.find_element(*PlaceLocators.FIELD_PASSWORD)
        password.send_keys(f'{random.randint(1, 99999)}')
        register_button = driver.find_element(*PlaceLocators.BUTTON_REGISTER)
        register_button.click()
        assert driver.find_element(*PlaceLocators.PASSWORD_ERROR).is_displayed(), 'Password error does not exist'
        