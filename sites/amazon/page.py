from typing import List

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

    def get_homepage(self) -> None:
        """
        Goes to Amazon's homepage
        :return: None
        """
        self.driver.get("https://www.amazon.com/")

    def search_for(self, text: str) -> None:
        """
        Conducts a search using Amazon's search bar

        :param text: str
        :return: None
        """
        text_box = self.find_element(by=self.SearchBox.by, value=self.SearchBox.value)

        text_box.send_keys(text)

        submit_search_icon = self.find_element(
            by=self.SubmitSearchIcon.by, value=self.SubmitSearchIcon.value
        )

        submit_search_icon.click()

    def get_search_results(self) -> List[RemoteWebElement]:
        """
        Returns a list of WebElements representing the the Amazon search result items

        :return: list[RemoteWebElement]
        """
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

    @staticmethod
    def click_search_result(search_result: RemoteWebElement) -> None:
        """
        Clicks on the passed in Amazon search result

        :param search_result: RemoteWebElement
        :return: None
        """
        _ = search_result.location_once_scrolled_into_view
        search_result.find_element_by_css_selector("img").click()

    def login(self, email: str, password: str) -> None:
        """
        Log into the Amazon site

        :param email: str
        :param password: str
        :return: None
        """
        sign_in_link = self.driver.find_element(
            by=self.SignInLink.by, value=self.SignInLink.value
        )

        sign_in_link.click()

        self.wait_for_element_to_be_present(self.SignInFormEmail)

        form_email = self.driver.find_element(
            by=self.SignInFormEmail.by, value=self.SignInFormEmail.value
        )

        form_email.send_keys(email)

        submit_button = self.driver.find_element(
            by=self.SignInFormSubmit.by, value=self.SignInFormSubmit.value
        )

        submit_button.click()

        self.wait_for_element_to_be_present(self.SignInFormPassword)

        form_password = self.driver.find_element(
            by=self.SignInFormPassword.by, value=self.SignInFormPassword.value
        )

        form_password.send_keys(password)

        submit_button = self.driver.find_element(
            by=self.SignInFormSubmit.by, value=self.SignInFormSubmit.value
        )

        submit_button.click()

    def click_fresh_nav_link(self: None):
        """
        Click on the Amazon Fresh link in the nav bar

        :return: None
        """
        self.wait_for_element_to_be_present(self.NavLinkFresh)

        nav_fresh_link = self.driver.find_element(
            by=self.NavLinkFresh.by, value=self.NavLinkFresh.value
        )

        nav_fresh_link.click()

    def click_checkout_cart(self) -> None:
        """
        Click on the checkout cart icon

        :return: None
        """
        self.wait_for_element_to_be_present(self.CheckoutCart)

        cart = self.driver.find_element(
            by=self.CheckoutCart.by, value=self.CheckoutCart.value
        )

        cart.click()

    def click_amazon_fresh_checkout_button(self) -> None:
        """
        Click the checkout button on the Amazon Fresh checkout page

        :return: None
        """
        self.wait_for_element_to_be_present(self.FreshCheckoutButton)

        button = self.driver.find_element(
            by=self.FreshCheckoutButton.by, value=self.FreshCheckoutButton.value
        )

        button.click()

    def click_on_proceed_to_checkout_button(self) -> None:
        """
        Click on the Proceed to Checkout button

        :return: None
        """
        self.wait_for_element_to_be_present(self.ProceedToCheckoutButton)

        button = self.driver.find_element(
            by=self.ProceedToCheckoutButton.by, value=self.ProceedToCheckoutButton.value
        )

        button.click()

    def get_fresh_time_slots(self) -> List[RemoteWebElement]:
        """
        Return a list of slot WebElements

        :return: list[RemoteWebElement]
        """
        self.wait_for_element_to_be_present(self.FreshTimeSlots)

        slots = self.driver.find_elements(
            by=self.FreshTimeSlots.by, value=self.FreshTimeSlots.value
        )

        return slots

    def any_available_slots(self) -> bool:
        """
        Checks to see if any slots are available

        :return: bool
        """
        result = False
        slots = self.get_fresh_time_slots()

        # Scroll down to bring the slots in view
        if slots:
            self.scroll_to_element(slots[0])

        for slot in slots:
            if "Not available" not in slot.text:
                result = True

        return result
