# Lesson how to break a for loop

successful = False  #True

for numbers in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:       # will be executed only if the loop completes without a early break statement
    print("Attempted 3 times and failed")