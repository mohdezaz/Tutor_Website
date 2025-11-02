from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    page.goto("file:///app/index.html")
    page.screenshot(path="/app/jules-scratch/verification/index.png")

    page.goto("file:///app/pages/contact.html")
    page.screenshot(path="/app/jules-scratch/verification/contact.png")

    page.goto("file:///app/pages/free-trial.html")
    page.screenshot(path="/app/jules-scratch/verification/free-trial.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
