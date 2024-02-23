import sys
import itertools
import time

sys.path.append("/home/joannes/Documents/herokuapp-challenges")
from class_search.SearchChallenges import *

path_seclists = "/home/joannes/Documents/herokuapp-challenges/seclists"

usernames = []
with open(path_seclists + "/names.txt", "r") as file:
    rows = file.readlines()
    for user in rows:
        formatted_user = user.replace("\n", "")
        usernames.append(formatted_user)

passwords = []
with open(path_seclists + "/10-million-password-list-top-500.txt", "r") as file:
    rows = file.readlines()
    for code in rows:
        formatted_code = code.replace("\n", "")
        passwords.append(formatted_code)

test_herokuapp = SearchChallenges(name_challenge="Form Authentication")
test_herokuapp.browser_configurations()
test_herokuapp.get_page()
test_herokuapp.select_challenges()

driver = test_herokuapp.driver_instance()
challenge_title = driver.find_element(By.TAG_NAME, "h2")
print(f"Testing {challenge_title.text}")

authentication_list = list(itertools.product(usernames, passwords))


def elements_for_login():
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    return username, password


for username_value, password_value in authentication_list:
    username, password = elements_for_login()
    username.send_keys(username_value)
    password.send_keys(password_value)
    login_button = driver.find_element(By.CLASS_NAME, "radius")
    login_button.click()
    authentication_message = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in authentication_message:
        print(
            f"Access with username: {username_value} with password: {password_value} sucessful!"
        )
        break
    else:
        username, password = elements_for_login()
        username.clear()
        password.clear()


# credits to Daniel Miessler for sharing the seclists on github
