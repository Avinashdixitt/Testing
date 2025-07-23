import asyncio
from playwright.async_api import async_playwright, expect

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://stage.grip-research.org/catalogue")
        await expect().to_be_visible()


        # Open login modal
        await page.click("#login2")
        await page.wait_for_selector("#logInModal", state="visible")

        # Locators
        username_input = page.locator("#loginusername")
        password_input = page.locator("#loginpassword")
        login_button = page.locator('button[onclick="logIn()"]')
        welcome_text = page.locator("#nameofuser")

        # Actions
        await username_input.fill("aviiiiiviviviviivivi")
        await password_input.fill("123")
        await login_button.click()

        # Assertion - Check welcome message
        await expect(welcome_text).to_be_visible()
        await expect(welcome_text).to_contain_text("Welcome")

        print("✅ Login test passed.")

        await page.wait_for_timeout(3000)
        await browser.close()

asyncio.run(run())
