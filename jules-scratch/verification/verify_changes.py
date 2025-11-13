from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    page.goto("file:///app/pages/contact.html")
    page.screenshot(path="/app/jules-scratch/verification/contact.png")

    page.goto("file:///app/pages/about.html")
    page.screenshot(path="/app/jules-scratch/verification/about.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
