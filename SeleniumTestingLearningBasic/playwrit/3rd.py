import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://www.saucedemo.com/")

        # Fill in username and password
        await page.fill('input[data-test="username"]', "standard_user")
        await page.fill('input[data-test="password"]', "secret_sauce")

        # Click the login button
        await page.click('input[data-test="login-button"]')

        # Wait for inventory page to load and check title
        await page.wait_for_selector('.title')
        title = await page.inner_text('.title')

        print("Login successful, page title is:", title)

        await browser.close()

asyncio.run(run())
