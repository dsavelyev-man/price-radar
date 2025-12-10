from time import sleep
import time
from selenium.webdriver import ChromeOptions, DesiredCapabilities
import undetected_chromedriver as uc


class DriverStorage:
    __driver = None

    def __init__(self) -> None:
        if DriverStorage.__driver == None:
                options = ChromeOptions()
                options.add_argument('--blink-settings=imagesEnabled=false')
                options.page_load_strategy = 'none'
                
                capa = DesiredCapabilities.CHROME
                capa["pageLoadStrategy"] = "none"

                driver = uc.Chrome(options=options, desired_capabilities=capa)

                DriverStorage.__driver = driver
    
    @staticmethod
    def get_driver():
        return DriverStorage.__driver

    @staticmethod
    def page_is_loaded():
        driver = DriverStorage.get_driver()
        try:
            driver.find_element(uc.By.ID, "base-header")
        except:
            time.sleep(1)
            DriverStorage.page_is_loaded()            