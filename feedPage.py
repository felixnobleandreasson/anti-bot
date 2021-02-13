from selenium import webdriver

class FeedPage:
    def __init__(self, browser):
        self.browser = browser

    def declineNotifications(self):
        notifications = self.browser.find_element_by_css_selector('button.aOOlW:nth-child(2)')
        notifications.click()