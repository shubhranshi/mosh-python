# Web Scraping:
# Not every website has an API to work with.
# In situations like that the only way to get the data we want is to parse the html behind a webpage,
# get rid of all the html tags, and extract the actual data.
# This technique is called Web Scraping.
# So we scrape all the HTML tags and extract the data that we want.
# In this example we are going to write a program that extract the list of the newest questions
# form https://stackoverflow.com/questions/
# This is called a Web Crawler or a Web Spider.

# For this we are going to use the "beautifulsoup4" package
# It is a very popular package for extracting information from HTML and XML files.
# (pip or pipenv) install beautifulsoup4


import requests
from bs4 import BeautifulSoup

# first download the webpage containing newest question

# Using the ".get()" method form the "request" module to download the web page.
response = requests.get("https://stackoverflow.com/questions")
# This returns the html content with the ".text" attribute
content_html = response.text
# BeautifulSoup can read any html or xml text given to it in form of a string.
soup = BeautifulSoup(content_html, "html.parser")
#print(soup)
# This soup object mirrors the structure of our html document so we can navigate
# this document and find various elements
# We can inspect (right click on webpage) the webpage and find the relevant tags that contains information.

# We pass the CSS selector we type "." and then the name of the class.
# In this case (".question-summary") class_name: ".s-post-summary.js-post-summary". This will return a list.
questions = soup.select(".s-post-summary.js-post-summary")
print(type(questions[0]))
# Type of question 1, each item in "questions" list is an instance of Tag class
# this Tag object has some attributes that are stored in a dictionary "attr"
print(questions[0].attrs)
print(questions[0].select(".s-link"))

for question in questions:
    print(question.select_one(".s-link").getText())  # ".question-hyperlink"
    # The ".select_one()" method can be used in this particular case because each question had only
    # one title, so we don't need to return a list. getText() helps to get value of tag.
    print(question.select_one(".s-post-summary--stats-item-number").getText())  # ".vote-count-post"


