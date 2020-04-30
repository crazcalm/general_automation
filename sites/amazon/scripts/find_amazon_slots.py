import argparse
from os import path
from time import sleep

from playsound import playsound

from libs.base import get_webdriver
from sites.amazon.page import Amazon


DESCRIPTION = "Logs into the Amazon site and refreshes the Amazon fresh checkout page until it finds an open slot"
DRIVER_HELP = "Selects which web browser to use"
EMAIL_HELP = "Amazon email"
PASSWORD_HELP = "Amazon email"
REFRESH_RATE = "Page refresh rate per seconds"

DEFAULT_SOUND_FILE = path.join("sound_files", "open_slot.mp3")


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
    parser.add_argument("email", type=str, help=EMAIL_HELP)
    parser.add_argument("password", type=str, help=PASSWORD_HELP)
    parser.add_argument(
        "--refresh", "-r", type=int, default=40, help=REFRESH_RATE, dest="refresh"
    )
    parser.add_argument(
        "--sound_file",
        "-s",
        type=str,
        default=DEFAULT_SOUND_FILE,
        dest="sound_file_path",
    )

    args = parser.parse_args()

    driver = get_webdriver(driver_name=args.driver)
    browser = Amazon(driver=driver, implicit_wait=10)
    browser.get_homepage()
    browser.login(email=args.email, password=args.password)

    browser.click_checkout_cart()
    browser.click_amazon_fresh_checkout_button()
    browser.click_on_proceed_to_checkout_button()

    # TODO: Figure out how to properly wait...
    sleep(3)

    any_slots = browser.any_available_slots()
    while not any_slots:

        # Sleep until in need to refresh the page
        sleep(args.refresh)

        browser.page_refresh()

        # TODO: Figure out how to properly wait...
        sleep(3)

        # Need to wait till slots has fully rendered
        any_slots = browser.any_available_slots()

        # TODO: consider adding verbose output
        # TODO: consider adding a timestamp
        print(f"any open slots: {any_slots}")

    playsound(args.sound_file_path)


if __name__ == "__main__":
    main()
