from time import sleep
from selenium import webdriver
import os

configFilePath = "config.ini"

def validateConfigFile(filePath):
    if os.path.isfile(filePath):
        if not (os.stat(filePath).st_size == 0):
            return True
        else: 
            return False
    else:
        return False

def getUserInfo():
    usern = ""
    passw = ""
    if validateConfigFile(configFilePath): 
        userInfoFile = open(configFilePath, "r")
        lines = userInfoFile.readlines()
        for line in lines:
            if ("user" in line):
                usern = line.split('=')[1]
                print(usern)
            if ("password" in line):
                passw = line.split('=')[1]
                print(passw)

        print("Credentials import successful.")
        print("Logging in using credentials for user:" + usern)
    else:
        print("No user info found, please enter credentials to create new configuration file.")
        print("username: ", end ='')
        usern = str(input()) 
        print("Enter password: ", end = '')
        passw = str(input())
        userInfoFile = open((configFilePath),"w+")
        userInfoFile.writelines(["username=" + usern, "\n","password="+ passw])
        userInfoFile.close()
    return [usern, passw]


userInfo = getUserInfo()
username = userInfo[0]
password = userInfo[1]

browser = webdriver.Firefox(executable_path="./drivers/geckodriver")


browser.get("https://www.instagram.com/")

sleep(3)

acceptcookies = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
acceptcookies.click()


sleep(3)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

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

    