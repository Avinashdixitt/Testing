# pages/login_page.py

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.login_button = page.locator('button[onclick="logIn()"]')
        self.welcome_text = page.locator("#nameofuser")

    async def open_login_modal(self):
        await self.page.click("#login2")
        await self.page.wait_for_selector("#logInModal", state="visible")

    async def login(self, username, password):
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.login_button.click()

    async def is_login_successful(self):
        return await self.welcome_text.text_content()
