from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import string

web=webdriver.Chrome(ChromeDriverManager().install())
#------- Account infromation ------------
name = "" 
password = ""
lang = ""

new_adress = "" #type new email adress here
# ---------------------------------------

web.get("https://www.allcashbackcasino.com/?lang=en")

time.sleep(5)

openLogWin = web.find_element_by_xpath('//*[@id="pageLoginForm"]/div/div/a[1]').click()

time.sleep(5)

# Login user
username = web.find_element_by_xpath('//*[@id="loginusernameInput"]')
username.send_keys(name)

securityfield = web.find_element_by_xpath('//*[@id="loginpasswordInput"]')
securityfield.send_keys(password)

login= web.find_element_by_xpath('//*[@id="lightboxLoginForm"]/div/fieldset[4]/a')
login.click()

time.sleep(10)
#---------------- open Personal Details & change email adress ------------
web.get("https://www.allcashbackcasino.com/my-account/?lang=en#myAccount/personalDetails")

time.sleep(5)

#  change language 
web.find_element_by_xpath("//option[@value='" + lang + "']").click()

upDet = web.find_element_by_xpath('//*[@id="popupPersonalDetailsForm"]/div/fieldset[12]/a').click() 

time.sleep(5)                           
closeWin = web.find_element_by_xpath('//*[@id="myAccountPersonalDetailsCompleteLightbox"]/div[1]/a').click() 

time.sleep(5)
# Change email adress

em = web.find_element_by_xpath('//*[@id="registerEmailInput"]').clear()

time.sleep(1)

Fn = web.find_element_by_xpath('//*[@id="registerEmailInput"]')
Fn.send_keys(new_adress)

time.sleep(2)
update= web.find_element_by_xpath('//*[@id="popupPersonalDetailsForm"]/div/fieldset[12]/a')
update.click()

