import pytest
from selenium import webdriver
import settings


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)
    return chrome_driver
