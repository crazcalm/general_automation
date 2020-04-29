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
    SignInLink = Locator(By.CSS_SELECTOR, "a#nav-link-accountList")
    SignInFormEmail = Locator(By.CSS_SELECTOR, "input#ap_email")
    SignInFormPassword = Locator(By.CSS_SELECTOR, "input#ap_password")
    SignInFormSubmit = Locator(By.CSS_SELECTOR, "input[type='submit']")

    NavLinkFresh = Locator(By.CSS_SELECTOR, "a#nav-link-fresh")
    CheckoutCart = Locator(By.CSS_SELECTOR, "a#nav-cart")

    FreshCheckoutButton = Locator(By.CSS_SELECTOR, "input[name*='ALMCheckout']")
    ProceedToCheckoutButton = Locator(By.CSS_SELECTOR, "a[name='proceedToCheckout']")

    FreshTimeSlots = Locator(By.CSS_SELECTOR, "ul.ss-carousel-items li")

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

    def login(self, email: str, password: str):
        signin_link = self.driver.find_element(
            by=self.SignInLink.by, value=self.SignInLink.value
        )

        # import pdb; pdb.set_trace()

        signin_link.click()

        form_email = self.driver.find_element(
            by=self.SignInFormEmail.by, value=self.SignInFormEmail.value
        )

        form_email.send_keys(email)

        submit_button = self.driver.find_element(
            by=self.SignInFormSubmit.by, value=self.SignInFormSubmit.value
        )

        submit_button.click()

        form_password = self.driver.find_element(
            by=self.SignInFormPassword.by, value=self.SignInFormPassword.value
        )

        form_password.send_keys(password)

        submit_button = self.driver.find_element(
            by=self.SignInFormSubmit.by, value=self.SignInFormSubmit.value
        )

        submit_button.click()

        self.driver

    def click_fresh_nav_link(self):
        nav_fresh_link = self.driver.find_element(
            by=self.NavLinkFresh.by, value=self.NavLinkFresh.value
        )

        nav_fresh_link.click()

    def click_checkout_cart(self):
        cart = self.driver.find_element(
            by=self.CheckoutCart.by, value=self.CheckoutCart.value
        )

        cart.click()

    def click_amazon_fresh_checkout_button(self):
        button = self.driver.find_element(
            by=self.FreshCheckoutButton.by, value=self.FreshCheckoutButton.value
        )

        button.click()

    def click_on_proceed_to_checkout_button(self):
        button = self.driver.find_element(
            by=self.ProceedToCheckoutButton.by, value=self.ProceedToCheckoutButton.value
        )

        button.click()

    def get_fresh_time_slots(self):
        slots = self.driver.find_elements(
            by=self.FreshTimeSlots.by, value=self.FreshTimeSlots.value
        )

        return slots

    def any_available_slots(self):
        result = False
        slots = self.get_fresh_time_slots()
        for slot in slots:
            if "Not available" not in slot.text:
                result = True

        return result
