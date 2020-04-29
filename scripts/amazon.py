import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from libs.base import get_webdriver
from sites.amazon.page import Amazon


def main():
    driver_name = "firefox"

    driver = get_webdriver(driver_name=driver_name)
    browser = Amazon(driver=driver)
    browser.get_homepage()

    browser.search_for("raspberry pi")


if __name__ == "__main__":
    main()
