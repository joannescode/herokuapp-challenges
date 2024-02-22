import sys
sys.path.append("/home/joannes/Documents/herokuapp-challenges")
from class_search.SearchChallenges import *
from selenium.webdriver.support.ui import Select
import random
from colorama import Fore

test_herokuapp = SearchChallenges(name_challenge="Dropdown")
test_herokuapp.configurations_bot()
test_herokuapp.get_page()
test_herokuapp.select_challenges()

driver = test_herokuapp.driver_instance()
challenge_title = driver.find_element(By.TAG_NAME,"h3")
print(f"Testing {challenge_title.text}...\n")

random_list = []
for number in range(30):
    item_number = random.randint(1,2)
    random_list.append(item_number)
    
dropdown_list = Select(driver.find_element(By.ID,"dropdown"))    
for item in random_list:
    dropdown_list.select_by_value(str(item))
    item_selected = dropdown_list.first_selected_option.get_attribute("value")
    
    if str(item) == item_selected:
        print(Fore.GREEN + f"Value selected is {item_selected} and value in random_list is {str(item)} ✅")
    else:
        print(Fore.RED + f"Value selected is {item_selected} and value in random_list is {str(item)} ❌")

# Testing disabled value in dropdown menu
try:
    dropdown_list.select_by_value("disabled")
except Exception as e:
    print(Fore.RED + "\nError: ",e)
