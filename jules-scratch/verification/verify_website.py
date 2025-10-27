from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Home page
        page.goto(f'file://{os.getcwd()}/index.html')
        page.screenshot(path='jules-scratch/verification/home.png')

        # About page
        page.goto(f'file://{os.getcwd()}/pages/about.html')
        page.screenshot(path='jules-scratch/verification/about.png')

        # Free trial page
        page.goto(f'file://{os.getcwd()}/pages/free-trial.html')
        page.screenshot(path='jules-scratch/verification/free-trial.png')

        # Contact page
        page.goto(f'file://{os.getcwd()}/pages/contact.html')
        page.screenshot(path='jules-scratch/verification/contact.png')

        browser.close()

run()