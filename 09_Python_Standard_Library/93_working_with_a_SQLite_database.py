# SQLite is a very light weight database, used to store data of an application (small application).

import sqlite3
import json
from pathlib import Path

# We are going to read all the movies from the JSON file from the last lesson
# and store then in a data base.

movies_list = json.loads(Path("movies.json").read_text())
print(movies_list)

# The ".connect()" method from the "sqlite3" module returns a connection object.
# We pass to it the name of our data base. If it does not exist, it will create it.
# First we need to create a command for the data base,
# this is SQL language each "?" is a placeholder for our value.
# We are lopping over our JSON file store in our variable "movies".
# And executing the "command", in the values for each movie, that have to be converted as tuples.
# When we are done we should call the ".commit()" method that will write all the changes to the data base.
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies_list:
        conn.execute(command, tuple(movie.values()))
    conn.commit()


# Now we are going to read the from our data base
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"    # command to read all the movies from the "Movies" Table
    cursor = conn.execute(command)  # When we read data from database, it returns a cursor(cursor is an iterable object)
    # for row in cursor:
    #     print(row)    # for each iteration we get a tuple with the content of each row
    movies = cursor.fetchall()  # With this method we will get a list with all the rows.
    print(movies)

# We can not run it after the for loop, because the cursor will be at the end of the rows,
# and it will not return any values.
# Therefore, we cannot use the "for row in cursor" and "cursor.fetchall()" one after the other.
# Use either one of them.
