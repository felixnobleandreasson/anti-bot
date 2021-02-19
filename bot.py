from time import sleep
from selenium import webdriver
import os

class UserLogin:

    def __init__(self):
        self.configFilePath = "config.ini"
        self.usern = ""
        self.passw = ""

    def validateConfigFile(self, filePath):
        if os.path.isfile(filePath):
            if not (os.stat(filePath).st_size == 0):
                return True
            else:
                return False
        else:
            return False

    def userMissing(self):
        print(
            "No user info found, please enter credentials to create new configuration file.")
        self.createNewUser()

    def createNewUser(self):

        print("Enter username: ", end='')
        self.usern = str(input())
        print("Enter password: ", end='')
        self.passw = str(input())

        userInfoFile = open((self.configFilePath), "w+")
        userInfoFile.writelines(
            ["username=" + self.usern, "\n", "password=" + self.passw])
        userInfoFile.close()
        print("Credentials successfully stored in " + self.configFilePath)

    def changeConfigPath(self, newPath):
        configFilePath = newPath

    def getUserInfo(self):
        
        if self.validateConfigFile(self.configFilePath):
            userInfoFile = open(self.configFilePath, "r")
            lines = userInfoFile.readlines()
            for line in lines:
                if ("user" in line):
                    self.usern = line.split('=')[1]
                if ("password" in line):
                    self.passw = line.split('=')[1]

            if (not (self.passw and self.usern)):
                self.userMissing()
            else:
                print("Credentials import successful.")
                print("Logging in using credentials for user: " + self.usern)
        else:
            self.userMissing()
        return [self.usern, self.passw]


userLogin = UserLogin()
userInfo = userLogin.getUserInfo()
username = userInfo[0]
password = userInfo[1]

browser = webdriver.Firefox(executable_path="./drivers/geckodriver")


browser.get("https://www.instagram.com/")

sleep(3)

acceptcookies = browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/div/div[2]/button[1]")
acceptcookies.click()


sleep(3)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(6)

notifications = browser.find_element_by_css_selector(
    'button.aOOlW:nth-child(2)')
notifications.click()
print("clicked")

sleep(7)
browser.close()
