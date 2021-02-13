from selenium import webdriver
from feedPage import FeedPage

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.instagram.com/")

    def acceptCookies(self):
        acceptcookies = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
        acceptcookies.click()
    
    def login(self, username, password):
        browser = self.browser
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        return FeedPage(self.browser)