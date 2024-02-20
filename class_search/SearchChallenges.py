from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchChallenges():
	def __init__(
		self, name_challenge):
		self.url_page = "https://the-internet.herokuapp.com/"
		self.name_challenge = name_challenge
		self.configurations_bot()

	def configurations_bot(self):	
		configurations = webdriver.ChromeOptions()
		configurations.add_argument("--headless")
		configurations.add_argument("--start-maximized")
		configurations.add_argument("--incognito")
		self.driver = webdriver.Chrome(options=configurations)

	def driver_instance(self):
		self.driver
		return self.driver

	def get_page(self):
		self.driver.get(self.url_page)
		if self.driver.current_url == self.url_page:
			print("Request for page OK!")

	def select_challenges(self):		
		for options_challenges in range(1,44):
			try:
				menu_options = self.driver.find_element(By.XPATH,f'/html/body/div[2]/div/ul/li[{options_challenges}]/a')
				if menu_options.text == self.name_challenge:
					request_challenge = menu_options.get_attribute("href")
					self.driver.get(request_challenge)
					print("Option for testing selected:", request_challenge)
					break
			except Exception as e:
					print(f"Error:{e}")
					pass

# Example Usage
#test_herokuapp = SearchChallenges(name_challenge="Drag and Drop")
#test_herokuapp.configurations_bot()
#test_herokuapp.get_page()
#test_herokuapp.select_challenges()
