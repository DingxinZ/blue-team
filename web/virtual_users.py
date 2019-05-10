import requests
import time
import getpass
import selenium
import sys
import csv
import getpass

from selenium import webdriver

#------------------------------------------------

default_target = "http://localhost:8080/"

#------------------------------------------------
# Useage:
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------
#def create_account(driver):

def success(message):
    print("Successful load: ", message)
    time.sleep(2)

def access(driver, id, name):
    login_button = driver.find_element_by_id(id)
    login_button.click()
    success(name)

def scrape(target):

    driver = webdriver.Firefox()
    groups = {}


    print("Canvas login creds:")

    print("Loading login portal")
    driver.get(target)
    success("homepage")

    access(driver, "register", "register_page")

    username = input("Enter your username for register: ")
    print("Enter your new password")
    password = getpass.getpass()
    print("Enter your password again")
    password2 = getpass.getpass()

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

    print("success register")
    #driver.get(target)

    username = input("Enter your username: ")
    print("Enter your password")
    password = getpass.getpass()

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

    print("logged in!")

    access(driver, "user", "profile page")
    
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

    time.sleep(2)

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
