from time import sleep
from selenium import webdriver

browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

browser.get("https://www.instagram.com/")

sleep(3)

acceptcookies = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
acceptcookies.click()


sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

userInfoFile = open("userinfo.txt", "r")
username = userInfoFile.readline()
password = userInfoFile.readline()

print(username)
print(password)

username_input.send_keys(username)
password_input.send_keys(password)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(6)

notifications = browser.find_element_by_css_selector('button.aOOlW:nth-child(2)')
notifications.click()
print("clicked")

sleep(7)
browser.close()