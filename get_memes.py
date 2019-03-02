from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import requests
import os
from uuid import uuid4

MEME_STORAGE_DIR = "meme_storage"
if not os.path.exists(MEME_STORAGE_DIR):
    os.mkdir(MEME_STORAGE_DIR)


def get_image(url, filename):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(os.path.join(MEME_STORAGE_DIR, filename))


if __name__ == "__main__":

    opts = Options()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.get('https://old.reddit.com/r/adviceanimals')
    # expand memes
    expando_buttons = driver.find_elements(
        By.CSS_SELECTOR, ".expando-button.collapsed")
    for btn in expando_buttons:
        btn.click()

    # for url in meme_urls:
        #get_image(url, '')

    posts = driver.find_elements(By.CSS_SELECTOR, "div.thing")
    memes = list()
    for idx, post in enumerate(posts):
        if 'promoted' not in post.text:
            try:
                url = post.find_element(
                    By.CSS_SELECTOR,
                    ".expando img.preview").get_attribute("src")
                score = post.find_element(
                    By.CSS_SELECTOR, "div.score").get_attribute("title")
                get_image(url, f'{score}-{uuid4().hex}.gif')
            except NoSuchElementException:
                pass
