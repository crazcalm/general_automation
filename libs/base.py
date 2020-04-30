from collections import namedtuple
from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Locator = namedtuple("Locator", "by value")


class BasePage:
    """
    Base class for all page objects
    """

    def __init__(self, driver, implicit_wait=0):
        self.driver = driver
        self.driver.implicitly_wait(implicit_wait)

    def get_title(self) -> str:
        """
        Wrapper around webdriver.title

        :return: str
        """
        return self.driver.title

    def get_driver_name(self) -> str:
        """
        Wrapper around webdriver.name

        :return: str
        """
        return self.driver.name

    def quit(self) -> None:
        """
        Wrapper around webdriver.quit()

        :return: None
        """
        self.driver.quit()

    def get_page_source(self) -> str:
        """
        Wrapper around webdriver.page_source

        :return: str
        """
        return self.driver.page_source

    def page_refresh(self):
        """
        Wrapper around webdriver.refresh()

        :return: None
        """
        self.driver.refresh()

    def get_homepage(self):
        """
        Abstract method for get_homepage
        """
        raise NotImplementedError

    def find_element(self, by: str, value: str) -> RemoteWebElement:
        """
        Wrapper around webdriver.find_element

        :param by: str
        :param value: str
        :return: RemoteWebElement
        """
        return self.driver.find_element(by=by, value=value)

    def find_elements(self, by: str, value: str) -> List[RemoteWebElement]:
        """
        Wrapper around webdriver.find_elements

        :param by: str
        :param value: str
        :return: list[RemoteWebElement]
        """
        return self.driver.find_elements(by=by, value=value)

    @staticmethod
    def scroll_to_element(element: RemoteWebElement) -> None:
        """
        Scroll to element

        :param element: RemoteWebElement
        :return: None
        """
        _ = element.location_once_scrolled_into_view

    def wait_for_element_to_be_present(self, locator: Locator, wait_time=50) -> None:
        """
        Waits for the element to be present

        :param locator: Locator
        :param wait_time: int
        :return: None
        """
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator)
        )


def get_webdriver(driver_name: str) -> RemoteWebDriver:
    """
    A factory that returns the webdriver you want.

    :param driver_name: str
    :return: RemoteWebDriver
    """
    mapping = {"chrome": webdriver.Chrome, "firefox": webdriver.Firefox}
    mapping_keys_list = [key for key in mapping.keys()]
    driver_list = ", ".join(mapping_keys_list[:-1])
    driver_list += f", and {mapping_keys_list[-1]}"

    if driver_name not in mapping:
        raise Exception(
            f"The driver you selected ({driver_name}) "
            f"is not in our list of drivers: {driver_list}"
        )

    return mapping[driver_name]()
