# In the previous lesson we stored our API key in our code.
# That's a bad practice, because if we publish our code to git this API key will be visible to anyone.
# We should store our API Key in another file and exclude that file from git.
# Also, some malicious person may get access to our API key and violate the policy of Yelp or misuse the platform.

# Create a new file "config.py" which will store all sort of configuration parameters for our application,
# including the API Key. (api_key="432felijfl3342523")
# Then in our application we must import the "config" module and in the module we have an attribute call "api_key"

# To exclude this file from git. Add a new file and call it ".gitignore".
# There we can specify what file and directories should be excluded from our git repository.

import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Indian Food",
    "location": "Taipei"
}

response = requests.get(url, headers=headers, params=params)
result = response.json()
businesses = result["businesses"]

filter_busi = [business["name"] for business in businesses if business["rating"] >= 4.5]
print(filter_busi)