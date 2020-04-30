import argparse
from os import path
from time import sleep

from playsound import playsound

from libs.base import get_webdriver
from sites.amazon.page import Amazon


DESCRIPTION = "log into amazon and close the browser"
DRIVER_HELP = "Selects which web browser to use"
EMAIL_HELP = "Amazon email"
PASSWORD_HELP = "Amazon email"
REFRESH_RATE = "Page refresh rate per seconds"


def main():
    # TODO: Add Browser choice and set default browser to firefox
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

    args = parser.parse_args()

    driver_name = "firefox"

    driver = get_webdriver(driver_name=driver_name)
    browser = Amazon(driver=driver, implicit_wait=10)
    browser.get_homepage()

    browser.login(email=args.email, password=args.password)

    # Experimental
    browser.click_checkout_cart()

    browser.click_amazon_fresh_checkout_button()

    browser.click_on_proceed_to_checkout_button()

    sleep(5)

    any_slots = browser.any_available_slots()
    while not any_slots:

        # TODO -- Add refresh rate to cmd args
        sleep(args.refresh)

        browser.page_refresh()

        # TODO: look into waiting properly
        sleep(4)

        # Need to wait till slots has fully rendered
        any_slots = browser.any_available_slots()

        # TODO: consider adding verbose output
        print(any_slots)

    # TODO: add the sound file to cmd args
    sound_file_path = path.join("sound_files", "open_slot.mp3")
    playsound(sound_file_path)

    # TODO: remove before committing to Master
    browser.quit()


if __name__ == "__main__":
    main()
