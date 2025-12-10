import array
import json
import time
from loguru import logger
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import By, Chrome
from dns_parser.driver_storage import DriverStorage
from dns_parser.helpers import url


class Category():
    children = None

    def __init__(self, name: str, href: str, parent_category: str=None) -> None:
        self.name = name
        self.href = href
        if(parent_category):
            self.parent_category = parent_category
    
    def set_children(self, children: list):
        self.children = children
    

class Parser: 
    excluded_links = ["configurator/", "configurator-kitchen/", "user-pc/"]
    counter = 0

    def __init__(self) -> None:
        logger.info("Collectiong categories")
        driver = DriverStorage.get_driver()
        driver.get(url("catalog"))
        root_categories = self.__get_categories()
        self.get_recursive_categories(root_categories)
        
    def get_recursive_categories(self, categories: list[Category]):
        driver = DriverStorage.get_driver()
        for category in categories:
            driver.get(category.href)
            child_categories = self.__get_categories(parent_category=category)
            category.set_children(child_categories)

    def __get_categories(self, parent_category: str=None):
        driver = DriverStorage.get_driver()

        # DriverStorage.page_is_loaded()
        wait = WebDriverWait(driver, 10)

        try:
            wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "subcategory__item")))
        except:
            try:
                wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "subcategory__childs-item")))
            except:
                return []
            

        driver.execute_script("window.stop();")

        categories = []
        links = driver.find_elements(By.CLASS_NAME, 'subcategory__childs-item')
        if len(links) == 0:
            links = driver.find_elements(By.CLASS_NAME, 'subcategory__item')

            for link in links:
                href = link.get_attribute("href")
                text = None

                try:
                    title_el = link.find_element(By.CLASS_NAME, "subcategory__title")
                    text = title_el.text
                except:
                    pass

                if any(href.endswith(excluded_link) for excluded_link in Parser.excluded_links):
                    continue

                categories.append(Category(text, href, parent_category))
        else: 
            for link in links:
                href = link.get_attribute("href")
                text = link.get_attribute("innerHTML")

                if any(href.endswith(excluded_link) for excluded_link in Parser.excluded_links):
                    continue
                categories.append(Category(text, href, parent_category))

        # TODO удалить
        with open("test-" + str(self.counter) + ".json", "w", encoding="utf-8") as f:
            json.dump(categories, f, ensure_ascii=False, indent=4, default=vars)

        self.counter += 1
        logger.info(f"Collected: " + str(len(categories)) + " categories")



        return categories
