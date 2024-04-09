from selenium.webdriver.common.by import By


class PlaceLocators:
    BUTTON_LOGIN_TO = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка «Войти в аккаунт»
    REGISTRATION_ENTER = (By.XPATH, '//a[contains(@href, "login")]')  # кнопка  в форме регистрации
    FORGOT_PASSWORD_ENTER = (By.XPATH, '//a[@class = "Auth_link__1fOlj"]')  # кнопка в форме восстановления пароля
    FIELD_NAME = (By.NAME, 'name')
    FIELD_EMAIL = (By.XPATH, '//fieldset[2]//input[@name="name"]')
    FIELD_PASSWORD = (By.XPATH, '//fieldset[3]//input[@name="Пароль"]')
    BUTTON_REGISTER = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # кнопка зарегистрироваться
    PASSWORD_ERROR = (By.XPATH, '//p[text()="Некорректный пароль"]')
    LOGIN_EMAIL_INPUT = (By.NAME, 'name')
    LOGIN_PASSWORD_INPUT = (By.NAME, 'Пароль')
    LOGIN_SUBMIT = (By.XPATH, './/button[text()="Войти"]')
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]')  # личный аккуант
    BUTTON_EXIT = (By.XPATH, '//button[text()="Выход"]')
    CONSTRUCTOR = (By.XPATH, './/p[text()="Конструктор"]/parent::a')
    HEADER_LOGO = (By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2')  # stellar burger
    SECTION_SAUCES = (By.XPATH, './/span[text()="Соусы"]/parent::div')
    SECTION_BUN = (By.XPATH, './/span[text()="Булки"]/parent::div')
    SECTION_FILLING = (By.XPATH, './/span[text()="Начинки"]/parent::div')
    TEXT_ASSEMBLE_BURGER = (By.XPATH, './/h1[text() ="Соберите бургер"]')
