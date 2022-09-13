import os
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import os
clear = lambda: os.system('cls')

warnings.filterwarnings("ignore")

months = ("Sep")
days = ("09") # Only 9/11 accounts
years = ("2001")


f = open("SAM-acc.txt", "w")
file_exists = os.path.exists('SAM-acc.txt')

print("\n you might have to do captcha if you've \n generated too many")
usernameinput = input(" Username: ")
passwordinput = input(" Password: ")

def fuckoff():
    print('fuck off chromedriver, jus press enter')
    xy = input("press enter")
    clear()

def yes_or_no():
    reply = str(input('\n \n \n \n \n \n terminate processes?'+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        driver.quit()
    if reply[0] == 'n':
        print('ok we not close :D')
    else:
        return yes_or_no("reeetaaaaard (y/n): ")

print("writing user&pass into SAM-acc.txt")

shidfard = (usernameinput + ":" + passwordinput)

f.write(shidfard)
f.close()

driver = webdriver.Chrome()
driver.get("https://roblox.com/signup") #roblox signup page

userelement = driver.find_element(By.NAME, "signupUsername") #username
userelement.send_keys(usernameinput)

month_dropdown_list = driver.find_element_by_name("birthdayMonth")
Select(month_dropdown_list).select_by_value(months) #bd year

day_dropdown_list = driver.find_element_by_name("birthdayDay")
Select(day_dropdown_list).select_by_value(days) #bd day

year_dropdown_list = driver.find_element_by_name("birthdayYear")
Select(year_dropdown_list).select_by_value(years) #bd year


password_input_box = driver.find_element_by_name("signupPassword")
password_input_box.send_keys(passwordinput) #inputs password

print('waiting 1 second and registering')

time.sleep(1)
#waits 1 second retard

declinecookie = driver.find_element(By.CLASS_NAME, "cookie-banner-bg")
declinecookie.click()
time.sleep(0.3)
gender = driver.find_element(By.ID, "MaleButton")
gender.click()

time.sleep(0.3)
signup = driver.find_element_by_name("signupSubmit")
signup.click()

print('finished making account - user: ', usernameinput, ' - password: ', passwordinput)
print('saved user:pass combo into SAM-acc.txt')

time.sleep(0.3)

print("\n")

fuckoff()

yes_or_no()