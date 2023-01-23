# first we need to import the csv module
import csv


# WRITING
# using built-in open(), cannot use the Path class

# First we create and open the file in the desired location with the "open()" function in the write mode "w'.
# The "csv" module has a method for creating a csv writer "csv.writer()".
# In here we are storing that method in the "writer" variable.
# And now we can write tabular data to our file.
# newline='' will avoid adding a blank row after every row that is added.
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['transaction_id','product_id','price'])   # Here writing the first row with headings.
    writer.writerow([1, 48721, 120.00]) # Each row with data
    writer.writerow([2, 48725, 500.00])

# READING
with open("data.csv") as file:
    reader = csv.reader(file)
    print(reader)   # The reader returns an iterable object

    # We can call the list function to convert all the data in the csv file to a list.
    # Each line will be a list in the list
    # print(list(reader))
    # Note that the value of each cell is represented as a string, so we have to manually convert it to int.

    # Because the "reader" is itable we can use a for loop over it.
    for row in reader:
        print(row)

# We can not iterate twice in "reader" object.
# Because it has an index and that starts in the beginning of the file.
# And after the first iteration it goes to the end of the file.
# If we iterate it again we will not get any readings.

# With these functions we can operate over CSV files easily in python.
# Assume we have a directory that has 100s of CSV files
# we can iterate this directory, open each CSV file and remove the first row (header row)
# combine them, or summarize them, etc. For eg, summarizing or adding values of a column.
