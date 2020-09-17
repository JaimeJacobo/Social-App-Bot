from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

driver.get("https://tinder.com")

# Hacer click en log in button

def click_on_log_in_button():
    log_in_button = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
    log_in_button.click()


def prueba(counter_int):
    try:
        click_on_log_in_button()
    except:
        counter_int = counter_int + 1
        print("No se encontró botón de LOG IN. Probemos otra vez. Intento número " + str(counter_int))
        if counter_int < 500:
            prueba(counter_int)


prueba(0)


time.sleep(1)
facebook_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_button.click()

main_window = driver.window_handles[0]
pop_up_window = driver.window_handles[1]
driver.switch_to.window(pop_up_window)

email_input = driver.find_element_by_xpath('//*[@id="email"]')
password_input = driver.find_element_by_xpath('//*[@id="pass"]')

email_input.send_keys('YOUR_USERNAME_HERE')
password_input.send_keys('YOUR_PASSWORD_HERE')

time.sleep(1)
log_in_facebook_button = driver.find_element_by_xpath('//*[@id="loginbutton"]')
log_in_facebook_button.click()

time.sleep(1)
driver.switch_to.window(main_window)
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

# allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
# allow_location_button.click()

time.sleep(1)
# enable_location = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
# enable_location.click()

time.sleep(5)


# Find Tinder's pop-up and if it exists, click on "Maybe later"
def manage_maybe_letter_button():
    maybe_later_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]')
    maybe_later_button.click()


def find_publicity_popup(counter_int):
    try:
        manage_maybe_letter_button()
    except:
        counter_int = counter_int + 1
        print("No se encontró botón. Porbemos otra vez. Intento número " + str(counter_int))
        if counter_int < 500:
            find_publicity_popup(counter_int)


find_publicity_popup(0)

# def like():
#     like_button = driver.find_element_by_xpath(
#         '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
#     like_button.click()
#
#
# for i in range(10):
#     time.sleep(4)
#     like()
