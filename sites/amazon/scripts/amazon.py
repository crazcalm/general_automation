from time import sleep

from libs.base import get_webdriver
from sites.amazon.page import Amazon


def main():
    driver_name = "firefox"

    driver = get_webdriver(driver_name=driver_name)
    browser = Amazon(driver=driver, implicit_wait=10)
    browser.get_homepage()

    browser.search_for("raspberry pi")

    results = browser.get_search_results()

    if not results:
        print("Had to use sleep...")
        sleep(4)
        results = browser.get_search_results()

    if len(results) > 5:
        browser.click_search_result(results[5])

    # TODO: remove before committing
    browser.quit()


if __name__ == "__main__":
    main()
