# Ayush Petigara
# import required modules
import time
import getpass
from twilio.rest import Client
from selenium import webdriver

# url that I am trying to access
url = 'https://learn.zybooks.com/zybook/CLEMSONCPSC3300AllenFall2019'
email = 'your zybooks email'

password = getpass.getpass(prompt='Please enter your zybooks password: ')

driver = webdriver.Chrome(executable_path='path to your chrome driver')
driver.get(url)

driver.find_element_by_css_selector("input[type='email']").send_keys(email)
driver.find_element_by_css_selector("input[type='password']").send_keys(password)
driver.find_element_by_xpath("//*[@class='signin-button zb-button primary raised full-width ember-view']").click()

wait = 15
driver.implicitly_wait(wait)
driver.find_element_by_xpath("//*[@class='full-tab inactive']/following-sibling::button/following-sibling::button").click()

due_date = []
due_date = driver.find_elements_by_xpath("//*[@class='due-date-text']")

# formatting the output
result = "Hi, \n Following are the due dates of your zybooks assignments: \n"
for i in due_date:
    text = i.text.split('\n')
    if (text[0] == 'Due:'):
        result += i.text
        result += '\n'

# using twilio client to send the SMS
account_sid = 'your twilio account sid'
auth_token = 'your twilio auth token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=result,
                     from_='+1##########',
                     to='+1##########'
                 )

print(message.sid)

time.sleep(5)
driver.quit()

