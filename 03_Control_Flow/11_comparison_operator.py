# >, <, >=, <=, ==, !=
# Use comparison operator to compare values
# < strictly less than
# <= less than or equal
# > strictly greater than
# >= greater than or equal
# == equal
# != not equal
# is object identity
# is not negated object identity

print(10 > 3) #True
print(10 <= 3)  #False
print(10 == '10')   #False
print("bag" > "apple")  #True, because when we sort, bag comes after apple
print("bag" == "BAG")   #False, because the numeric representation of 'b' has a smaller value than 'B'
print(ord("b"), ord("B"))   #numeric value - ascii value : b - 98 , B - 66

temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

### exercise

name = input("Enter your name: ")
len_name = len(name)
if len_name < 3:
    print("Name must be at least 3 characters")
elif len_name > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("name looks good!")