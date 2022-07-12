import time
from weakref import ref
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# USERNAME = input('Please enter username: ') or 'instructor'
# PASSWORD = input('Please enter password: ') or 'Qwer1234'
email_list = []

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(r'chromedriver.exe'), options=options)



# def login():
#     url = "https://latbob.com/user-account/"
#     driver.get(url)

#     user = driver.find_element("name", "login")
#     user.send_keys(USERNAME)

#     pwd = driver.find_element("name", "password")
#     pwd.send_keys(PASSWORD)
#     pwd.send_keys(Keys.ENTER)

# def addStudent():
#     URL = "https://latbob.com/user-account/add-students/"
#     driver.get(URL)

#     email_box = driver.find_element(By.CSS_SELECTOR, "input[class ='form-control'")
#     for email in email_list:
#         email_box.send_keys(email)
#         email_box.send_keys(Keys.ENTER)

def open():
    url = "https://www.google.com/"
    driver.get(url)


def refreshing():
    n = 0
    while n < 5:
        open()
        time.sleep(2)
        for x in range(len(driver.window_handles)):
            driver.switch_to.window(driver.window_handles[x])
            driver.refresh()
            time.sleep(2)
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
        n += 1
        print(driver.window_handles)



refreshing()
# open()
# # login()
# time.sleep(2)
# # driver.switch_to.window(driver.window_handles[1])
# # open()
# time.sleep(4)
# driver.refresh()

# driver.execute_script("window.open()")
# driver.switch_to.window(driver.window_handles[1])

# addStudent()
