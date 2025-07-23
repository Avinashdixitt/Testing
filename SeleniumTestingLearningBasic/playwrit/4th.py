import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://www.demoblaze.com/")
        await page.click('//a[@id="login2"]')

        # Fill in username and password
        await page.fill("//input[@id='loginusername']", "aviiiiiviviviviivivi")
        await page.fill("//input[@id='loginpassword']", "123")

        # Click the login button
        await page.click("//button[normalize-space()='Log in']")

        # Wait for inventory page to load and check title
        await page.wait_for_selector("//a[@id='nava']")
        title = await page.inner_text("//a[@id='nava']")

        print("Login successful, page title is:", title)

        await browser.close()

asyncio.run(run())
