
import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the HTML file
        # The HTML file is in the root directory
        html_file_path = os.path.abspath('index.html')

        # Go to the local HTML file
        page.goto(f'file://{html_file_path}')

        # Take a screenshot
        page.screenshot(path='jules-scratch/verification/homepage-philosophy.png')

        browser.close()

if __name__ == "__main__":
    run()
