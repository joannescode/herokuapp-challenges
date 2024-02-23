import sys
sys.path.append('/home/joannes/Documents/herokuapp-challenges')
from class_search.SearchChallenges import *
from PIL import Image

test_herokuapp = SearchChallenges(name_challenge= "Basic Auth")
test_herokuapp.browser_configurations()
driver = test_herokuapp.driver_instance()

# Credentials for concat in url string
username = "admin"
password = "admin"
webpage = "the-internet.herokuapp.com/basic_auth"

driver.get(f"https://{username}:{password}@{webpage}")
driver.save_screenshot("auth_screen.png")
screenshot = Image.open("auth_screen.png")
screenshot.show()

challenge_title = driver.find_element(By.TAG_NAME, "h3")
print(f"{challenge_title.text} realized!\n")