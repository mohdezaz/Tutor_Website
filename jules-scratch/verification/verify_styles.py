from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Base path for HTML files
        base_path = os.path.abspath('.')

        # Pages to screenshot
        pages = {
            "homepage": "index.html",
            "about": "pages/about.html",
            "free-trial": "pages/free-trial.html",
            "contact": "pages/contact.html"
        }

        for name, path in pages.items():
            full_path = f'file://{os.path.join(base_path, path)}'
            print(f"Navigating to {full_path}")
            page.goto(full_path)
            page.screenshot(path=f"jules-scratch/verification/{name}-styled.png")
            print(f"Screenshot saved for {name}")

        browser.close()

if __name__ == "__main__":
    run()
