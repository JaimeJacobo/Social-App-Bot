from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
import requests
# from datetime import date
from datetime import datetime

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


def manage_log_in_button(counter_int):
    try:
        click_on_log_in_button()
    except:
        counter_int = counter_int + 1
        print("No se encontró botón de LOG IN. Probemos otra vez. Intento número " + str(counter_int) + '/500')
        if counter_int < 500:
            manage_log_in_button(counter_int)


manage_log_in_button(0)

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
        print("No se encontró botón. Porbemos otra vez. Intento número " + str(counter_int) + '/500')
        if counter_int < 500:
            find_publicity_popup(counter_int)


find_publicity_popup(0)


def like():
    try:
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[4]/button')
    except:
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')

    like_button.click()


def check_for_match():
    try:
        back_to_tinder_button = driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/button')
        back_to_tinder_button.click()
        print('MATCH GOTTEN! <3')
    except:
        print('No match gotten')
        print('---------------')
    pass


def check_for_home_screen_popup():
    try:
        not_interested_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        not_interested_button.click()
        print('POP-UP DELETED')
    except:
        print('Pop-up didn\'t appear')


def get_age():
    age = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div[1]/div/span')
    print('Age: ' + age.text)


instagram_accounts = []


def check_for_different_instagram_typos(bio_text, typo):
    personalized_range = 0
    if typo == 'ig ':
        personalized_range = 2
    elif typo == 'ig: ' or typo == 'ig, ':
        personalized_range = 3
    elif typo == 'instagram: ':
        personalized_range = 10
    elif typo == 'instagram ':
        personalized_range = 9
    elif typo == 'insta: ':
        personalized_range = 6
    elif typo == 'insta ':
        personalized_range = 5

    bio_text = bio_text.lower()
    index = bio_text.index(typo)
    bio_text_list = list(bio_text)
    bio_text_list[index] = '@'
    for i in range(personalized_range):
        del bio_text_list[index + 1]
    bio_text = "".join(bio_text_list)
    get_instagram(bio_text)


def get_instagram(bio_text):
    instagram_account = ''
    found_space = False

    if '@' in bio_text:
        index = bio_text.index('@')
        while not found_space and index < len(bio_text):
            if bio_text[index] != ' ' and bio_text[index] != '\\':
                instagram_account = instagram_account + bio_text[index]
                index = index + 1
            else:
                found_space = True
        print('Instagram: ' + instagram_account)
        date_time_object = datetime.now()
        instagram_accounts.append([instagram_account, date_time_object.strftime("%d %b %Y")])
    elif 'ig ' in bio_text.lower():
        check_for_different_instagram_typos(bio_text, 'ig ')
    elif 'ig: ' in bio_text.lower():
        check_for_different_instagram_typos(bio_text, 'ig: ')
    elif 'ig, ' in bio_text.lower():
        check_for_different_instagram_typos(bio_text, 'ig, ')
    elif 'instagram: ' in bio_text.lower():
        check_for_different_instagram_typos(bio_text, 'instagram: ')
    elif 'instagram ' in bio_text.lower():
        check_for_different_instagram_typos(bio_text, 'instagram ')
    elif 'insta: ' in bio_text.lower():
        check_for_different_instagram_typos(bio_text, 'insta: ')
    elif 'insta ' in bio_text.lower():
        check_for_different_instagram_typos(bio_text, 'insta ')
    else:
        print('No instagram found on the bio')


def get_bio():
    try:
        bio_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/button')
        bio_button.click()

        time.sleep(3)

        bio = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div')
        print('Bio: ' + bio.text)
        get_instagram(bio.text)
    except:
        print('This person does not have a description')


out_of_likes = False


def check_if_out_of_likes():
    global out_of_likes
    try:
        no_thanks_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        no_thanks_button.click()
        print('OUT OF LIKES!')
        out_of_likes = True
    except:
        return


def do_the_magic():
    for i in range(20):
        check_if_out_of_likes()
        if not out_of_likes:
            check_for_home_screen_popup()
            time.sleep(1)
            get_age()
            get_bio()
            check_for_home_screen_popup()
            like()
            time.sleep(1)
            check_for_match()


do_the_magic()

print(instagram_accounts)
if len(instagram_accounts) > 0:
    for account in instagram_accounts:
        # template = {"username": "", "date": ""}
        # template["username"] = account["username"]
        # template["date"] = account["date"]
        requests.post('http://localhost:5555/new-user', data={"username": account[0], "date": account[1]})
        # prtint()

        # old_dict = {'hello': 'world', 'foo': 'bar'}
        # new_dict = {**old_dict, 'foo': 'baz'}