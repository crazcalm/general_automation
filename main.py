from libs.base import get_webdriver


def main():
    driver_name = "firefox"

    # This will not work on my linux box because my
    # version of chrome is too new...
    # driver_name = "chrome"

    browser = get_webdriver(driver_name=driver_name)
    browser.get("http://seleniumhq.org/")

    browser.implicitly_wait(10)
    browser.find_element_by_name()


if __name__ == "__main__":
    main()
