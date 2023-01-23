# Browser Automation
# https://selenium-python.readthedocs.io/   (Waits and Page objects are important advanced topics)

# with selenium we can automate testing browser.
# In this example we are going to test function on a website, with browser automation.
# Writing a script that will test the log-in function in git hub.

# First, install selenium library, pip or pipenv install selenium.
# We also a driver, a driver is a piece of software to automate a specific browser.
# Each browser (eg. chrome) have their own specific browser. Link : https://pypi.org/project/selenium/
# download the drivers (put it in Path... Windows folder in C: drive)

# webdriver module has classes that represent all the popular browsers
from selenium import webdriver

browser = webdriver.Chrome()    # Here we create a browser object
browser.get("https://github.com")   # We use the browser object to navigate to https://github.com

# We can to find the elements on the webpage by their id, class, name, or text. (Inspect the page)

# browser.find_element_by_link_text("Sign in")  # deprecated now. Use below instead:
signin_link = browser.find_element("link text", "Sign in")    # Finding the "Sign in" button by its text
signin_link.click()

username_box = browser.find_element("id", "login_field")    # Finding the username filed by the id.
username_box.send_keys("ninjacoder22")  # We use the ".send_keys()" method to type the username in the username field.

password_box = browser.find_element("id", "password")
password_box.send_keys("blahblah")
password_box.submit()

# To make sure this log in function worked properly we want to make an assertion
# The ".page_source" attribute return the html content of the webpage as a string.
# And we are aaserting if the "ninjacoder22" is in that html string.
# if the string is not found, we will get an exception AssertionError.
assert "ninjacoder22" in browser.page_source

# we can be more specific with the asserting. like this
profile_link = browser.find_element("class", "user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "ninjacoder22" in link_label # The ".page_source" attribute return the html content of the webpage.

browser.quit()  # to close the browser window
