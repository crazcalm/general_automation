import argparse
from os import path
from time import sleep

from playsound import playsound

from libs.base import get_webdriver
from sites.amazon.page import Amazon

DESCRIPTION = "log into amazon and close the browser"


def main():
    # TODO: Add Browser choice and set default browser to firefox
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("email", type=str, help="Amazon email")
    parser.add_argument("password", type=str, help="Amazon password")

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
        sleep(40)

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
