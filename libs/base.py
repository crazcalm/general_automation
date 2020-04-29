from collections import namedtuple

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


Locator = namedtuple("Locator", "by value")


class BasePage:
    """
    Base class for all page objects
    """

    def __init__(self, driver, implicit_wait=0):
        self.driver = driver
        self.driver.implicitly_wait(0)

    def get_title(self) -> str:
        return self.driver.title

    def get_driver_name(self) -> str:
        return self.driver.name

    def quit(self) -> None:
        self.driver.quit()

    def get_page_source(self) -> str:
        return self.driver.page_source

    def page_refresh(self):
        self.driver.refresh()

    def get_homepage(self):
        raise NotImplementedError

    def find_element(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by=by, value=value)


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
