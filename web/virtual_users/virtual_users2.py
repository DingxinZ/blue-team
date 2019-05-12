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

    front_end_button = driver.find_element_by_id("Front-end")
    hover = ActionChains(driver).move_to_element(front_end_button)
    hover.perform()
    time.sleep(5)
    access(driver, "HTML-int", "HTML_intro_page")
    time.sleep(2)
    access(driver, "sHTML-tut", "HTML_tut_page")
    time.sleep(2)
    access(driver, "sCSS-int", "CSS_intro_page")
    time.sleep(2)
    access(driver, "sCSS-tut", "CSS-tut_page")
    time.sleep(2)
    access(driver, "sJS-int", "Javascript_intro_page")
    time.sleep(2)
    access(driver, "sJS-tut", "Javascript_tut_page")
    time.sleep(2)

    back_end_button = driver.find_element_by_id("Back-end")
    hover = ActionChains(driver).move_to_element(back_end_button)
    hover.perform()
    time.sleep(5)
    access(driver, "PB-int", "PythonBottle_intro_page")
    time.sleep(2)
    access(driver, "sPB-tut", "PythonBottle_tut_page")
    time.sleep(2)
    access(driver, "sPHP-int", "PHP_intro_page")
    time.sleep(2)
    access(driver, "sPHP-tut", "PHP_tut_page")
    time.sleep(2)

    Database_button = driver.find_element_by_id("Database")
    hover = ActionChains(driver).move_to_element(Database_button)
    hover.perform()
    time.sleep(5)
    access(driver, "SQL-int", "SQL_intro_page")
    time.sleep(2)
    access(driver, "sSQL-tut", "SQL_tut_page")
    time.sleep(2)
    access(driver, "sMysql-int", "Mysql_intro_page")
    time.sleep(2)
    access(driver, "sMysql-tut", "Mysql_tut_page")
    time.sleep(2)
    access(driver, "sSQLite-int", "SQLite_intro_page")
    time.sleep(2)
    access(driver, "sSQLite-tut", "SQLite_tut_page")
    time.sleep(2)

    print("successfully accessing all resources!")
    time.sleep(2)
    print("logging out...")
    logout_button = driver.find_element_by_id("logout")
    logout_button.click()
    time.sleep(2)
    print("successfully logged out!")
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
