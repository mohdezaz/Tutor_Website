
import os
from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        repo_path = os.path.abspath('.')

        # Homepage
        page.goto(f'file://{repo_path}/index.html')
        expect(page.locator(".hero-image")).to_be_visible()
        page.screenshot(path='jules-scratch/verification/homepage.png')

        # About page
        page.goto(f'file://{repo_path}/pages/about.html')
        expect(page.locator(".page-image")).to_be_visible()
        page.screenshot(path='jules-scratch/verification/about.png')

        # Free Trial page
        page.goto(f'file://{repo_path}/pages/free-trial.html')
        expect(page.locator(".page-image")).to_be_visible()
        page.screenshot(path='jules-scratch/verification/free-trial.png')

        # Contact page
        page.goto(f'file://{repo_path}/pages/contact.html')
        expect(page.locator(".page-image")).to_be_visible()
        page.screenshot(path='jules-scratch/verification/contact.png')

        browser.close()

if __name__ == '__main__':
    run()
