from bottle import route, get, post, request, response
import requests
import time
import getpass
import selenium
import sys
import csv
import getpass
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#------------------------------------------------

default_target = "http://10.83.65.37:8080/"

#------------------------------------------------
# Useage:
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------
#def create_account(driver):

def success(message):
    print("Successfully load: ", message)
    time.sleep(2)

def access(driver, id, name):
    print("Loading %s..." % name)
    login_button = driver.find_element_by_id(id)
    login_button.click()
    success(name)

def initial(target, driver):
    print("Virtual user for login system:")

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
    access(driver, "register", "register_page")
    print("Enter your username for register: ", end = "")
    time.sleep(1)
    print("user2019")
    username = "user2019"
    print("Enter your new password: ", end = "")
    time.sleep(1)
    print("******")
    password = "123456"
    print("Enter your password again: ", end = "")
    time.sleep(1)
    print("******")
    password2 = "123456"
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    password_field2 = driver.find_element_by_name("password2")
    password_field2.clear()
    password_field2.send_keys(password2)
    # Hit the button
    login_button = driver.find_element_by_id("registerbutton")
    login_button.click()
    time.sleep(2)
    passwordlist = ["12345678", "abc123456", "Webhub19"]
    i = 0
    while True:
        try:
            login_button = driver.find_element_by_id("loginbutton")
            break
        except:
            print("Invalid password format!")
            access(driver, "register", "register_page")
            print("Enter your username for register: ", end = "")
            time.sleep(1)
            print("user2019")
            username = "user2019"
            print("Enter your new password: ", end = "")
            time.sleep(1)
            print("********")
            password = passwordlist[i]
            print("Enter your password again: ", end = "")
            time.sleep(1)
            print("********")
            password2 = passwordlist[i]
            username_field = driver.find_element_by_name("username")
            username_field.clear()
            username_field.send_keys(username)

            # Enter password
            password_field = driver.find_element_by_name("password")
            password_field.clear()
            password_field.send_keys(password)

            password_field2 = driver.find_element_by_name("password2")
            password_field2.clear()
            password_field2.send_keys(password2)
            # Hit the button
            login_button = driver.find_element_by_id("registerbutton")
            login_button.click()
            time.sleep(2)
            i += 1
    print("Successfully register!")
    #driver.get(target)

    print("Enter your username: ", end = "")
    time.sleep(1)
    print("user2019")
    username = "user2019"
    print("Enter your password: ", end = "")
    time.sleep(1)
    print("*******")
    password = "1234567"
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
    while True:
        try:
            profile = driver.find_element_by_id("user")
            break
        except:
            print("Incorrect combination! Log in failed. Please try again.")
            access(driver, "login", "login_page")
            print("Enter your username: ", end = "")
            time.sleep(1)
            print("user2019")
            username = "user2019"
            print("Enter your password: ", end = "")
            time.sleep(1)
            print("********")
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

    print("Successfully logged in!")
    access(driver, "user", "profile page")
    profile = driver.find_element_by_name("profile").text
    print("The profile page shows: ", profile)
    time.sleep(2)
    print("logging out...")
    logout_button = driver.find_element_by_id("logout")
    logout_button.click()
    time.sleep(2)
    print("successfully logged out!")
    time.sleep(2)
    print("Closing the server...")
    time.sleep(2)
    #???????????????
    #content = driver.find_element_by_name("profile")
    #content.clear()
    #a = content.txt
    #print(driver.find_element_by_name("profile").text)
    #print("a",a)
    #driver.get(target)


#    username = input("Enter your canvas username: ")
#    password = getpass.getpass()

#    print("Logging in")

    # Enter username
#    username_field = driver.find_element_by_name("UserName")
#    username_field.clear()
#    username_field.send_keys(username)

    # Enter password
#    password_field = driver.find_element_by_name("Password")
#    password_field.clear()
#    password_field.send_keys(password)

    # Hit the button
#    login_button = driver.find_element_by_id("submitButton")
#    login_button.click()


    driver.close()
#    print("Logged in!")
#    driver.get(target)

#    for group in range(1, 50):
#        try:
            # Click to expand group header
#            group_xpath = '//*[@class="span9 groups"]//div//ul//li[{group}]//div//div//a'
#            group_heading = driver.find_element_by_xpath(group_xpath.format(group=group))
#            group_name = group_heading.text
#            group_heading.click()

#            groups[group_name] = []

            # Get members from group
#            for member in range(1,6):
#                try:
#                    member_xpath = '//*[@class="span9 groups"]//div//ul//li[{group}]//div[2]//ul//li[{member}]//div'
#                    member_name = driver.find_element_by_xpath(member_xpath.format(group=group, member=member)).text

#                    groups[group_name].append(member_name)
#                except:
#                    print("Member not found")
#        except:
#            pass

#        print("Group: {} contains {}".format(group_name, groups[group_name].__repr__()) )

#    print("Scraping finished, closing web driver.")
#    driver.close()
#    return groups


#------------------------------------------------

def csv_groups(groups):
    with open('groups.csv', 'w') as groups_file:
        csv_writer = csv.writer(groups_file)
        for count, group in enumerate(groups):
            if len(groups[group]) > 0:
                for member in groups[group]:
                    group_line = ['group_{}'.format(count ), member]
                    csv_writer.writerow(group_line)
    print("CSV written")
    return

#------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        target_url = default_target
    else:
        target_url = sys.argv[1]

scrape(target_url)
#    groups = scrape(target_url)
#    csv_groups(groups)
print("Finished!")
