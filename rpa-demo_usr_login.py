from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
import dependency_filler # this will run automatically just by importing

import warnings
warnings.filterwarnings("ignore")


url = 'https://rpademo.automationanywhere.com/' # New User Registration
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

# readin credentials
with open('credentials.txt', 'r') as f:
    credentials = f.readlines()
    username = credentials[-1].split(',')[0]
    password = credentials[-1].split(',')[1]

wait_for_ele( driver, "//*[@name='username']")
driver.find_element(By.XPATH,"//*[@name='username']").send_keys(username)

wait_for_ele( driver, "//*[@name='password']")
driver.find_element(By.XPATH,"//*[@name='password']").send_keys(password)

# login form
wait_for_ele( driver, "//*[@type='button']")
driver.find_element(By.XPATH,"//*[@type='button']").click()

# check for success message


wait_for_ele( driver, "/html/body/form/center/h1")
if driver.find_element(By.XPATH,"/html/body/form/center/h1").text == "Successfully Logged In":
    print("User login successfully")

print("Msg for you mate from site:", driver.find_element(By.XPATH,"/html/body/form/center/h3").text)
time.sleep(5)

