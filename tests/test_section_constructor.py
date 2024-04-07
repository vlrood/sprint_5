import settings
from locators import PlaceLocators


class TestSectionConstructor:
    def test_transition_to_sauces_driver_transferred(self, driver):
        sauces = driver.find_element(*PlaceLocators.SECTION_SAUCES)
        sauces.click()
        list_sauces = driver.find_element(*PlaceLocators.LIST_SAUCES)
        assert list_sauces.is_displayed()
        driver.quit()

    def test_transition_to_bun_driver_transferred(self, driver):
        filling = driver.find_element(*PlaceLocators.SECTION_FILLING)
        filling.click()
        bun = driver.find_element(*PlaceLocators.SECTION_BUN)
        bun.click()
        list_bun = driver.find_element(*PlaceLocators.LIST_BUN)
        assert list_bun.is_displayed()
        driver.quit()

    def test_transition_to_filling_driver_transferred(self, driver):
        filling = driver.find_element(*PlaceLocators.SECTION_FILLING)
        filling.click()
        list_filling = driver.find_element(*PlaceLocators.LIST_FILLING)
        assert list_filling.is_displayed()
        driver.quit()
