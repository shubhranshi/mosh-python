# Working with JSON files
# JSON stands for JavaScript Object Notation.
# It is a popular way to format data in a human-readable way.
# A lot of popular of websites provide their data in JSON format.

import json
from pathlib import Path

# PART 1: writing data formatted as JSON to a file.

movies_write = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarden Cop", "year": 1993}
]

# First we set an array. In this case an array of movie objects. Each item in this array is going to be
# a dictionary, because each movie object has properties like id, title, year and so on.
# So each movie object is essentially a collection of key-value pairs

# With the ".dumps()" method form the "json" module. We convert our object to a string formatted as JSON.
data_write = json.dumps(movies_write)  # gives a string of movies data formatted as JSON
print(data_write)
# Gives: [{"id": 1, "title": "Terminator", "year": 1989}, {"id": 2, "title": "Kindergarden Cop", "year": 1993}]
# In Python, it will look the same as the syntax we wrote in our "movies" variable. (not the same case in other langs)


# Now we can write it to the file
Path("movies.json").write_text(data_write)

# with open("movies.json", "w") as movies_json: # Or we could use the "with" statement instead of "Path().write_text"
#    movies_json.write(data)


# PART 2: read the data from the JSON file.

data_read = Path("movies.json").read_text() # First we read the content of the JSON file and store it in a variable.
print(data_read)
# So "data_read" is a string that includes data formatted as JSON.

# Now we parse this string into an array of objects
movies_read = json.loads(data_read)
print(movies_read)   # So movies_read becomes an array of dictionaries, that we can access.
print(movies_read[0])
print(movies_read[0]["title"])