#define function with parameters
#parameters are the placeholders for receiving information in our function
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("John", "Smith")
greet_user("Mary", "Jones") #'Mary' is the argument, that we pass to the 'name' parameter
print("Finish")