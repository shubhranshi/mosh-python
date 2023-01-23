## You will be given 3 chances to guess my secret number

secret_number = 9
guess_count = 0 #number of guesses
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed")


## in python, while blocks can optionally have else part too, just like if.
# if the while block executes successfully without any immediate break,
# then the else part get executed.