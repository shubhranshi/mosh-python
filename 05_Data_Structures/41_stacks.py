# Data structure:  Stack, eg. stack of books,
# the last book on top of the stack is the first to be removed.
# LIFO - last in first out

# list can be used to implement stack
stack = [1, 2, 3, 4]

# EXAMPLE: browser stack
# A good example would be a browser back page

browsing_session = []

# whenever user navigates a new websites, each website is added to browsing session
browsing_session.append(1) # add address of website
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

# now when a user pushes a back button, we should remove that website from stack
last = browsing_session.pop()  # removes and returns the last value in the stack
print(last)
print(browsing_session)
# now return the user to the previous website
print("redirect", browsing_session[-1]) # browsing_session[-1] this gives the last item

# here we need to check if the stack is empty or not,
# if it is empty we need to disable the last button
# 0, "" empty string, [] empty list : are these are falsy values.
# ' not [] ' gives a boolean True

if not browsing_session: # check if the stack is empty, we can not go back anymore.
    print("disable back button")



