import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # headless=True means no GUI
        page = await browser.new_page()
        await page.goto("https://google.com")
        await page.fill("//textarea[@id='APjFqb']", "Avi")
        await page.screenshot(path="example.png")  # takes a screenshot
        await browser.close()

asyncio.run(run())
