from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
import dependency_filler # this will run automatically just by importing
import json
import warnings
import subprocess
warnings.filterwarnings("ignore")

# start chrome with remote debugging port linux no msg
subprocess.Popen(['google-chrome', '--remote-debugging-port=9222', '--user-data-dir=/home/infinity/Desktop/ChromeData'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

url = 'https://mail.google.com/'
chrome_driver_path = './chromedriver'

options = webdriver.ChromeOptions()

options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# open url
driver.get(url)

def wait_for_ele(driver, xpath):
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

# compose mail
wait_for_ele( driver, "//*[contains(text(),'Compose')]")
driver.find_element(By.XPATH,"//*[contains(text(),'Compose')]").click()

# fill form
with open('email_list.json', 'r') as f:
    email = json.load(f)

email=email['emails']

wait_for_ele( driver, "//*[@class='aH9']/input")
driver.find_element(By.XPATH,"//*[@class='aH9']/input").send_keys(email)

wait_for_ele( driver, "//*[@name='subjectbox']")
driver.find_element(By.XPATH,"//*[@name='subjectbox']").send_keys('Test Mail')

wait_for_ele( driver, "//*[@class='Am Al editable LW-avf tS-tW']")
driver.find_element(By.XPATH,"//*[@class='Am Al editable LW-avf tS-tW']").send_keys("Hello, this is a test mail")

wait_for_ele( driver, "//*[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
driver.find_element(By.XPATH,"//*[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']").click()

## check for mail send sucessful

wait_for_ele( driver, "//*[@class='aio UKr6le']/span//*[contains(text(),'Sent')]")
driver.find_element(By.XPATH,"//*[@class='aio UKr6le']/span//*[contains(text(),'Sent')]").click()

wait_for_ele( driver, "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[1]/div[1]/div[1]/div/table/tbody/tr[1]")
driver.find_element(By.XPATH,"/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[1]/div[1]/div[1]/div/table/tbody/tr[1]").click()

email_name = email[0].split('@')[0]
wait_for_ele( driver, '//*[@name="{}"]'.format(email_name))
print("Mail sent successfully to {}".format(email[0]))

time.sleep(5)

driver.quit()
subprocess.Popen(['killall', 'chrome'])
