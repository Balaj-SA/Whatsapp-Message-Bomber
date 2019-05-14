from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyfiglet import Figlet 
import time

custom_fig=Figlet(font='cyberlarge')
print(custom_fig.renderText('Whatsapp Bomber'))
target=str(input("Enter the contact name: "))
string = str(input('Enter your message: '))
n = int(input('spam count: '))

browser = webdriver.Firefox()
browser.get("https://web.whatsapp.com/")
print("Scan the QR code with your android mobile from whatsapp")
time.sleep(60)
print("..........QR code scanned.........")
print("..........sending message........")
name = '//span[contains(@title, '+ '"' +target + '"'+ ')]'
print(name)
print("The contact name was detected by the bot")
wait = WebDriverWait(browser,30)
person_title = wait.until(EC.presence_of_element_located((By.XPATH, name)))
print(person_title)
person_title.click()
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

for i in range(n):
    input_box.send_keys(string + Keys.ENTER)
time.sleep(1)
print("The message was sent successfully")
