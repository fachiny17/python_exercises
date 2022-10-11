from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "C:\Users\CHISOM\Downloads/chromedriver_win32"


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)