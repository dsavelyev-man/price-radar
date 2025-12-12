from time import sleep
import time
from selenium.webdriver import ChromeOptions, DesiredCapabilities
from selenium_stealth import stealth
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from loguru import logger
class DriverStorage:
    __driver = None

    def __init__(self) -> None:
        if DriverStorage.__driver == None:
                options = ChromeOptions()
                options.add_argument('--blink-settings=imagesEnabled=false')
                options.add_argument("--window-size=1920,1080")
                options.add_argument('--allow-running-insecure-content')
                ua = UserAgent(browsers=["Chrome"])
                logger.info(ua["Chrome"])
                options.add_argument("user-agent=" + ua["Chrome"])

                options.page_load_strategy = 'none'
                
                capa = DesiredCapabilities.CHROME
                capa["pageLoadStrategy"] = "none"

                driver = uc.Chrome(options=options, desired_capabilities=capa)
                stealth(driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    user_agent=ua["Chrome"]
                )
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