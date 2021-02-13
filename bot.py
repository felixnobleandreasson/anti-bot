from time import sleep
from selenium import webdriver

class FeedPage:
    def __init__(self, browser):
        self.browser = browser

    def declineNotifications(self):
        notifications = browser.find_element_by_css_selector('button.aOOlW:nth-child(2)')
        notifications.click()



class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.instagram.com/")

    def acceptCookies(self):
        acceptcookies = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
        acceptcookies.click()
    
    def login(self, username, password):
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        return FeedPage(self.browser)


browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
browser.implicitly_wait(5)

home_page = HomePage(browser)
home_page.acceptCookies()

userInfoFile = open("userinfo.txt", "r")
username = userInfoFile.readline()
password = userInfoFile.readline()

#print(username)
#print(password)

feed_page = home_page.login(username, password)
feed_page.declineNotifications()

sleep(5)
browser.close()