import time

from selenium.webdriver import ActionChains, Chrome
from dns_parser.categories import categories
from loguru import logger
from selenium.webdriver.common.alert import Alert
from selenium_stealth import stealth

from dns_parser.driver_storage import DriverStorage

def test(driver: Chrome):
    url = 'https://antcpt.com/score_detector'

    driver.get(url)
    time.sleep(10)
    # alert = driver.switch_to.alert  # or Alert(driver)
    # alert.accept()          
    time.sleep(5)       
    actions = ActionChains(driver) 
    actions.move_by_offset(50, 20).perform() 
    actions.move_by_offset(50, 50).perform() 
    driver.get_screenshot_as_file("screenshot.png")

def main():
    logger.info("Creating chrome driver")
    DriverStorage()

    driver = DriverStorage.get_driver()
    # driver.get("https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html")
    # time.sleep(10)
    # driver.get_screenshot_as_file("screenshot.png")
    # driver = 
    categories.Parser()
    # test(driver=driver)
    try:
        driver.quit()
    except OSError:
        pass

if __name__ == '__main__':
    main()