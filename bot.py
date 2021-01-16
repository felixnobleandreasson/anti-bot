from time import sleep
from selenium import webdriver

browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

browser.get("https://www.instagram.com/")

sleep(3)

acceptcookies = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
acceptcookies.click()

#browser.close()