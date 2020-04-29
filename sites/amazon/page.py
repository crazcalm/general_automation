from libs.base import BasePage
from libs.base import Locator

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Amazon(BasePage):
    SearchBox = Locator(By.CSS_SELECTOR, ".nav-search-field input[id$='textbox']")
    SubmitSearchIcon = Locator(By.CSS_SELECTOR, ".nav-search-submit")
    SearchResultsSection = Locator(By.CSS_SELECTOR, ".s-search-results")
    SearchResultsSectionItems = Locator(
        By.CSS_SELECTOR, "[data-cel-widget^='search_result_']"
    )

    def get_homepage(self):
        self.driver.get("https://www.amazon.com/")

    def search_for(self, text: str):
        text_box = self.find_element(by=self.SearchBox.by, value=self.SearchBox.value)

        text_box.send_keys(text)

        submit_search_icon = self.find_element(
            by=self.SubmitSearchIcon.by, value=self.SubmitSearchIcon.value
        )

        submit_search_icon.click()

    def get_search_results(self):
        # Waiting for the page to load
        WebDriverWait(self.driver, 100).until(
            EC.visibility_of_any_elements_located(
                (
                    self.SearchResultsSectionItems.by,
                    self.SearchResultsSectionItems.value,
                )
            )
        )

        search_result_items = self.driver.find_elements(
            by=self.SearchResultsSectionItems.by,
            value=self.SearchResultsSectionItems.value,
        )

        return search_result_items

    def click_search_result(self, search_result: RemoteWebElement):
        search_result.location_once_scrolled_into_view
        search_result.find_element_by_css_selector("img").click()
