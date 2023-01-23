# lets install "requests" package inside a virtual environment.

import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "eioqwr54389NotTheRealAPIKey" # get the actual API key from Yelp developer --> our APP.
headers = {
    "Authorization": "Bearer " + api_key
}
params = {
    "term": "Indian Food",
    "location": "Taipei"
}
# requests.get() is used to send an HTTP request to the endpoint to get data. It returns a response object
response = requests.get(url, headers=headers, params=params)

# Use the ".text" method to convert the response to text.
# It can be used in case of error so see the description of the error.
print(response.text)

result = response.json()    # To convert the response into a dictionary use the "json()" method.
businesses = result["businesses"]   # Accessing the "businesses" key in the dictionary.
print(businesses)
for business in businesses:
    print(business["name"])

filter_busi = [business["name"] for business in businesses if business["rating"] >= 4.5]
# We are using a comprehension list to filter all the business with rating >= 4.5 and storing their name in a new list.
print(filter_busi)