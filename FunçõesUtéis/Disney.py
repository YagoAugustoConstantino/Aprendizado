from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=r"C:\Users\GAMER\PycharmProjects\chromedriver.exe")
drive = webdriver.Chrome(service=service)

def dysnei():
    drive.implicitly_wait(3)
    drive.maximize_window()
    drive.get(r'https://www.disneyplus.com/pt-br?cid=DSS-Search-Google-71700000075038498-&s_kwcid=AL!8468!3!546262373719!e!!g!!disney&gclid=Cj0KCQiA_P6dBhD1ARIsAAGI7HC2jHewV1JqV05Hz6ftKZZgmCQSfXZ4Hk5A7eaXPTgnxsXmZV14Fs4aAtoKEALw_wcB&gclsrc=aw.ds')
    sleep(2)
    drive.find_element('xpath', '/html/body/header/nav[1]/ul/li/a').click()
    sleep(10)

    drive.find_element('xpath', '/html/body/div/div/div[4]/div/main/div/form/fieldset/span/input').send_keys('yagoa.const@outlook.com.br')
    sleep(2)

    drive.find_element('xpath', '//*[@id="dssLogin"]/div[2]/button').click()
    sleep(5)

    drive.find_element('xpath', '//*[@id="password"]').send_keys('Y@g22523464')
    sleep(3)

    drive.find_element('xpath', '//*[@id="dssLogin"]/div[2]/button').click()
    sleep(3)

    drive.find_element('xpath', '/html/body/div[1]/div/div[4]/div/main/div/div/section/ul/div[4]/div/div').click()
    sleep(5)

dysnei()
drive.quit()

