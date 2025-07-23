class BasePage:
    def __init__(self, page):
        self.page = page

    def click_element(self, selector):
        self.page.click(selector)