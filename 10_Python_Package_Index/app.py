# import requests
import nltk

response = requests.get("http://google.com")
print(response)


# If we run this file in terminal as "python app.py"
# it will search for "requests" package globally.
# If we have installed this package locally in our virtual environment, then
# we need to run this script inside of our virtual environment