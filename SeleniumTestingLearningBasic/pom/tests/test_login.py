# tests/test_login.py

import asyncio
from playwright.async_api import async_playwright, expect
from pom.pages.login_page import LoginPage

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.demoblaze.com/")

        login_page = LoginPage(page)

        await login_page.open_login_modal()
        await login_page.login("aviiiiiviviviviivivi", "123")

        await expect(login_page.welcome_text).to_be_visible()
        await expect(login_page.welcome_text).to_contain_text("Welcome")

        print("✅ Login passed using Page Object Model.")
        await browser.close()

asyncio.run(run())
