import argparse
from time import sleep

from libs.base import get_webdriver
from sites.amazon.page import Amazon


DESCRIPTION = "Amazon automation demo"
DRIVER_HELP = "Selects which web browser to use"


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "--driver",
        "-d",
        choices=["firefox", "chrome"],
        default="firefox",
        help=DRIVER_HELP,
        dest="driver",
    )

    args = parser.parse_args()

    driver = get_webdriver(driver_name=args.driver)
    browser = Amazon(driver=driver, implicit_wait=10)
    browser.get_homepage()

    browser.search_for("raspberry pi")

    results = browser.get_search_results()

    if not results:  # Try again
        sleep(3)
        results = browser.get_search_results()

    if len(results) > 5:
        browser.click_search_result(results[5])

    # Keep the page on screen so that you gan see it
    sleep(3)

    browser.quit()


if __name__ == "__main__":
    main()
