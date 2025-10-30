import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Navigate to the local index.html file
        file_path = os.path.abspath('index.html')
        await page.goto(f'file://{file_path}')

        # Wait for the page to load completely
        await page.wait_for_load_state('networkidle')

        # Locate and click each FAQ question to expand it
        faq_questions = await page.query_selector_all('.faq-question')
        for question in faq_questions:
            await question.click()
            # Add a small delay to allow the animation to complete
            await page.wait_for_timeout(500)

        # Take a full-page screenshot to verify the expanded FAQ section
        screenshot_path = 'jules-scratch/verification/homepage-faq-open.png'
        await page.screenshot(path=screenshot_path, full_page=True)

        await browser.close()
        print(f"Screenshot saved to {screenshot_path}")

if __name__ == '__main__':
    asyncio.run(main())
