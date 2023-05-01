from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
import dependency_filler # this will run automatically just by importing

import warnings
warnings.filterwarnings("ignore")

def randomStringGen(sl=10, isEmail=False):
    import random
    import string
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(sl))

    if isEmail:
        return ''.join(random.choice(letters) for i in range(sl))+"@gmail.com"

def randomPhNo():
    import random
    return random.randint(9000000000,9999999999)


url = 'https://rpademo.automationanywhere.com/newuser.php' # New User Registration
chrome_driver_path = './chromedriver'

prefs = {"profile.default_content_setting_values.notifications": 2}
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument('--headless')
options.add_argument("--disable-gpu")
# options.add_argument("window-size=1920,1080")
options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# open url
driver.get(url)

# fill form

def wait_for_ele(driver, xpath):
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))


wait_for_ele( driver, "//*[@name='firstname']")
driver.find_element(By.XPATH,"//*[@name='firstname']").send_keys(randomStringGen())

wait_for_ele( driver, "//*[@name='lastname']")
driver.find_element(By.XPATH,"//*[@name='lastname']").send_keys(randomStringGen())

wait_for_ele( driver, "//*[@name='companyname']")
driver.find_element(By.XPATH,"//*[@name='companyname']").send_keys(randomStringGen())

wait_for_ele( driver, "//*[@name='email']")
driver.find_element(By.XPATH,"//*[@name='email']").send_keys(randomStringGen(isEmail=True))

wait_for_ele( driver, "//*[@name='companyname']")
driver.find_element(By.XPATH,"//*[@name='companyname']").send_keys(randomStringGen())

wait_for_ele( driver, "//*[@name='phonenumber']")
driver.find_element(By.XPATH,"//*[@name='phonenumber']").send_keys(randomPhNo())



username = randomStringGen(12)
password = randomStringGen(10)

wait_for_ele( driver, "//*[@name='username']")
driver.find_element(By.XPATH,"//*[@name='username']").send_keys(username)

wait_for_ele( driver, "//*[@name='password']")
driver.find_element(By.XPATH,"//*[@name='password']").send_keys(password)

# append to file
with open('credentials.txt', 'a') as f:
    f.write(username + "," + password + ',' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +  "\n")

# submit form
wait_for_ele( driver, "//*[@type='submit']")
driver.find_element(By.XPATH,"//*[@type='submit']").click()

# check for success message
wait_for_ele( driver, "//*[@id='message']/h3")
if driver.find_element(By.XPATH,"//*[@id='message']/h3").text == "User added.":
    print("User added successfully")
time.sleep(5)

