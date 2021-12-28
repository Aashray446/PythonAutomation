from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyinputplus as inpt
import time
url  = "https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=1&msaredir=1&client-request-id=db4673b7-ca9e-7750-7230-55f5ffd062e0&protectedtoken=true&claims=%7b%22id_token%22%3a%7b%22xms_cc%22%3a%7b%22values%22%3a%5b%22CP1%22%5d%7d%7d%7d&nonce=637762610973301006.a8d3275e-0112-4df7-b359-21593c1c83dc&state=Dcu9DoIwFEDhou_iVrm317Z0IA4aw4ALmmjY-kcikWCAYHx7O3xnOxljbJtskgxSmFaktRIKwWgiQAC1t0UgoWXkgCj4IXSaO5KGC5SGPPqCgs_Se87Hr82P82KXWOJuiuE1Rb_cx9JWDfjqquqfWcOzmZ0wUz2YoR3efXuTvROwusfl407FHw"
##email = inpt.inputEmail("Enter email")
##some_text = input("Enter any text")
browser = webdriver.Chrome()
browser.get(url)

try:
    user_name = browser.find_element_by_name("loginfmt")
    user_name.send_keys('aashray9876@outlook.com')
    user_name.send_keys(Keys.RETURN)
    time.sleep(5)
    password = browser.find_element_by_id("i0118")
    password.send_keys('Aashray@9876')
    password.send_keys(Keys.RETURN)
    time.sleep(5)
    btn = browser.find_element_by_id("idSIButton9")
    btn.click()
    time.sleep(10)
    button = browser.find_elements_by_class_name("root-174")
    button[0].click()
    time.sleep(10)
    inputs = browser.find_elements_by_tag_name("input")
    inputs[4].send_keys("aashray446@gmail.com")
    inputs[5].send_keys("subject")
    inputs[5].send_keys(Keys.TAB ,"sasdasas")
    ##text_area = browser.find_element_by_id("virtualEditScroller87")
    ##text_area.send_keys("Lorem Ipsum")
    button = browser.find_elements_by_class_name("root-253")
    button[0].click()
    time.sleep(10)
    print("Email Send Successfully")
except:
    print("not found")
