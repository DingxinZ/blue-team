import requests
import time
import getpass
import selenium
import sys
import csv

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

default_target = "http://10.83.65.37:8080/"

def success(message):
    print("Successful load: ", message)
    time.sleep(2)

def access(driver, id, name):
    print("Loading %s..." % name)
    login_button = driver.find_element_by_id(id)
    login_button.click()
    success(name)

def initial(target, driver):

    print("Virtual user for access resources:")

    print("Loading server...")
    driver.get(target)
    print("Load success!")
    print("Loading homepage...")
    success("homepage")

def scrape(target):
    options = Options()
    options.add_argument('headless')
    #options.set_headless(headless=True)
    driver = webdriver.Firefox(firefox_options=options)
    initial(target, driver)

    access(driver, "login", "login_page")
    print("Enter your username: ", end = "")
    time.sleep(1)
    print("admin")
    username = "admin"
    print("Enter your password: ", end = "")
    time.sleep(1)
    print("*****")
    password = "admin"
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id("loginbutton")
    login_button.click()
    time.sleep(2)

    access(driver, "banuser", "muteuser_page")
    print("Enter the user you want to mute: ", end = "")
    time.sleep(1)
    print("user2019")
    username_mute = "user2019"
    username_mute_field = driver.find_element_by_id("username1")
    username_mute_field.clear()
    username_mute_field.send_keys(username_mute)
    time.sleep(2)
    mute_button = driver.find_element_by_id("ban")
    mute_button.click()
    time.sleep(2)
    print("Lift success!")

    print("logging out...")
    logout_button = driver.find_element_by_id("logout")
    logout_button.click()
    time.sleep(2)
    print("successfully logged out!")
    time.sleep(2)

    access(driver, "login", "login_page")
    print("Enter your username: ", end = "")
    time.sleep(1)
    print("user2019")
    username = "user2019"
    print("Enter your password: ", end = "")
    time.sleep(1)
    print("******")
    password = "Webhub19"
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id("loginbutton")
    login_button.click()
    time.sleep(2)

    print("Loading sendmessage_page...")
    sendmessage = driver.find_element_by_id("sendmessage")
    sendmessage.click()
    try:
        send_button = driver.find_element_by_id("sendbutton")
        success("sendmessage_page")
    except:
        print("No access to send messages!")

    print("logging out...")
    logout_button = driver.find_element_by_id("logout")
    logout_button.click()
    time.sleep(2)
    print("successfully logged out!")
    time.sleep(2)

    access(driver, "login", "login_page")
    print("Enter your username: ", end = "")
    time.sleep(1)
    print("admin")
    username = "admin"
    print("Enter your password: ", end = "")
    time.sleep(1)
    print("*****")
    password = "admin"
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id("loginbutton")
    login_button.click()
    time.sleep(2)

    access(driver, "banuser", "muteuser_page")
    print("Enter the user you want to lift: ", end = "")
    time.sleep(1)
    print("user2019")
    username_lift = "user2019"
    username_lift_field = driver.find_element_by_id("username2")
    username_lift_field.clear()
    username_lift_field.send_keys(username_lift)
    time.sleep(2)
    lift_button = driver.find_element_by_id("lift")
    lift_button.click()
    time.sleep(2)
    print("Lift success!")

    print("logging out...")
    logout_button = driver.find_element_by_id("logout")
    logout_button.click()
    time.sleep(2)
    print("successfully logged out!")
    time.sleep(2)

    access(driver, "login", "login_page")
    print("Enter your username: ", end = "")
    time.sleep(1)
    print("user2019")
    username = "user2019"
    print("Enter your password: ", end = "")
    time.sleep(1)
    print("******")
    password = "Webhub19"
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id("loginbutton")
    login_button.click()
    time.sleep(2)

    print("Loading sendmessage_page...")
    sendmessage = driver.find_element_by_id("sendmessage")
    sendmessage.click()
    try:
        send_button = driver.find_element_by_id("sendbutton")
        success("sendmessage_page")
    except:
        print("No access to send messages!")
    time.sleep(2)

    print("Closing the server...")
    time.sleep(2)
    driver.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        target_url = default_target
    else:
        target_url = sys.argv[1]

scrape(target_url)
#    groups = scrape(target_url)
#    csv_groups(groups)
print("Finished!")
