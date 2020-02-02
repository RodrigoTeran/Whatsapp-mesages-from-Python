# Code to send message to WhatsApp from python 3.7
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import socket

# -----------------------------------CHANGE-----------------------------------
message_text = 'mesage...'  # message you want to send
no_of_message = 1  # number of times the message is send
# phone numbers (integer) or links to WhatsApp groups (string)
moblie_no_list = [000000000, 000000000, 000000000]
# -----------------------------------CHANGE-----------------------------------


def element_presence(by, xpath, time):
    element_present = ec.presence_of_element_located((by, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        is_connected()


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(10)


def send_whatsapp_msg(phone_no, text):
    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to.alert
    except:
        pass
    try:
        element_presence(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except:
        print("invailid phone no :"+str(phone_no))


for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no, message_text)
    except:
        sleep(10)
        is_connected()
