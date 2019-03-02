from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import requests


def get_image(url, filename):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


if __name__ == "__main__":

    opts = Options()
    driver = webdriver.Firefox(firefox_options=opts)
    driver.get('https://old.reddit.com/r/adviceanimals')
    expando_buttons = driver.find_elements(
        By.CSS_SELECTOR, ".expando-button.collapsed")
    for btn in expando_buttons:
        btn.click()
    memes = driver.find_elements(By.CSS_SELECTOR, ".expando img.preview")
    meme_urls = [meme.get_attribute('src') for meme in memes]
    for url in meme_urls:
        get_image(url, '')
