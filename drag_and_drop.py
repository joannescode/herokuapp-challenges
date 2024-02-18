from SearchChallenges import *
from selenium.webdriver.common.action_chains import ActionChains 
import time

test_herokuapp = SearchChallenges(name_challenge="Drag and Drop")
test_herokuapp.configurations_bot()
test_herokuapp.get_page()
test_herokuapp.select_challenges()

driver = test_herokuapp.driver_()
challenge_title = driver.find_element(By.TAG_NAME, "h3")
print(f"Testing {challenge_title.text}... \n")

column_a = driver.find_element(By.ID,"column-a")
column_b = driver.find_element(By.ID,"column-b")

action = ActionChains(driver)
for try_move in range(10):
	action.drag_and_drop(column_a, column_b).perform()
	primary_column = driver.find_element(By.CLASS_NAME,"column").text
	print(f"First column is {primary_column}")
print("\nTest finish.")
