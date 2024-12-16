from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = 'https://tutorialsninja.com/demo/'


def set_driver_config(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Enables new headless mode
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.get(URL)

    return context.driver


def quit_driver(context):
    context.driver.quit()
