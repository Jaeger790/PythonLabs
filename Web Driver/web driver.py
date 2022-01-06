

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time



browser = webdriver.Firefox();
path = "C:\\Programs\\Python36\\BrowersDriver\\chromedriver.exe";

browser.get("https://boards.greenhouse.io/epicgames/jobs/4159339004?gh_src=9bde549b4us#app")

login = browser.find_elements_by_xpath('//*[@id="first_name"]')
login[0].click();

time.sleep(2)

userName = browser.find_elements_by_id("first_name")
userName[0].send_keys("Bradley")


user = browser.find_elements_by_id("last_name")
user[0].send_keys("Rott")


email = browser.find_elements_by_id("email")
email[0].send_keys("b.rott8401@gmail.com")

phone = browser.find_elements_by_id("phone")
phone[0].send_keys('2097704977')








time.sleep(2)

login_button = browser.find_elements_by_xpath('//*[@id="signOnButton"]')
login_button[0].click()