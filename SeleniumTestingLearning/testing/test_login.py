# test_login.py
from playwright.sync_api import sync_playwright
from LoginPage import LoginPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/login")

    login_page = LoginPage(page)
    login_page.login("avinash", "123456")
