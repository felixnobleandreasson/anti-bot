from time import sleep
from selenium import webdriver
from homePage import HomePage
from feedPage import FeedPage


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