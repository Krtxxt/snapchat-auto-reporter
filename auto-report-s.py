import random
import string
import time
from selenium import webdriver

# function to generate a random username
def random_username(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

# set the number of reports to make before creating a new account
reports_per_account = 5

# start the infinite loop to report users
while True:
    # generate a new username and password
    username = random_username(10)
    password = 'YourPasswordHere'

    # create a new webdriver instance
    driver = webdriver.Chrome('chromedriver.exe')

    # navigate to the Snapchat signup page
    driver.get('https://accounts.snapchat.com/accounts/signup')

    # fill in the signup form with the random username and password
    driver.find_element_by_id('signup-username').send_keys(username)
    driver.find_element_by_id('signup-password').send_keys(password)

    # click the signup button
    driver.find_element_by_id('signup-button').click()

    # wait for the signup process to complete
    time.sleep(5)

    # navigate to the user profile to report
    driver.get('https://www.snapchat.com/add/USERNAME_HERE')

    # click the three-dot icon to open the user options
    driver.find_element_by_css_selector('div > div > svg[aria-label="More"]').click()

    # click the report button
    driver.find_element_by_xpath('//span[contains(text(),"Report")]').click()

    # click the 'It's spam' option
    driver.find_element_by_xpath('//span[contains(text(),"It")]').click()

    # click the 'Report' button
    driver.find_element_by_xpath('//span[contains(text(),"Report")]').click()

    # wait for the report to be submitted
    time.sleep(5)

    # close the webdriver instance
    driver.quit()

    # decrement the number of reports left for this account
    reports_per_account -= 1

    # if we have reported enough users, create a new account and reset the report count
    if reports_per_account == 0:
        reports_per_account = 5
