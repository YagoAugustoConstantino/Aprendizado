from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r"C:\Users\GAMER\PycharmProjects\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(0.8)
driver.maximize_window()

driver.get(r'https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/first_script/')
link = driver.current_url
print(link)


driver.quit()
