from libs.base import BasePage
from libs.base import Locator

from selenium.webdriver.common.by import By


class Amazon(BasePage):
    SearchBox = Locator(By.CSS_SELECTOR, ".nav-search-field input[id$='textbox']")
    SubmitSearchIcon = Locator(By.CSS_SELECTOR, ".nav-search-submit")

    def get_homepage(self):
        self.driver.get("https://www.amazon.com/")

    def search_for(self, text: str):
        text_box = self.find_element(by=self.SearchBox.by, value=self.SearchBox.value)

        text_box.send_keys(text)

        submit_search_icon = self.find_element(
            by=self.SubmitSearchIcon.by, value=self.SubmitSearchIcon.value
        )

        submit_search_icon.click()
