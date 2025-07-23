# locators.py
from selenium.webdriver.common.by import By

search_box = (By.ID, "twotabsearchtextbox")
sign_in_button = (By.ID, "nav-link-accountList")
mobiles_link = (By.LINK_TEXT, "Mobiles")

first_product_xpath = "//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1']//div[@class='a-section a-spacing-none puis-padding-right-small s-title-instructions-style puis-desktop-list-title-instructions-style']"
add_to_cart_xpath = "//input[@id='add-to-cart-button']"
sponsored_product_xpath = "//div[contains(@class, 's-widget-container') and .//span[text()='Sponsored']]//a[contains(@class, 'a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal')]"
wishlist_button_xpath = "//span[@id='wishListMainButton']"
