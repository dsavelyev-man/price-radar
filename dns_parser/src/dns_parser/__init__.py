from dns_parser.categories import categories
from loguru import logger

from dns_parser.driver_storage import DriverStorage

def main():
    logger.info("Creating chrome driver")
    DriverStorage()

    driver = DriverStorage.get_driver()

    categories.Parser()

    try:
        driver.quit()
    except OSError:
        pass

if __name__ == '__main__':
    main()