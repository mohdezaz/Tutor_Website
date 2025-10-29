import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('file://' + os.path.abspath('index.html'))
        page.screenshot(path='jules-scratch/verification/homepage-we-provide.png')
        browser.close()

run()
