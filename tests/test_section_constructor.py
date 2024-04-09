import settings
from locators import PlaceLocators


class TestSectionConstructor:
    def test_transition_to_sauces_driver_transferred(self, driver):
        sauces = driver.find_element(*PlaceLocators.SECTION_SAUCES)
        nonactive_sauces = sauces.get_attribute('class')
        sauces.click()
        active_sauces = sauces.get_attribute('class')
        assert nonactive_sauces != active_sauces

    def test_transition_to_bun_driver_transferred(self, driver):
        filling = driver.find_element(*PlaceLocators.SECTION_FILLING)
        filling.click()
        bun = driver.find_element(*PlaceLocators.SECTION_BUN)
        nonactive_bun = bun.get_attribute('class')
        bun.click()
        active_bun = bun.get_attribute('class')
        assert nonactive_bun != active_bun

    def test_transition_to_filling_driver_transferred(self, driver):
        filling = driver.find_element(*PlaceLocators.SECTION_FILLING)
        nonactive_filling = filling.get_attribute('class')
        filling.click()
        active_filing = filling.get_attribute('class')
        assert nonactive_filling != active_filing
