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
import sys

MEME_STORAGE_DIR = "meme_storage"
if not os.path.exists(MEME_STORAGE_DIR):
    os.mkdir(MEME_STORAGE_DIR)


class MemeGrabber():
    def __init__(
            self,
            start_url="https://old.reddit.com/r/adviceanimals/new/?limit=100"):
        opts = Options()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)
        self.meme_count = 0
        self.driver.get(start_url)

    def get_memes(self):
        self._expand_memes()
        self._save_images()

    def _expand_memes(self):
        expando_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, ".expando-button.collapsed")
        for btn in expando_buttons:
            btn.click()

    def _save_images(self):
        """Saves memes as GIFs in the MEME_STORAGE_DIR"""
        posts = self.driver.find_elements(By.CSS_SELECTOR, "div.thing")
        memes = list()
        for idx, post in enumerate(posts):
            if 'promoted' not in post.text:
                try:
                    url = post.find_element(
                        By.CSS_SELECTOR,
                        ".expando img.preview").get_attribute("src")
                    score = post.find_element(
                        By.CSS_SELECTOR, "div.score").get_attribute("title")
                    if int(score) < 20:
                        print(
                            "Rejected Meme:%7s Upvotes" %
                            score if len(score) > 0 else 0,
                            file=sys.stderr)
                        raise ValueError  # only the best memes allowed
                    fname = f'{score}-{uuid4().hex}.tiff'
                    get_image(url, fname)
                    print(
                        "Got      Meme:%7s Upvotes, Filename: %42s" %
                        (score, fname), file=sys.stderr)
                    self.meme_count += 1
                except(NoSuchElementException, ValueError):
                    pass

    def next_page(self):
        """goes to the next page"""
        next_btn = self.driver.find_element(
            By.CSS_SELECTOR, "span.next-button > a")
        url = next_btn.get_attribute('href')
        print(f"Next Page! {url}", file=sys.stderr)
        next_btn.click()
        return url


def get_image(url, filename):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(os.path.join(MEME_STORAGE_DIR, filename))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        mg = MemeGrabber(start_url=sys.argv[2])
    elif len(sys.argv) == 2:
        total = int(sys.argv[1])
        mg = MemeGrabber()
    else:
        total = 100
        mg = MemeGrabber()

    while(mg.meme_count < total):
        mg.get_memes()
        mg.next_page()
